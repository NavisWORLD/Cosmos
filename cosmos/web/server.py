from __future__ import annotations

from http import HTTPStatus
from http.server import BaseHTTPRequestHandler, HTTPServer
import json
from typing import Any

from ..config import CosmosConfig
from ..runtime import CosmosRuntime


class CosmosHandler(BaseHTTPRequestHandler):
    runtime: CosmosRuntime

    def _json(self, status: int, payload: dict[str, Any]) -> None:
        body = json.dumps(payload, ensure_ascii=False).encode("utf-8")
        self.send_response(status)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def _body(self) -> dict[str, Any]:
        length = int(self.headers.get("Content-Length", "0"))
        if length > 1_000_000:
            raise ValueError("request too large")
        raw = self.rfile.read(length) if length else b"{}"
        value = json.loads(raw.decode("utf-8"))
        if not isinstance(value, dict):
            raise ValueError("JSON body must be an object")
        return value

    def do_GET(self) -> None:  # noqa: N802
        if self.path == "/health":
            self._json(HTTPStatus.OK, {"ok": True, "service": "cosmos"})
        elif self.path == "/state":
            self._json(HTTPStatus.OK, self.runtime.status())
        else:
            self._json(HTTPStatus.NOT_FOUND, {"error": "not found"})

    def do_POST(self) -> None:  # noqa: N802
        try:
            body = self._body()
            if self.path == "/chat":
                result = self.runtime.process_turn(str(body.get("message", "")))
                self._json(HTTPStatus.OK, {"response": result.response, "state": result.state, "memories": result.memories, "backend": result.backend})
            elif self.path == "/sensory":
                packet = body.get("packet", body)
                if not isinstance(packet, dict):
                    raise ValueError("packet must be an object")
                self._json(HTTPStatus.OK, {"sensory": self.runtime.ingest_sensory(packet)})
            else:
                self._json(HTTPStatus.NOT_FOUND, {"error": "not found"})
        except (ValueError, json.JSONDecodeError) as exc:
            self._json(HTTPStatus.BAD_REQUEST, {"error": str(exc)})
        except Exception as exc:
            self._json(HTTPStatus.INTERNAL_SERVER_ERROR, {"error": str(exc)})

    def log_message(self, fmt: str, *args: object) -> None:
        return


def serve(config: CosmosConfig | None = None) -> None:
    cfg = config or CosmosConfig.from_env()
    runtime = CosmosRuntime(cfg)
    handler = type("ConfiguredCosmosHandler", (CosmosHandler,), {"runtime": runtime})
    server = HTTPServer((cfg.host, cfg.port), handler)
    try:
        print(f"COSMOS listening on http://{cfg.host}:{cfg.port}")
        server.serve_forever()
    finally:
        server.server_close()
        runtime.close()

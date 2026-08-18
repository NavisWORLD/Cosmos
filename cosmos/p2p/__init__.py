"""P2P namespace.

The public 3.0 core deliberately ships no unauthenticated WAN relay. Network transports
must be added as explicit, security-reviewed adapters.
"""


def status() -> dict[str, object]:
    return {"enabled": False, "transport": None, "reason": "no public WAN transport enabled by default"}

__all__ = ["status"]

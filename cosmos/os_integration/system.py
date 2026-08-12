from __future__ import annotations

import os
import platform


def system_summary() -> dict[str, object]:
    """Read-only host summary; this module does not kill processes or mutate the OS."""
    return {
        "platform": platform.platform(),
        "python": platform.python_version(),
        "cpu_count": os.cpu_count(),
    }

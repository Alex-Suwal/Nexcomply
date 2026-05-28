"""PyInstaller entrypoint for launching Nexcomply as a Windows executable."""

from pathlib import Path
import os
import sys


def _bundle_root() -> Path:
    if getattr(sys, "frozen", False) and hasattr(sys, "_MEIPASS"):
        return Path(sys._MEIPASS)
    return Path(__file__).resolve().parent


def main() -> int:
    bundle_root = _bundle_root()
    os.chdir(bundle_root)

    app_file = bundle_root / "app.py"
    if not app_file.exists():
        raise FileNotFoundError(f"Unable to find bundled app.py at {app_file}")

    from streamlit.web.cli import main as streamlit_main

    sys.argv = [
        "streamlit",
        "run",
        str(app_file),
        "--server.headless=true",
        "--global.developmentMode=false",
        "--browser.gatherUsageStats=false",
    ]

    return int(streamlit_main())


if __name__ == "__main__":
    raise SystemExit(main())

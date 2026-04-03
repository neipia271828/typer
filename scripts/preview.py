import os
import signal
import subprocess
import sys
import threading
import webbrowser


def main() -> int:
    host = os.environ.get("TYPER_DOCS_PREVIEW_HOST", "127.0.0.1")
    port = os.environ.get("TYPER_DOCS_PREVIEW_PORT", "8008")
    open_browser_enabled = (
        os.environ.get("TYPER_DOCS_PREVIEW_OPEN", "1").lower()
        not in {"0", "false", "no"}
    )
    url = f"http://{host}:{port}/"
    print(f"Preview: {url}")
    process = subprocess.Popen(
        ["mkdocs", "serve", "--dev-addr", f"{host}:{port}"],
    )

    def open_browser() -> None:
        webbrowser.open(url)

    timer = None
    if open_browser_enabled:
        timer = threading.Timer(2.0, open_browser)
        timer.daemon = True
        timer.start()

    def forward_signal(signum: int, frame: object) -> None:
        if process.poll() is None:
            process.send_signal(signum)

    signal.signal(signal.SIGINT, forward_signal)
    signal.signal(signal.SIGTERM, forward_signal)

    return_code = process.wait()
    if timer is not None:
        timer.cancel()
    return return_code


if __name__ == "__main__":
    sys.exit(main())

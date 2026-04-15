import os
import signal
import socket
import subprocess
import sys
import threading
import webbrowser


def _find_available_port(host: str, start_port: int, attempts: int = 20) -> int:
    for port in range(start_port, start_port + attempts):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            try:
                sock.bind((host, port))
            except OSError:
                continue
        return port
    raise RuntimeError(f"No available port found starting at {start_port}")


def main() -> int:
    host = os.environ.get("TYPER_DOCS_PREVIEW_HOST", "127.0.0.1")
    requested_port = int(os.environ.get("TYPER_DOCS_PREVIEW_PORT", "8008"))
    port = _find_available_port(host, requested_port)
    open_browser_enabled = (
        os.environ.get("TYPER_DOCS_PREVIEW_OPEN", "1").lower()
        not in {"0", "false", "no"}
    )
    url = f"http://{host}:{port}/"
    print(f"Preview: {url}")
    env = os.environ.copy()
    env.setdefault("DYLD_FALLBACK_LIBRARY_PATH", "/opt/homebrew/lib")
    process = subprocess.Popen(
        ["mkdocs", "serve", "--dev-addr", f"{host}:{port}"],
        env=env,
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

"""
app/server.py
──────────────
Serves the CropGuard AI web interface.

Usage:
    python app/server.py
    Then open http://localhost:8080 in your browser.
"""

import http.server
import socketserver
import os
import webbrowser
import threading

PORT = 8080
APP_DIR = os.path.dirname(os.path.abspath(__file__))


class Handler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=APP_DIR, **kwargs)

    def log_message(self, format, *args):
        # Clean log output
        print(f"  [{self.address_string()}] {format % args}")


def open_browser():
    import time
    time.sleep(1.2)
    webbrowser.open(f"http://localhost:{PORT}")


if __name__ == "__main__":
    print()
    print("=" * 50)
    print("  CropGuard AI — Web Server")
    print("=" * 50)
    print(f"  Serving from : {APP_DIR}")
    print(f"  URL          : http://localhost:{PORT}")
    print()
    print("  Opening browser automatically...")
    print("  Press Ctrl+C to stop the server.")
    print()

    # Open browser in background thread
    threading.Thread(target=open_browser, daemon=True).start()

    with socketserver.TCPServer(("", PORT), Handler) as httpd:
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\n  Server stopped.")

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Local HTTP Server for DeutschMeister Web Preview
Serves tools/ directory so index.html can load ../curriculum.json via standard fetch.
"""

import http.server
import socketserver
import os
import webbrowser
import sys

PORT = 8080

class Handler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        # Serve from project tools directory so ../curriculum.json is accessible
        tools_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        super().__init__(*args, directory=tools_dir, **kwargs)

def main():
    port = PORT
    if len(sys.argv) > 1 and sys.argv[1].isdigit():
        port = int(sys.argv[1])

    url = f"http://localhost:{port}/web_preview/index.html"
    print("=" * 60)
    print(f"DeutschMeister 开发预览工具本地服务器启动中...")
    print(f"URL: {url}")
    print("按 Ctrl+C 停止服务器")
    print("=" * 60)

    try:
        with socketserver.TCPServer(("", port), Handler) as httpd:
            if "--open" in sys.argv:
                webbrowser.open(url)
            httpd.serve_forever()
    except KeyboardInterrupt:
        print("\n服务器已停止。")
    except OSError as e:
        print(f"端口 {port} 可能被占用: {e}")

if __name__ == "__main__":
    main()

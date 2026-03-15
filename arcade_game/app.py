"""
Pixel Quest - Classic Arcade Game Server
A nostalgic arcade game with retro pixel art style
"""

import http.server
import socketserver
import os

PORT = 8001
DIRECTORY = os.path.dirname(os.path.abspath(__file__))

class MyHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    """Custom HTTP request handler"""
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=DIRECTORY, **kwargs)
    
    def end_headers(self):
        """Add custom headers"""
        self.send_header('Cache-Control', 'no-store, no-cache, must-revalidate')
        self.send_header('Access-Control-Allow-Origin', '*')
        return super().end_headers()

def run_server():
    """Start the HTTP server"""
    try:
        with socketserver.TCPServer(("", PORT), MyHTTPRequestHandler) as httpd:
            print(f"""
╔════════════════════════════════════════════════════════════╗
║          PIXEL QUEST - Classic Arcade Game                 ║
╚════════════════════════════════════════════════════════════╝

✓ Server running at: http://localhost:{PORT}
✓ Serving files from: {DIRECTORY}
✓ Press Ctrl+C to stop the server

Open your browser and navigate to http://localhost:{PORT}
            """)
            httpd.serve_forever()
    except KeyboardInterrupt:
        print("\n\n✓ Server stopped successfully!")
    except OSError as e:
        print(f"✗ Error: {e}")
        print(f"✗ Port {PORT} might be in use. Try a different port.")

if __name__ == "__main__":
    run_server()

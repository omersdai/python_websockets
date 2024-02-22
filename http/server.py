import http.server
import socketserver

class WebSocketHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.headers.get('Upgrade') == 'websocket':
            self.handle_websocket()
        else:
            super().do_GET()

    def handle_websocket(self):
        self.send_response(101)
        self.send_header('Upgrade', 'websocket')
        self.send_header('Connection', 'Upgrade')
        self.send_header('Sec-WebSocket-Accept', '...')
        self.end_headers()

        while True:
            # Handle WebSocket communication here
            pass


PORT = 8765
with socketserver.TCPServer(('', PORT), WebSocketHandler) as httpd:
    print(f"WebSocket server running at port {PORT}")
    httpd.serve_forever()

from http.server import BaseHTTPRequestHandler, HTTPServer
import json

PORT = 3000

class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/hello":
            self.respond(200, {"message": "Hello, World!"})
        elif self.path == "/about":
            self.respond(200, {"name": "Mini Backend", "author": "Abdullah", "university": "Air University"})
        else:
            self.respond(404, {"error": "Route not found"})

    def respond(self, status, data):
        body = json.dumps(data).encode()
        self.send_response(status)
        self.send_header("Content-Type", "application/json")
        self.end_headers()
        self.wfile.write(body)

if __name__ == "__main__":
    print(f"Server running at http://localhost:{PORT}")
    HTTPServer(("", PORT), Handler).serve_forever()
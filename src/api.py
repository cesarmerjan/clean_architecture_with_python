"""
Responsible for receiving data from client and forwarding as the controller.
"""
import cgi
import http
import http.server
import json

from config import API_HOST, API_PORT
from src.controllers import api_cli_sign_up


class Handler(http.server.BaseHTTPRequestHandler):

    def do_POST(self):
        if self.path == "/sign_up":
            ctype, pdict = cgi.parse_header(self.headers.get("content-type"))

            if ctype != "application/json":
                self.send_response(http.HTTPStatus.BAD_REQUEST)
                self.end_headers()
                return

            content_len = int(self.headers.get("content-length", 0))

            post_body = self.rfile.read(content_len)
            _json: str = json.loads(post_body.decode())

            view = api_cli_sign_up(**_json)

            self.send_response(view.status_code)
            for header in view.headers:
                self.send_header(header[0], header[1])
            self.end_headers()

            self.wfile.write(bytes(view.body, "utf-8"))


def create_server(port: int, host: str) -> http.server.HTTPServer:
    server = http.server.HTTPServer((port, host), Handler)
    return server


if __name__ == "__main__":

    server = create_server(API_HOST, API_PORT)

    try:
        print(f"Server started at {API_PORT}")
        server.serve_forever()
    except KeyboardInterrupt:
        server.server_close()
        server.shutdown()
        server.socket.close()

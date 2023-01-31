"""
Responsible for receiving data from client and forwarding as the controller.
"""
import cgi
import http
import http.server
import json

from src.controllers import sign_in
from config import API_PORT, API_HOST


class Handler(http.server.BaseHTTPRequestHandler):
    def _set_headers(self):
        self.send_response(200)
        self.send_header("Content-type", "application/json")
        self.end_headers()

    def do_HEAD(self):
        self._set_headers()

    def do_POST(self):
        if self.path == "/sign_in":
            ctype, pdict = cgi.parse_header(self.headers.get("content-type"))

            if ctype != "application/json":
                self.send_response(http.HTTPStatus.BAD_REQUEST)
                self.end_headers()
                return

            content_len = int(self.headers.get("content-length", 0))

            post_body = self.rfile.read(content_len)
            _json: str = json.loads(post_body.decode())
            view = sign_in(**_json)

            self._set_headers()
            payload = json.dumps(view.data)
            self.wfile.write(bytes(payload, "utf-8"))

            if view.is_successful:
                self.send_response(http.HTTPStatus.CREATED)
            else:
                self.send_response(http.HTTPStatus.INTERNAL_SERVER_ERROR)


if __name__ == "__main__":

    server = http.server.HTTPServer((API_HOST, API_PORT), Handler)

    try:
        print(f"Server started at {API_PORT}")
        server.serve_forever()
    except KeyboardInterrupt:
        server.server_close()
        server.shutdown()
        server.socket.close()

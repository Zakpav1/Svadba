from http.server import BaseHTTPRequestHandler, HTTPServer
import urllib.parse

class RequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/':
            self.send_response(200)
            self.send_header('Content-type', 'text/html; charset=utf-8')
            self.end_headers()
            with open('index.html', 'rb') as file:
                self.wfile.write(file.read())
        elif self.path == '/style.css':
            try:
                with open('style.css', 'rb') as file:
                    self.send_response(200)
                    self.send_header('Content-type', 'text/css')
                    self.end_headers()
                    self.wfile.write(file.read())
            except FileNotFoundError:
                self.send_error(404, "File not found")
        elif self.path == '/favicon.ico':
            # Игнорируем запросы к favicon.ico
            self.send_response(204)
            self.end_headers()
        else:
            self.send_error(404, "Page not found")

    def send_error(self, code, message=None):
        try:
            if message:
                message = message.encode('utf-8').decode('latin-1')
            super().send_error(code, message)
        except UnicodeEncodeError:
            super().send_error(code, "Page not found")

def run(server_class=HTTPServer, handler_class=RequestHandler, port=8000):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print(f'Сервер запущен на http://localhost:{port}')
    httpd.serve_forever()

if __name__ == '__main__':
    run()
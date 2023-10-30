import http.server
import socketserver

class HeaderDisplayHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        
        headers = self.headers
        header_list = "<ul>"
        for header, value in headers.items():
            header_list += f"<li><strong>{header}:</strong> {value}</li>"
        header_list += "</ul>"
        
        response = f"<html><body><h1>Headers</h1>{header_list}</body></html>"
        self.wfile.write(response.encode())

PORT = 8000

with socketserver.TCPServer(("", PORT), HeaderDisplayHandler) as httpd:
    print(f"Serving at port {PORT}")
    httpd.serve_forever()

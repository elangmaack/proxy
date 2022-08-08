import socketserver
import http.server
import urllib.request

PORT = 9097


class MyProxy(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        url=self.path[1:]
        self.send_response(200)
        self.end_headers()
        self.copyfile(urllib.request.urlopen(url), self.wfile)

httpd = socketserver.ThreadingTCPServer(('', PORT), MyProxy)
print ("Now serving at")
httpd.serve_forever()

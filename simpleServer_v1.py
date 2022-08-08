import socketserver
import http.server
import urllib.request

PORT = 9097

class MyProxy(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        url=self.path[1:]


        #self.copyfile(urllib.request.urlopen(url), self.wfile)

        try:
            self.send_response(200)
            self.end_headers()
            self.copyfile(urllib.request.urlopen(url), self.wfile)
        except Exception as err:
            exception_type = type(err).__name__
            print(exception_type)
            return


httpd = socketserver.ThreadingTCPServer(('', PORT), MyProxy)
print ("Now serving at")
httpd.serve_forever()

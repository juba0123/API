from http.server import HTTPServer, SimpleHTTPRequestHandler
import ssl
import sys

arguments = str(sys.argv)
port = sys.argv[2]
port = int(port)
httpd = HTTPServer(('localhost', port), SimpleHTTPRequestHandler)
httpd.socket = ssl.wrap_socket(httpd.socket, certfile='/home/juba/Bureau/test_stage_ftn/server.pem', server_side=True)
httpd.serve_forever()

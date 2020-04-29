#!/usr/bin/env python
"""
Very simple HTTP server in python.

Usage::
    ./dummy-web-server.py [<port>]

Send a GET request::
    curl http://localhost

Send a HEAD request::
    curl -I http://localhost

Send a POST request::
    curl -d "foo=bar&bin=baz" http://localhost

"""
import subprocess
from http.server import BaseHTTPRequestHandler, HTTPServer
import socketserver

secret = "floofball"

class Pipeline:

    def __init__(self, directory):
        self.directory = directory
        self.deploy_directory = deploy_directory
        self.scripts = ["update.sh", "deploy.sh"]

    def run_command(self, bash_command):
        process = subprocess.Popen(bash_command.split(), stdout=subprocess.PIPE)
        return process.communicate()

    def run_pipeline(self):
        command = "cd {} && ".format(directory)
        for script in self.scripts:
            command += "./{} '{}' && ".format(script, self.directory)
        command += "echo Finished"
        self.run_command(command)
        

class S(BaseHTTPRequestHandler):
    def _set_headers(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()

    def do_GET(self):
        print(self.headers)
        self._set_headers()
        print(self.headers)
        self.wfile.write(bytes("<html><body><h1>hi! we have updated</h1></body></html>", encoding="utf-8"))

    def do_HEAD(self):
        self._set_headers()
        
    def do_POST(self):
        # Doesn't do anything with posted data
        if "cicd" in self.path:
            pipeline = Pipeline("cicd", ".")
        else:
            pipeline = Pipeline("sunrise", "/home/pi/Devel/sunrise")
        pipeline.run_pipeline()

        self._set_headers()
        content_len = int(self.headers.getheader('content-length', 0))
        post_body = self.rfile.read(content_len)
        print(post_body + "\n")
        self.wfile.write("<html><body><h1>POST!</h1></body></html>")

        
def run(server_class=HTTPServer, handler_class=S, port=80):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print('Starting httpd...')
    httpd.serve_forever()

if __name__ == "__main__":
    from sys import argv

    if len(argv) == 2:
        run(port=int(argv[1]))
    else:
        run()

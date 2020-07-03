# coding: utf-8
from wsgiref.simple_server import make_server


def app(env, resp):
    for k in env:
        print(k)
    resp("200 OK", [('Content-Type', 'text/html')])
    return "hello world"


httpd = make_server("", 8080, app)
print("server start...")
httpd.serve_forever()

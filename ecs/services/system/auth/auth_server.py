# -*- coding: utf-8 -*-
__author__ = 'zhangkaixuan'

from wsgiref.simple_server import make_server

from webob import Request

from common import auth


def application(environ, start_response):
    standard_request = Request(environ)
    userName = standard_request.headers.get('X-Auth-User', '')
    userKey = standard_request.headers.get('X-Auth-Key', '')
    response_body = auth(userName, userKey)
    if response_body == "OK":
        status = '200 OK'

    else:
        status = '401 ERROR'
    response_headers = [('Content-Type', "text/plain"),
                        ('Content-Length', str(len(response_body)))]
    start_response(status, response_headers)

    return response_body


if __name__ == '__main__':
    httpd = make_server(
        'localhost',
        8888,
        application
    )

    httpd.serve_forever()
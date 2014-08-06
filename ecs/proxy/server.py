# -*- coding: utf-8 -*-
"""
Created on 2013年9月11日

@author: adrian
"""
import os
from paste.deploy import loadapp

from eventlet import wsgi
import eventlet

from ecs.util.params import PROXY_SERVER_CONFIG


class Server():
    def __init__(self):
        pass

    def start(self):
        configfile = PROXY_SERVER_CONFIG
        appname = "scloud_proxy"
        wsgi_app = loadapp("config:%s" % os.path.abspath(configfile), appname)
        wsgi.server(eventlet.listen(('localhost', 8080)), wsgi_app)

    def stop(self):
        pass

    def restart(self):
        self.stop()
        self.start()

if __name__ == '__main__':
    scloud_server = Server()
    scloud_server.start()




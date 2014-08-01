# -*- coding: utf-8 -*-
__author__ = 'zhangkaixuan'

import socket
port = 43278
s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
s.bind(("", port))
print 'waiting on port:', port
while True:
    data, addr = s.recvfrom(1024)
    print 'recived:',data,"from",addr
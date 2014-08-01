__author__ = 'zhangkaixuan'

import socket
import time

MONITOR_SERVER_IP = '127.0.0.1'
SERVER_PORT = 43278
BEAT_PERIOD = 10

print 'Sending heartbeat to IP %s , port %d' % (MONITOR_SERVER_IP, SERVER_PORT)
while True:
    hbSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    hbSocket.sendto('hello,i am agent ,this message stands that i am alive ^@^', (MONITOR_SERVER_IP, SERVER_PORT))
    if __debug__:
        print 'Time: %s' % time.ctime( )
    time.sleep(BEAT_PERIOD)
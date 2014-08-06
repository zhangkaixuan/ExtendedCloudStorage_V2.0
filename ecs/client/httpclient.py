__author__ = 'zhangkaixuan'
import httplib

from ecs.util.params import PROXY_SERVER_URL, CDMI_VERSION
from ecs.util.tools import md5, encrypt


class ECSClient:
    def __init__(self, conn):
        self.conn = conn
        self.heads = {"X-CDMI-Specification-Version":CDMI_VERSION}
        self.body = None
        self.params = {}
        self.method = "GET"
        self.host = "cloud.ecust.edu.cn"
        self.path = "/"

    def setAcceptType(self, accepttype):
        self.heads.setdefault("Accept", accepttype)

    def setMethod(self, method):
        self.method = method

    def setHost(self, host):
        self.host = host

    def setPath(self, path):
        self.path = path

    def setUser(self, user):
        u = encrypt(10,user)
        self.heads.setdefault("X-Auth-User", u)

    def setPassWord(self, password):
        ciphertext = md5(password)
        self.heads.setdefault("X-Auth-Key", ciphertext)

    def setBody(self, body):
        self.body = body


    def sendRequest(self):
        self.conn.request(self.method, self.path, self.body, self.heads)
        response = self.conn.getresponse(buffering = False)
        data = response.read()
        print data


if __name__ == '__main__':

    conn = httplib.HTTPConnection(PROXY_SERVER_URL)
    client = ECSClient(conn)
    client.setUser("045130160")
    client.setPassWord("oooooo")
    client.setAcceptType("text/plain")
    client.sendRequest()
    conn.close()


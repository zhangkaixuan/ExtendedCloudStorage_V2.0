__author__ = 'zhangkaixuan'

import json

from urlparse import urlparse, urljoin
from urllib import quote
from httplib import HTTPConnection


def http_connection(url):
    parsed = urlparse(url)
    conn = HTTPConnection(parsed.netloc)
    return parsed, conn


def json_request(method, url, **kwargs):
    kwargs.setdefault('headers', {})
    kwargs['headers']['Content-Type'] = 'application/json'
    kwargs['body'] = json.dumps(kwargs['body'])
    parsed, conn = http_connection(url)
    conn.request(method, parsed.path, **kwargs)
    resp = conn.getresponse()
    body = resp.read()
    body = json.loads(body)
    return resp, body


def get_auth():
    url = 'http://192.168.1.108:5000/v2.0/'
    body = {'auth': {'passwordCredentials': {'password': 'ADMIN',
                                             'username': 'admin'}, 'tenantName': 'admin'}}
    token_url = urljoin(url, "tokens")
    resp, body = json_request("POST", token_url, body=body)
    token_id = None
    try:
        url = None
        catalogs = body['access']["serviceCatalog"]
        for service in catalogs:
            if service['type'] == 'object-store':
                url = service['endpoints'][0]['publicURL']
        token_id = body['access']['token']['id']
    except(KeyError, IndexError):
        print "error"
    return url, token_id


def get_object():
    """

    :rtype : object
    """
    url, token = get_auth()
    parsed, conn = http_connection(url)
    path = '%s/%s/%s' % (parsed.path, quote('myfile'), quote('asd.txt'))
    method = 'GET'
    headers = {'X-Auth-Token': token}
    conn.request(method, path, '', headers)
    resp = conn.getresponse()
    body = resp.read()
    print body


if __name__ == '__main__':
    # get_object()
    print get_auth()
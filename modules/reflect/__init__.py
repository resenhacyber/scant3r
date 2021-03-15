from core.libs import insert_to_params_urls  as ur
from core.libs import random_str
from urllib.parse import urlparse
import random

class Reflect:
    def __init__(self,r):
        self.http = r
    def start(self,url,method):
        http = self.http
        self.found = list()
        txt = f'scan{random_str(3)}tr'
        if urlparse(url).query:
            nurls = ur(url,txt)
        else:
            return []
        for nurl in nurls:
            if method == 'GET':
                r = http.send(method,nurl)
            else:
                r = http.send(method,nurl.split('?')[0],body=urlparse(nurl).query)
            if txt in r.content.decode('utf-8'):
                self.found.append(txt)
        return self.found
def main(opts,r):
    R = Reflect(r)
    for method in opts['methods']:
        v = R.start(opts['url'],method)
        if v:
            print(f'[Refelct] Found :> {v}')

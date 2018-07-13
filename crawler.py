import json
from setting import REDIS_KEY
import requests
from db import RedisClient

class Crawler(object):
    def __int__(self):
        self.client = RedisClient()

    def getProxies(self,API):
        response = requests.get(API)
        if response:
            j = json.loads(response.text)
            for item in j["RESULT"]:
                proxy = str(item['ip'])+":"+str(item['port'])
                self.client.add(REDIS_KEY,proxy)
                print("成功获取到代理["+str(proxy)+"]")


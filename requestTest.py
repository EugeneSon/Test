import requests

class ReqeustTest:
    async def rTest(self, i):
        r = requests.get('http://naver.com')
        return i, r
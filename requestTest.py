import requests

class ReqeustTest:
    async def asyncFun(self, session, i):
        async with session.get('http://naver.com') as response:
            res = await response.text()

        return i, res

    def normalFun(self, i):
        r = requests.get('http://naver.com')
        return r
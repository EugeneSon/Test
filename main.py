# import SingletonTest
#
# def test():
#     s = SingletonTest.Singleton()
#     s1 = SingletonTest.Singleton()
#     print(s)
#     print(s1)
#
#
# # Press the green button in the gutter to run the script.
# if __name__ == '__main__':
#     test()
#---------------------------------------------------------------------
import asyncio
import aiohttp
from time import time

from requestTest import ReqeustTest

result = []
async def main():
    test = ReqeustTest()
    async with aiohttp.ClientSession() as session:
        results = await asyncio.gather(*[test.asyncFun(session, i) for i in range(1, 11)])

    for r in result:
        print(r)

if __name__ == '__main__':
    begin = time()
    asyncio.run(main())
    end = time()
    print('실행 시간: {0:.3f}초'.format(end - begin))
#---------------------------------------------------------------------
# result = []
# def main():
#     test = ReqeustTest()
#     for i in range(1,11):
#         result.append(test.normalFun(i))
#
#     for r in result:
#         print(r)
#
# if __name__ == '__main__':
#     begin = time()
#     main()
#     end = time()
#     print('실행 시간: {0:.3f}초'.format(end - begin))
#---------------------------------------------------------------------
# from time import time
# from urllib.request import Request, urlopen
# import asyncio
#
# urls = ['https://www.google.co.kr/search?q=' + i
#         for i in ['apple', 'pear', 'grape', 'pineapple', 'orange', 'strawberry']]
#
#
# async def fetch(url):
#     request = Request(url, headers={'User-Agent': 'Mozilla/5.0'})  # UA가 없으면 403 에러 발생
#     response = await loop.run_in_executor(None, urlopen, request)  # run_in_executor 사용
#     page = await loop.run_in_executor(None, response.read)  # run in executor 사용
#     return len(page)
#
#
# async def main():
#     futures = [asyncio.ensure_future(fetch(url)) for url in urls]
#     print(futures)
#     # 태스크(퓨처) 객체를 리스트로 만듦
#     result = await asyncio.gather(*futures)  # 결과를 한꺼번에 가져옴
#     print(result)
#
#
# begin = time()
# loop = asyncio.get_event_loop()  # 이벤트 루프를 얻음
# loop.run_until_complete(main())  # main이 끝날 때까지 기다림
# loop.close()  # 이벤트 루프를 닫음
# end = time()
# print('실행 시간: {0:.3f}초'.format(end - begin))
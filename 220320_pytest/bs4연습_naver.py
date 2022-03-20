import requests as req
# request modue => 웹페이지를 요청하고 응답 데이터를 받을 수 있음
from bs4 import BeautifulSoup
# bs4 import Error : https://pycoding.tistory.com/entry/%ED%8C%8C%EC%9D%B4%EC%8D%AC-bs4-%EC%97%90%EB%9F%AC-ImportError-cannot-import-name-BeautifulSoup-from-bs4

#요청시 헤더 정보를 크롬으로 지정
request_headers = { 'User-Agent' : ('Mozilla/5.0 (Windows NT 10.0;Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98Safari/537.36'), }
# 네이버의 경우 알 수 없는 정보들을 다 쳐내기 때문에 기기정보를 작성해주는 것

r = req.get('https://news.naver.com/', headers = request_headers)
# print(r)

# html code 읽어와야 됨
# print(r.text)

# html code parser
soup = BeautifulSoup(r.text, 'html.parser')

list = soup.select(".cjs_channel_card")
print(list)
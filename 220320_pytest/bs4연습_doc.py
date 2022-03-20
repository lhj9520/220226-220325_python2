import requests as req
# request modue => 웹페이지를 요청하고 응답 데이터를 받을 수 있음
from bs4 import BeautifulSoup
# bs4 import Error : https://pycoding.tistory.com/entry/%ED%8C%8C%EC%9D%B4%EC%8D%AC-bs4-%EC%97%90%EB%9F%AC-ImportError-cannot-import-name-BeautifulSoup-from-bs4

# html tag를 알려주는 모듈을 사용해서 html 해석을 해야함
html_doc = """<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>
"""
# print(html_doc)
soup = BeautifulSoup(html_doc, 'html.parser')
# print(soup.prettify())

# select()를 이용해 html tag 선택
# print(soup.select("a"))
list = soup.select("a")
print(list[1])

# 텍스트 가져오기
print(list[1].text)

# 속성값을 가져오기 <태그명 속성명="속성값">
print(list[1]["href"])
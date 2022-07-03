# 강의 노트는 <뉴스 제목 + 링크 크롤링>에 있다.

import requests
from bs4 import BeautifulSoup

response = requests.get("https://search.naver.com/search.naver?where=news&sm=tab_jum&query=%EC%82%BC%EC%84%B1%EC%A0%84%EC%9E%90") # 괄호 안에는 사이트 주소 입력
html = response.text # response에서 text 파일을 가져온다.

soup = BeautifulSoup(html, 'html.parser') # 위에서 가져온 html 텍스트는 그대로 사용하기 힘드므로 html.parser 번역 선생님을 사용한다.
# 그걸 soup에 저장
links = soup.select(".news_tit") # select에서 Ctrl + F 로 테스트 해본 선택자를 가져온다.
# print(links) # 리스트 형태로 출력 # 리스트 형태는 for문으로 추가 처리가 가능하다.

for link in links:
    title = link.text # link를 뽑아서 그 안에 text 요소만 가져온다.
    url = link.attrs['href'] # herf의 속성값을 가져온다. (이거는 외우기)
    print(title, url)
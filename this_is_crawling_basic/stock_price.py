# <네이버 주식 현재가 크롤링>

import requests
from bs4 import BeautifulSoup

# 종목 코드 리스트
codes = ['005930','000660','035720']

for code in codes:
    url = f"https://finance.naver.com/item/sise.naver?code={code}"
    response = requests.get(url) # get 명령어로 url에서 response를 받아왔다.
    html = response.text # response를 text 형태로 해서 html에 저장한다.
    soup = BeautifulSoup(html, 'html.parser') # html 통으로 되어 있으면 구분이 어려우므로 BeautifulSoup를 사용한다.
    # name = soup.select_one(".wrap_company").text
    price = soup.select_one("#_nowVal").text # 사용해서 만든 soup 중 _nowVal이라는 id(#)를 갖고 있는 걸 하나 가져오고 그것 중 text만 선택한다.
    price = price.replace(',','')
    print(price)
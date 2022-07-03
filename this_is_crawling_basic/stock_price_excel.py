# <네이버 주식 현재가 크롤링>

import requests
from bs4 import BeautifulSoup
import openpyxl

fpath = r'C:\Users\jinho\Desktop\list.xlsx'

# 종목 코드 리스트
codes = ['005930','000660','035720']
# excel 데이터 저장 시 사용할 반복 변수
row = 1

wb = openpyxl.load_workbook(fpath) # 파일 열기
ws = wb['첫번째_시트'] # 엑셀 시트 선택

for code in codes:
    url = f"https://finance.naver.com/item/sise.naver?code={code}"
    response = requests.get(url) # get 명령어로 url에서 response를 받아왔다.
    html = response.text # response를 text 형태로 해서 html에 저장한다.
    soup = BeautifulSoup(html, 'html.parser') # html 통으로 되어 있으면 구분이 어려우므로 BeautifulSoup를 사용한다.
    # name = soup.select_one(".wrap_company").text
    price = soup.select_one("#_nowVal").text # 사용해서 만든 soup 중 _nowVal이라는 id(#)를 갖고 있는 걸 하나 가져오고 그것 중 text만 선택한다.
    price = price.replace(',','') # 가격에 ,가 붙어 있었는데 그걸 제거한다.
    ws[f'A{row}'] = int(price) # 워크시트에 데이터 저장
    row = row + 1

wb.save(fpath) # 파일 저장
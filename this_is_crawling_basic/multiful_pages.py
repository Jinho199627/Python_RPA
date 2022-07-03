# 강의 노트: <여러 페이지 결과 모두 가져오기>

import requests
import pyautogui
from bs4 import BeautifulSoup

keyword = pyautogui.prompt("input search word.")
lastpage = int(pyautogui.prompt("input last page number")) # str 형태로 저장되므로 int 형으로 바꾼다.
page_num = 1
for i in range(1,lastpage*10,10): # 네이버 뉴스 쿼리에선 'start = 페이지 넘버 구분' 이었다.
    print(f"{page_num}페이지 입니다.================================")
    response = requests.get(f"https://search.naver.com/search.naver?where=news&sm=tab_jum&query={keyword}&start={i}") # 괄호 안에는 사이트 주소 입력
    html = response.text # response에서 text 파일을 가져온다.

    soup = BeautifulSoup(html, 'html.parser') # 위에서 가져온 html 텍스트는 그대로 사용하기 힘드므로 html.parser 번역 선생님을 사용한다.
    # 그걸 soup에 저장
    links = soup.select(".news_tit") # select에서 Ctrl + F 로 테스트 해본 선택자를 가져온다.
    # print(links) # 리스트 형태로 출력 # 리스트 형태는 for문으로 추가 처리가 가능하다.

    for link in links:
        title = link.text # link를 뽑아서 그 안에 text 요소만 가져온다.
        url = link.attrs['href'] # herf의 속성값을 가져온다. (이거는 외우기)
        print(title, url)
    page_num = page_num + 1
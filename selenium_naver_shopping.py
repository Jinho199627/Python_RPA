from selenium import webdriver
from selenium.webdriver.common.keys import Keys # 엔터키 치기 위한 라이브러리
import time
import csv

f = open(r"C:\Users\82107\Desktop\data.csv", 'w', encoding='cp949', newline='')
# 경로, 쓰기모드, 인코딩(한글 깨짐 방지), 자동 줄바꿈 없음
csvwriter = csv.writer(f)


browser = webdriver.Chrome('C:/chromedriver.exe') # 브라우져 생성
browser.get('https://www.naver.com') # 웹 사이트 열기
browser.implicitly_wait(10) # 브라우져를 여는데 시간이 많이 걸리면 이어지는 명령어 수행이 불가하므로 시간 초 여유를 준다.

browser.find_element_by_css_selector('a.nav.shop').click() # 네이버 메인에서 쇼핑 클릭
time.sleep(2) # 2초간의 시간 여유를 준다.

search = browser.find_element_by_css_selector('input._searchInput_search_input_QXUFf') # 검색창
search.click()

search.send_keys('아이폰 13')
search.send_keys(Keys.ENTER)

# 스크롤 전 높이(자바스크립트 명령어를 사용할 수 있게 도와줌 execute_script)
before_h = browser.execute_script("return window.scrollY")
# 자바 스크립트로 return window.scrollY를 해준다는 말이다.

# 무한(반복문) 스크롤
while True:
    # 맨 아래로 스크롤을 내린다.
    browser.find_element_by_css_selector("body").send_keys(Keys.END) # END 키를 눌러주기
    time.sleep(2) # 스크롤 사이 페이지 로딩 시간
    after_h = browser.execute_script("return window.scrollY")

    if after_h == before_h:
        break # 더 이상 내릴 수 없을 때까지 내린다는 의미
    before_h = after_h

# 상품 정보 div
items = browser.find_elements_by_css_selector(".basicList_info_area__17Xyo")
for item in items:
    name = item.find_element_by_css_selector(".basicList_title__3P9Q7").text # 검색했을 때 나오는 개수가 같아야 한다.
    try:
        price = item.find_element_by_css_selector("span.price_num__2WUXn").text
    except:
        price = "판매중단" # 가격 정보가 없으면 판매중단 이라고 처리해준다.
    link = item.find_element_by_css_selector(".basicList_title__3P9Q7 > a").get_attribute('href')
    # 자식클래스 선택 basicList_title__3P9Q7 아래 a태그
    # print(name, price, link)
    csvwriter.writerow([name, price, link])

# 파일 닫기
f.close()

f = open(r"C:\Users\82107\Desktop\data.csv", 'r')
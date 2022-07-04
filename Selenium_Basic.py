import imp
from attr import s
from selenium import webdriver
from selenium.webdriver.common.keys import Keys # 엔터키 치기 위한 라이브러리
import time

browser = webdriver.Chrome('C:/chromedriver.exe') # 브라우져 생성
browser.get('https://www.naver.com') # 웹 사이트 열기
browser.implicitly_wait(10) # 브라우져를 여는데 시간이 많이 걸리면 이어지는 명령어 수행이 불가하므로 시간 초 여유를 준다.

browser.find_element_by_css_selector('a.nav.shop').click() # 네이버 메인에서 쇼핑 클릭
time.sleep(2) # 2초간의 시간 여유를 준다.

search = browser.find_element_by_css_selector('input._searchInput_search_input_QXUFf') # 검색창
search.click()

search.send_keys('아이폰 13')
search.send_keys(Keys.ENTER)
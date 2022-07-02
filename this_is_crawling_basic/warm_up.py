from urllib import response
import requests # 라이브러리를 불러오고
from bs4 import BeautifulSoup


response = requests.get("https://www.naver.com") # 네이버로 접속해 get 요청을 사용한다. 그리고 그 응답을 reponse 안에 넣어라.
html = response.text # response.text 안에는 html 코드가 들어있다. 그것을 html이라는 변수에 넣는다.
soup = BeautifulSoup(html, 'html.parser') # BeautifulSoup 사용
word = soup.select_one("#NM_set_home_btn") # soup로 원하는 태그를 선택할 수 있다.
            #select: 여러 개 선택, select_one: 한 개 선택
print("word")
print(word)
print("\n\nword.text")
print(word.text) # 선택한 요소에 대한 text 부분만 가져오기

# 네이버 메인에서 F12 누르고 돋보기로 '네이버를 시작페이지로' 버튼을 누르면 이런 HTML 문이 있다.
# <a id="NM_set_home_btn" href="https://help.naver.com/support/welcomePage/guide.help" class="link_set" data-clk="top.mkhome">네이버를 시작페이지로</a>
    #id는 고유의 값이라 선택하기 가장 용이하다. 그래서 이걸 가져오는데 id는 앞에 #을 붙여줘야 한다. '#NM_set_home_btn'
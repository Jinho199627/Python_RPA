# https://www.youtube.com/watch?v=aYwg1H5BK04&t=305s&ab_channel=%EA%B8%B0%EC%88%A0%EB%85%B8%ED%8A%B8with%EC%95%8C%EB%A0%89
# 크롤링: 웹사이트에서 HTML 데이터를 가져오고 parsing(분석, 구분) 해주는 기능

from urllib.request import urlopen
from bs4 import BeautifulSoup
# 관련 라이브러리를 cmd 창에서 설치(pip install)해야 한다.

# HTML에서 태그 데이터를 가져옴
html = urlopen("https://news.naver.com/")

# HTML에서 접근할 수 있게 해주는 것
bsObject = BeautifulSoup(html, "html.parser")

# 링크를 다 가져온다.
for link in bsObject.find_all('a'):
    print(link.text.strip(), link.get('href'))

# 이미지를 다 가져온다.
# for link in bsObject.find_all('img'):
#     print(link.text.strip(), link.get('src'))
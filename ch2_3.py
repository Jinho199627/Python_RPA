# 파이썬 업무 자동화 ch 2의 3장

import random
# chars = "abcdegf"
# print(random.choice(chars))

import time
# print(str(time.time())[-2:])
## 무작위 숫자를 생성하는 방법

import os
os.listdir()
# 폴더 안의 내용물을 리스트로 만들어준다.

# 결과물 파일을 생성합니다. 텅 빈 텍스트파일이 생성됩니다.
# out_file = open(outfile_name, 'w')

# 폴더의 내용물을 열람해 목록을 생성합니다.
# input_files = os.listdir(directory)

# 한글 인코딩 필수 코드
#-*-coding:euc-kr

test_list = ["abcd", "efgh"]
print(test_list[-1])
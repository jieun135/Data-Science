# 인프런 인기 강의 정보 수집하기

import requests
from bs4 import BeautifulSoup
from urllib.request import urlretrieve

raw = requests.get("https://www.inflearn.com/courses?level=level-1&view=list&order=popular",headers = {"User-Agent":"Mozilla/5.0"})
html = BeautifulSoup(raw.text, 'html.parser')

# 컨테이너 div.box
movies = html.select("div.box")

for m in movies:
    # 제목 div.content_container h2
    title = m.select_one("div.content_container h2")
    # 카테고리  div.tags
    tag = m.select_one("div.tags").text.strip()

    # 상세 페이지 들어가기
    url = title.attrs["href"]
    raw_each = requests.get("https://www.inflearn.com"+url, headers={"User-Agent": "Mozilla/5.0"})
    html_each = BeautifulSoup(raw_each.text, 'html.parser')

    try:
        # 수강 대상 div.student_targer ul
        student = html_each.select_one("div.student_target ul").text
        # 강의 평점 div.average span
        score = html_each.select_one("div.average span").text
    except:
        print("<"+title.text.strip()+">","해당정보가 없습니다.")
        print("=" * 50)
        continue
    #출력
    print("강의 제목: ",title.text.strip())
    print("-"*50)
    print("강의 카테고리 : ")
    print(tag)
    print("-" * 50)
    print("수강대상: ", student)
    print("-" * 50)
    print("강의 평점 ", score)
    print("="*50)

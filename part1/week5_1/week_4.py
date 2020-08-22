# 네이버 영화 데이터 수집

import requests
from bs4 import BeautifulSoup

raw = requests.get("https://movie.naver.com/movie/running/current.nhn#",
                   headers = {"User-Agent":"Mozilla/5.0"})
html = BeautifulSoup(raw.text, 'html.parser')

# 컨테이너 dl.lst_dsc
movies = html.select("dl.lst_dsc")

for m in movies:
    # 제목 dt.tit > a
    title = m.select_one("dt.tit > a").text
    # 평점 div.star_t1 a span.num
    score = m.select_one("div.star_t1 a span.num").text
    # 장르 dl.lst_dsc dl.info_txt1 dd a
    # 감독 dl.lst_dsc dl.info_txt1 dd a
    # 배우 dl.lst_dsc dl.info_txt1 dd a
    # 선택자를 사용하는 방법
    # 장르
    genre = m.select("dl.lst_dsc dl.info_txt1 dd:nth-of-type(1) a")
    # 감독
    director = m.select("dl.lst_dsc dl.info_txt1 dd:nth-of-type(2) a")
    # 배우
    actor = m.select("dl.lst_dsc dl.info_txt1 dd:nth-of-type(2) a")

    if float(score) < 8.5:
        continue

    genre_all = m.select_one("dl.lst_dsc dl.info_txt1 dd:nth-of-type(1) span.link_txt")
    if "액션" not in genre_all.text:
        continue
    print("제목 : ",title)
    print("-"*50)
    print("평점 : ",score)
    print("-"*50)
    for g in genre:
        print("장르 : ",g.text)
        print("-" * 50)
    for d in director:
        print("감독 : ",d.text)
        print("-" * 50)
    for a in actor:
        print("배우 : ",a.text)

    print("*"*50)

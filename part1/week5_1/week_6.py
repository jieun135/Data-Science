# 이미지 데이터 수집

import requests
from bs4 import BeautifulSoup
from urllib.request import urlretrieve

raw = requests.get("https://movie.naver.com/movie/running/current.nhn#",
                   headers = {"User-Agent":"Mozilla/5.0"})
html = BeautifulSoup(raw.text, 'html.parser')

# 컨테이너 dl.lst_dsc
movies = html.select("dl.lst_dsc")

for m in movies:
    # 제목 dt.tit > a
    title = m.select_one("dt.tit > a")
    url = title.attrs["href"]
    print("="*50)
    print("제목 : ", title.text)

    each_raw = requests.get("https://movie.naver.com"+url,
                            headers= {"User-Agent":"Mozilla/5.0"})
    each_html = BeautifulSoup(each_raw.text, 'html.parser')
    # 컨테이너 div.score_result > ul > li
    # 평점 div.star_score em
    # 리뷰 div.score_reple p

    poster = each_html.select_one("div.mv_info_area div.poster img")
    poster_src = poster.attrs["src"]
    # print(poster_src)
    urlretrieve(poster_src,"poster/"+title.text[:2]+".png")
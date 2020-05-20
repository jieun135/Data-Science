# 네이버 영화 데이터 수집 리뷰 // 상세 페이지

import requests
from bs4 import BeautifulSoup

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
    print("제목 : "title.text)

    each_raw = requests.get("https://movie.naver.com"+url,
                            headers= {"User-Agent":"Mozilla/5.0"})
    each_html = BeautifulSoup(each_raw.text, 'html.parser')
    # 컨테이너 div.score_result > ul > li
    # 평점 div.star_score em
    # 리뷰 div.score_reple p

    reviews = each_html.select("div.score_result > ul > li")
    for r in reviews:
        stars = r.select_one("div.star_score em").text
        reple = r.select_one("div.score_reple p").text

        print(stars, reple)
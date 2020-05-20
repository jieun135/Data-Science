# 이미지 데이터 수집

import requests
from bs4 import BeautifulSoup
from urllib.request import urlretrieve

raw = requests.get("http://ticket2.movie.daum.net/Movie/MovieRankList.aspx",
                   headers = {"User-Agent":"Mozilla/5.0"})
html = BeautifulSoup(raw.text, 'html.parser')

# 컨테이너 div.movie_join li
movies = html.select("ul.list_boxthumb > li")

for m in movies:
    # 제목 strong.tit_join
    title = m.select_one("strong.tit_join > a")

    # 상세 페이지로 들어가기
    url = title.attrs["href"]
    raw_each = requests.get(url, headers={"User-Agent": "Mozilla/5.0"})
    html_each = BeautifulSoup(raw_each.text, 'html.parser')

    try:
        # 제목 strong.tit_movie
        title = html_each.select_one("strong.tit_movie").text
        # 평점 em.emph_grade
        score = html_each.select_one("em.emph_grade").text
        # 장르 dl.list_movie > dd:nth-of-type(1)
        genre = html_each.select_one("dl.list_movie > dd:nth-of-type(1)").text
        # 감독
        director = html_each.select("dl.list_movie > dd:nth-of-type(5) a")
        # 배우
        actor = html_each.select("dl.list_movie > dd:nth-of-type(6) a")
    except:
        print(title.text.strip(), "상세페이지가 없습니다.")
        print("="*50)
        continue

    # 출력
    print("=" * 50)
    print("제목 : ", title.strip())
    print("=" * 50)
    print("평점 :", score.strip())
    print("="*50)
    print("장르 : ", genre.strip())
    print("감독 :")
    for d in director:
        print(d.text)
    print("배우 :")
    for a in actor:
        print(a.text)
    print("="*50)
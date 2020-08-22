import requests
from bs4 import BeautifulSoup

# IMDb 홈페이지에 데이터 요청하기
raw = requests.get("https://www.imdb.com/movies-in-theaters/?ref_=nv_mv_inth",
                   headers={"User-Agent": "Mozilla/5.0"})
html = BeautifulSoup(raw.text, 'html.parser')

# 컨테이너 수집하기
movies = html.select("td.overview-top ")

# 컨테이너를 반복하며 상세데이터(제목, 감독, 배우) 수집하기
for m in movies:
    title = m.select_one("h4 > a").text

    # 감독, 배우는 여러명일 수 있으므로 select를 활용해서 리스트로 저장합니다.
    # 원하는 데이터가 컨테이너의 자식관계에 있을 때는 자식 선택자(>)를 먼저 써줄 수도 있습니다.
    director = m.select("> div:nth-of-type(3) a")
    actor = m.select("> div:nth-of-type(4) a")

    print("제목:", title)
    # print(score)

    print("감독:")
    for d in director:
        print(d.text)

    print("배우:")
    for a in actor:
        print(a.text)

    print("=" * 50)
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

    # 감독과 배우가 모두 div.txt-block으로 선택되는 태그에 저장되어 있으므로
    # 리스트를 저장하여 첫번째: 감독/ 두번째: 배우를 구분합니다.
    info = m.select("div.txt-block")
    director = info[0].select("a")
    actor = info[1].select("a")

    print("제목:", title)
    # print(score)

    print("감독:")
    for d in director:
        print(d.text)

    print("배우:")
    for a in actor:
        print(a.text)

    print("=" * 50)
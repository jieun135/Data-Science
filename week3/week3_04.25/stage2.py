import requests
from bs4 import BeautifulSoup

# requests.get("긁고 싶은 url")
row = requests.get("https://tv.naver.com/r/")

# 써놓은 주소의 소스코드print(row.text)
# print(row.text)

# BeautifulSoup(소스코드, 파싱 종류)
html = BeautifulSoup(row.text,'html.parser')

# 컨테이너 : div.inner
# 제목 : dt.title
# 채널명 : dd.chn
# 재생수 : span.hit
# 좋아요 : span.like

#html.select('선택자')
# div.inner와 관련된 코드만 나온다.
clips = html.select('div.inner')
print(len(clips))

# 제목 클립 안에 제목은 하나니까 select_one 사용 text는 글자만 나오게 한다.
for rank in range(3): # for rank in [0,1,2]:
    title = clips[rank].select_one('dt.title').text
    chn = clips[rank].select_one('dd.chn').text
    hit = clips[rank].select_one('span.hit').text
    like = clips[rank].select_one('span.like').text
    print(title, chn, hit, like)

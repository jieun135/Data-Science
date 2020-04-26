import requests
from bs4 import BeautifulSoup

row = requests.get("https://tv.naver.com/r/")
html = BeautifulSoup(row.text,'html.parser')

clips = html.select('div.cds')
print(len(clips))

# 컨테이너 : div.cds
# 제목 : dt.title
# 채널명: dd.chn
# 재생수: span.hit
# 좋아요수: span.like
for rank in range(4,101): # for rank in [0,1,2]:
    title = clips[rank].select_one('dt.title').text.strip()
    chn = clips[rank].select_one('dd.chn').text
    hit = clips[rank].select_one('span.hit').text
    like = clips[rank].select_one('span.like').text
    print(title, chn, hit, like)
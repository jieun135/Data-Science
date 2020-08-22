import requests
from bs4 import BeautifulSoup
#csv 형식으로 저장하기
f = open("navertv.csv","w", encoding='UTF-8')
f.write("제목, 채널명, 재생수, 좋아요\n")

raw = requests.get("https://tv.naver.com/r/")
# print(row.text)

html = BeautifulSoup(raw.text,'html.parser')

clips = html.select('div.inner')

for rank in range(3): # for rank in [0,1,2]:
    title = clips[rank].select_one('dt.title').text.strip()
    chn = clips[rank].select_one('dd.chn').text.strip()
    hit = clips[rank].select_one('span.hit').text.strip()
    like = clips[rank].select_one('span.like').text.strip()

    title = title.replace(",","")
    chn = chn.replace(",","")
    hit = hit.replace(",","")
    like = like.replace(",","")

    hit = hit.replace("재생 수","")
    like = like[5:]
    # print(title)
    # print(chn)
    # print(hit)
    # print(like)
    # print("="*50)
    f.write(title + "," + chn + "," + hit + "," + like + "\n")

f.close()
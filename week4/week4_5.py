import requests
from bs4 import BeautifulSoup
import openpyxl

wb = openpyxl.Workbook()
sheet = wb.active
sheet.append(['제목','채널명','재생수','좋아요수'])

raw = requests.get("https://tv.naver.com/r/")
html = BeautifulSoup(raw.text,'html.parser')
clips = html.select('div.inner')

for rank in range(3): # for rank in [0,1,2]:
    title = clips[rank].select_one('dt.title').text.strip()
    chn = clips[rank].select_one('dd.chn').text.strip()
    hit = clips[rank].select_one('span.hit').text.strip()
    like = clips[rank].select_one('span.like').text.strip()

    hit = hit.replace("재생 수","")
    like = like[5:]

    sheet.append([title,chn, hit, like])
    # print(title)
    # print(chn)
    # print(hit)
    # print(like)
    # print("="*50)
wb.save("navertv.xlsx")
import requests
from bs4 import BeautifulSoup
import openpyxl

wb = openpyxl.Workbook() # 새로운 파일 생성
sheet = wb.active
sheet.append(['기사제목','기사요약'])

for n in range(1, 4):
    raw = requests.get("https://search.daum.net/search?w=news&q=코알라&p="+str(n))
    html = BeautifulSoup(raw.text, 'html.parser')

    articles = html.select("div.wrap_cont")

    for ar in articles:
        title = ar.select_one("a.f_link_b").text
        summary = ar.select_one("p.f_eb.desc").text

        # print(title)
        # print(summary)
        # # 기사별로 구분을 위해 구분선 삽입
        # print("="*50)
        print(title, summary)
        sheet.append([title, summary])
wb.save("hw2.xlsx")
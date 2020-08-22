import requests
from bs4 import BeautifulSoup

f = open('hw1_2.csv','w',encoding = 'utf-8-sig')

for p in range(1, 6):
    raw = requests.get("https://series.naver.com/ebook/top100List.nhn?page="+str(p),
                       headers={"User-Agent":"Mozilla/5.0"})
    html = BeautifulSoup(raw.text, 'html.parser')

    books = html.select("div.lst_thum_wrap li")
    for b in books:
        title = b.select_one("a strong").text
        author = b.select_one("span.writer").text
        title = title.replace(',','')
        author = author.replace(',','')
        f.write(title+','+author+'\n')
        #print(title, author)

f.close()
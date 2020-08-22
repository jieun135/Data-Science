import requests
from bs4 import BeautifulSoup

f = open('hw2_2.csv','w',encoding = 'utf-8-sig')

for n in range(1, 4):
    raw = requests.get("https://search.daum.net/search?w=news&q=코알라&p="+str(n))
    html = BeautifulSoup(raw.text, 'html.parser')

    articles = html.select("div.wrap_cont")

    for ar in articles:
        title = ar.select_one("a.f_link_b").text
        summary = ar.select_one("p.f_eb.desc").text
        title = title.replace(',','')
        summary = summary.replace(',','')
        f.write(title+','+summary+'\n'+'\n')

f.close()
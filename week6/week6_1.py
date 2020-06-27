import requests
from bs4 import BeautifulSoup

raw = requests.get("https://m.map.naver.com",
                   headers = {'User-Agent':"Mozilla/5.0"})
html = BeautifulSoup(raw.text, 'html.parser')

# 컨테이너 dl.lsnx_det
stores = html.select("dl.lsnx_det")
print(stores)
# 가게 이름
# 가게 주소
# 전화번호
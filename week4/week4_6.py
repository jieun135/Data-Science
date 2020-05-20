import requests
from bs4 import BeautifulSoup
import openpyxl

keyword = input("검색어 입력: ")

try: # 한 번 시도해볼게
    wb = openpyxl.load_workbook("navernews.xlsx") # 기존 파일 밑에 또 다시 저장 됨. (다른 검색어 입력했을 시
    sheet = wb.active
    print("불러오기 완료")
except: #try가 안되면 시도할게
    wb = openpyxl.Workbook() 새로운 파일 생성
    sheet = wb.active
    sheet.append(['제목','언론사'])
    print("새로 파일을 만들었습니다.")

for page in range(1,52, 10): # for page in range(1,52, 10) [1, 11, 21,31,41,51]
    # page로 숫자로 지정할 수 있다.
    url = "https://search.naver.com/search.naver?where=news&query="+keyword+"&start="+ str(page)
    row = requests.get(url, headers={'User-Agent':'Mozilla/5.0'})
    html = BeautifulSoup(row.text,'html.parser')

    # 컨테이너 : ul.type01>li
    # 제목 : a._sp_each_title
    # 신문사 : span._sp_each_source

    articles = html.select('ul.type01>li')
    for news in articles:
        title = news.select_one('a._sp_each_title').text.strip()
        journal = news.select_one('span._sp_each_source').text.strip()
        print(title, journal)
        sheet.append([title, journal])
    print("="*50)

wb.save("navernews.xlsx")

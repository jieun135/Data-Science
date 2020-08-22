
import time  # 지연시간
import requests
from bs4 import BeautifulSoup
from urllib.request import urlretrieve
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

import openpyxl

wb = openpyxl.Workbook()
sheet = wb.active
sheet.append(['도서명', '부제목', '출간일', '분야', '정가',  '평점', '쪽수', '이북 여부', '제목 길이','순위','베스트셀러 여부'])


# 2020년 6월
# 2020년 6월 첫번째 페이지만 GET 방식이니까 따로 먼저 돌려주기
first_url ="http://www.kyobobook.co.kr/bestSellerNew/bestseller.laf?range=1&kind=2&orderClick=DAB&mallGb=KOR&linkClass=A"
raw = requests.get(first_url, headers={"User-Agent":"Mozilla/5.0"})
html = BeautifulSoup(raw.text, 'html.parser')

container = html.select("div.detail")
num = 0
for c in container:
    title = c.select_one("div.detail div.title a")
    title_af = str(title.text.strip())
    title_len = 0
    for t in title_af:
        if t == '(':
            break
        title_len += 1
    addexplain = c.select_one("div.subtitle").text.strip()
    rank = c.select_one("div.review em").text.strip()
    if(c.select_one(".detail .price a span")):
        eBook = 1
    else:
        eBook = 0
    url = title.attrs["href"]

    each_raw = requests.get(url, headers={"User-Agent": "Mozilla/5.0"})
    each_html = BeautifulSoup(each_raw.text, 'html.parser')

    bf_page = each_html.select("table.table_simple2 td")
    page = bf_page[1].text.rstrip('쪽')

    date = each_html.select_one("div.author span.date").text.strip()
    year = date[0:4]
    month = date[6:8]
    day = date[10:12]
    date = year + month + day

    price = str(each_html.select_one(".box_detail_price .org_price").text.strip())
    price = price.rstrip('원')
    price = price.replace(",", "")

    num += 1
    bf_category = each_html.select("ul.list_detail_category a:nth-of-type(1)")
    try:
        category = bf_category[0].text.strip()
    except:
        category = ""
    print("제목:", title_af)
    print("제목 길이:", title_len)
    print("순위:",num)
    print("정가:",price)
    print("출간일:", date)
    print('분야:', category)
    print("부제목:",addexplain)
    print("평점:",rank)
    print("쪽수:",page)
    print("ebook여부:",eBook)
    print("=" * 50)

    sheet.append([title_af,addexplain,date, category, price, rank, page, eBook, title_len, num, 1])


# 두번째 페이지부터 POST 방식으로 크롤링하기
# 리스트 url
result_url = "http://www.kyobobook.co.kr/bestSellerNew/bestseller.laf"
# 특징
lines = '''targetPage: 2
mallGb: KOR
range: 1
kind: 2
kyoboTotalYn: N
selBestYmw: 2020060
linkClass: A
cateDivYn: 
pageNumber: 1
perPage: 20
excelYn: N
seeOverYn: Y
loginYN: N
barcode: 9791190382175
ejkGb: KOR
notAge: 0 
cartType: addMast
qty: 1
barcode: 9791130629636
ejkGb: KOR
notAge: 0 
cartType: addMast
qty: 1
barcode: 9791188331796
ejkGb: KOR
notAge: 0 
cartType: addMast
qty: 1
barcode: 9788932920337
ejkGb: KOR
notAge: 0 
cartType: addMast
qty: 1
barcode: 9791190786355
ejkGb: KOR
notAge: 0 
cartType: addMast
qty: 1
barcode: 9791158740757
ejkGb: KOR
notAge: 0 
cartType: addMast
qty: 1
barcode: 9791196831059
ejkGb: KOR
notAge: 0 
cartType: addMast
qty: 1
barcode: 9788965963790
ejkGb: KOR
notAge: 0 
cartType: addMast
qty: 1
barcode: 9788954671156
ejkGb: KOR
notAge: 0 
cartType: addMast
qty: 1
barcode: 9791130627878
ejkGb: KOR
notAge: 0 
cartType: addMast
qty: 1
barcode: 9788936434267
ejkGb: KOR
notAge: 0 
cartType: addMast
qty: 1
barcode: 9791190299060
ejkGb: KOR
notAge: 0 
cartType: addMast
qty: 1
barcode: 9788954672214
ejkGb: KOR
notAge: 0 
cartType: addMast
qty: 1
barcode: 9791190456098
ejkGb: KOR
notAge: 0 
cartType: addMast
qty: 1
barcode: 9791197016806
ejkGb: KOR
notAge: 0 
cartType: addMast
qty: 1
barcode: 9791187481720
ejkGb: KOR
notAge: 0 
cartType: addMast
qty: 1
barcode: 9788993178692
ejkGb: KOR
notAge: 0 
cartType: addMast
qty: 1
barcode: 9791197021602
ejkGb: KOR
notAge: 0 
cartType: addMast
qty: 1
barcode: 9791165210144
ejkGb: KOR
notAge: 0 
cartType: addMast
qty: 1
barcode: 9791187119845
ejkGb: KOR
notAge: 0 
cartType: addMast
qty: 1
'''.splitlines()

# 빈칸 제거하고 새로 만든 리스트에 key 와 value 값 넣기
lines_change = []
for line in lines:
    line = line.replace(' ', '')
    lines_change.append(line)

data = {}
for line in lines_change:
    key, value = line.split(':', 1)
    data[key] = value

# post 방식으로 조사
response = requests.post(result_url, data=data)
html = response.text
soup = BeautifulSoup(html, 'html.parser')

# 전체 크롤링

for n in range(2, 11):
    time.sleep(1)

    response = requests.post(result_url, data=data)
    html = response.text
    soup = BeautifulSoup(html, 'html.parser')

    container = soup.select("div.detail")
    for c in container:
        title = c.select_one("div.detail div.title a")
        title_af = str(title.text.strip())
        title_len = 0
        for t in title_af:
            if t == '(':
                break
            title_len += 1
        addexplain = c.select_one("div.subtitle").text.strip()
        rank = c.select_one("div.review em").text.strip()
        if (c.select_one(".detail .price a span")):
            eBook = 1
        else:
            eBook = 0
        url = title.attrs["href"]

        each_raw = requests.get(url, headers={"User-Agent": "Mozilla/5.0"})
        each_html = BeautifulSoup(each_raw.text, 'html.parser')

        bf_page = each_html.select("table.table_simple2 td")
        page = bf_page[1].text.rstrip('쪽')

        date = each_html.select_one("div.author span.date").text.strip()
        year = date[0:4]
        month = date[6:8]
        day = date[10:12]
        date = year + month + day

        price = str(each_html.select_one(".box_detail_price .org_price").text.strip())
        price = price.rstrip('원')
        price = price.replace(",", "")

        num += 1
        bf_category = each_html.select("ul.list_detail_category a:nth-of-type(1)")
        try:
            category = bf_category[0].text.strip()
        except:
            category = ""

        print("제목:", title_af)
        print("제목 길이:", title_len)
        print("순위:", num)
        print("정가:", price)
        print("출간일:", date)
        print('분야:', category)
        print("부제목:", addexplain)
        print("평점:", rank)
        print("쪽수:", page)
        print("ebook여부:", eBook)
        print("=" * 50)

        sheet.append([title_af, addexplain, date, category, price, rank, page, eBook, title_len, num, 1])

    data['targetPage'] = n + 1
    data['kind'] = 2
    data['pageNumber'] = n
wb.save('crawling_best_2020060.xlsx')
# 2017/4 ~ 2020/5

# 날짜 리스트 만들기
# 완료 2017040, 2017050, 2017060, 2017070,
bestYmd = [2017080, 2017090, 2017100, 2017110, 2017120,
           2018010, 2018020, 2018030, 2018040, 2018050, 2018060, 2018070, 2018080, 2018090, 2018100, 2018110, 2018120,
           2019010, 2019020, 2019030, 2019040, 2019050, 2019060, 2019070, 2019080, 2019090, 2019100, 2019110, 2019120,
           2020010, 2020020, 2020030, 2020040, 2020050]

for ymd in bestYmd:
    num2 = 0
    wb = openpyxl.Workbook()
    sheet = wb.active
    sheet.append(['도서명', '부제목', '출간일', '분야', '정가', '평점', '쪽수', 'eBook 여부', '제목 길이','순위','베스트셀러 여부'])

    data['selBestYmw'] = ymd
    data['targetPage'] = 0
    data['kind'] = 2
    
    for n in range(1, 11):
        time.sleep(1)

        response = requests.post(result_url, data=data)
        html = response.text
        soup = BeautifulSoup(html, 'html.parser')

        container = soup.select("div.detail")
        for c in container:
            title = c.select_one("div.detail div.title a")
            title_af = str(title.text.strip())
            title_len = 0
            for t in title_af:
                if t == '(':
                    break
                title_len += 1
            addexplain = c.select_one("div.subtitle").text.strip()
            #rank_bf = c.select_one("div.review em").text.strip()
            try:
                rank = c.select_one("div.review em").text.strip()
            except:
                rank = ""
            # try:
            #     rank = rank_bf[0].text.strip()
            # except:
            #     rank = ""

            if (c.select_one(".detail .price a span")):
                eBook = 1
            else:
                eBook = 0
            url = title.attrs["href"]

            each_raw = requests.get(url, headers={"User-Agent": "Mozilla/5.0"})
            each_html = BeautifulSoup(each_raw.text, 'html.parser')

            try:
                date_bf = each_html.select_one("div.author span.date").text.strip()
                year = date_bf[0:4]
                month = date_bf[6:8]
                day = date_bf[10:12]
                date_bf = year + month + day
            except:
                date_bf = ''
            try:
                price = str(each_html.select_one(".box_detail_price .org_price").text.strip())
                price = price.rstrip('원')
                price = price.replace(",", "")
            except:
                price = ''

            bf_page = each_html.select("table.table_simple2 td")
            try:
                page = bf_page[1].text.rstrip('쪽')
            except:
                page = str(0)

            num2 += 1
            bf_category = each_html.select("ul.list_detail_category a:nth-of-type(1)")
            try:
                category = bf_category[0].text.strip()
            except:
                category = ""

            print("제목:", title_af)
            print("제목 길이:", title_len)
            print("순위:", num2)
            print("정가:", price)
            print("출간일:", date_bf)
            print('분야:', category)
            print("부제목:", addexplain)
            print("평점:", rank)
            print("쪽수:", page)
            print("ebook여부:", eBook)
            print("=" * 50)

            sheet.append([title_af, addexplain, date_bf, category, price, rank, page, eBook, title_len, num2, 1])

        # 페이지 넘어가기
        data['targetPage'] = n + 1
        data['kind'] = 2
    wb.save('crawling_best_'+str(ymd)+'.xlsx')
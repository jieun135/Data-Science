from selenium import webdriver
import time

# 크롬창(웹드라이버) 열기
driver = webdriver.Chrome("./chromedriver.exe")

# 구글 지도 접속하기
driver.get("https://www.google.com/maps/")

# 검색창에 "카페" 입력하기
searchbox = driver.find_element_by_css_selector("input#searchboxinput")
searchbox.send_keys("카페")

# 검색버튼 누르기
searchbutton = driver.find_element_by_css_selector("button#searchbox-searchbutton")
searchbutton.click()
#5. 검색 결과 확인하기
# time.sleep(1)

# # 컨테이너 dl.lsnx_det
#     # stores = html.select("dl.lsnx_det")
#     stores = driver.find_elements_by_css_selector("dl.lsnx_det")
#
#     for s in stores:
#         name = s.find_element_by_css_selector("dt > a").text
#         addr = s.find_element_by_css_selector("dd.addr").text
#
#         try:
#             tel = s.find_element_by_css_selector("dd.tel").text
#         except:
#             tel = "전화번호 없음"
#         # 가게 이름 dt > a
#         # 가게 주소 dd.addr
#         # 전화번호 dd.tel
#
#         print(name)
#         print(addr)
#         print(tel)
#
#     # 페이지버튼 div.paginate > *
#     page_bar = driver.find_elements_by_css_selector("div.paginate > *")
#
#     try:
#         if n%5 != 0:
#             page_bar[n%5+1].click()
#         else:
#             page_bar[6].click()
#     except:
#         print("수집완료")
#         break
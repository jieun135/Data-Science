# 셀레니옴 연습하기

from selenium import webdriver
import time

#1.웹드라이버 켜기
driver = webdriver.Chrome("./chromedriver.exe")
#2. 파파고 접속하기
driver.get("https://papago.naver.com")
# 지연 시간 주기
time.sleep(0.5)
#3. 검색창에 검색어 입력하기 // 검색창 : textarea#txtSource
search_box = driver.find_element_by_css_selector("textarea#txtSource")
search_box.send_keys("seize the day") # 텍스트 입력 공간에 키워드 전송
#4. 검색버튼 누르기 // 번역 버튼 : button#btntranslate
button = driver.find_element_by_css_selector("button#btnTranslate")
button.click()
#5. 검색 결과 확인하기
# 지연 시간 주기
time.sleep(0.5)
result = driver.find_element_by_css_selector("div#txtTarget").text
print(result)

from selenium import webdriver
import time
# 크롬창(웹드라이버) 열기
driver = webdriver.Chrome("./chromedriver")
# ootd 태그 검색결과 페이지 접속
driver.get("https://www.instagram.com/explore/tags/ootd/")
log = driver.find_element_by_css_selector("button.sqdOP")
log.click()
time.sleep(1)
box = driver.find_elements_by_css_selector("input._2hvTZ")
box[0].send_keys("ijieun403")
box[1].send_keys("jieunlee308^^")
login = driver.find_element_by_css_selector("button.sqdOP.L3NKy")
login.click()
# 컨테이너(포스트) 12개 저장
instagram = driver.find_elements_by_css_selector("div.v1Nh3")
instagram = instagram[:12]
# 컨테이너 반복하기
for insta in instagram:
    # 포스트 클릭하기
    insta.click()
    
    # 시간 지연
    time.sleep(1)
    
    # 본문 선택 후 출력
    post = driver.find_element_by_css_selector("div.C4VMK span").text
    print(post)
    # 닫기 버튼 클릭
    but_close = driver.find_element_by_css_selector("button.ckWGn")
    but_close.click()
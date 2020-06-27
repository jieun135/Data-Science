from selenium import webdriver
import time

#1. 웹드라이버 켜기
driver = webdriver.Chrome("./chromedriver")
#2. 인스타 접속하기
driver.get("https://www.instagram.com/explore/tags/ootd/")
#2_1. 인스타 로그인
# 로그인 버튼 : button.sqdOP // 아이디 : input._2hvTZ
log = driver.find_element_by_css_selector("button.sqdOP")
log.click()
time.sleep(1)
box = driver.find_elements_by_css_selector("input._2hvTZ")
box[0].send_keys("aaaa")
box[1].send_keys("aaaaa")
login = driver.find_element_by_css_selector("button.sqdOP.L3NKy")
login.click()

# #3. 게시글로 들어가기 div.v1Nh3 // div.Nnq7C >div >a
time.sleep(3)
post = driver.find_elements_by_css_selector("div.Nnq7C >div >a")
post = post[:12]

for i in post: # 본문 내용 : div.C4VMK span
    time.sleep(1)
    i.click()
    time.sleep(1)

    txt = driver.find_element_by_css_selector("div.C4VMK span").text
    print(txt)
    print("=" * 50)

    time.sleep(1)
    close_btn = driver.find_element_by_css_selector("div.Igw0E button.wpO6b")
    close_btn.click()
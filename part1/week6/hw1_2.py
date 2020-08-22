from selenium import webdriver
import time

#1. 웹드라이버 켜기
driver = webdriver.Chrome("./chromedriver")
#2. 페이스북 로그인 접속하기
driver.get("https://www.facebook.com")

#3. 로그인 아이디/비밀번호 입력하기 // 아이디: input#email // 비밀번호 : input#pass
log_id = driver.find_element_by_css_selector("input#email")
log_id.send_keys("aaaa")
log_pw = driver.find_element_by_css_selector("input#pass")
log_pw.send_keys("aaaa")
#4. 로그인 버튼 누르기 // 로그인 버튼: input#u_0_e
login = driver.find_element_by_css_selector("input#u_0_e")
login.click()
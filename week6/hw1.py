from selenium import webdriver
import time

#1. 웹드라이버 켜기
driver = webdriver.Chrome("./chromedriver")
#2. 네이버 로그인 접속하기
driver.get("https://nid.naver.com")

#3. 로그인 아이디/비밀번호 입력하기 // 아이디: input#id // 비밀번호 : input#pw
log_id = driver.find_element_by_css_selector("input#id")
log_id.send_keys("aaaa")
log_pw = driver.find_element_by_css_selector("input#pw")
log_pw.send_keys("aaaaa")
#4. 로그인 버튼 누르기 // 로그인 버튼: input.btn_global
log_button = driver.find_element_by_css_selector("input.btn_global")
log_button.click()
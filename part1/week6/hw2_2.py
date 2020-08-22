from selenium import webdriver
import time

instagram_id = input("인스타그램 아이디를 입력하세요: ")
instagram_pw = input("인스타그램 비밀번호를 입력하세요: ")

driver = webdriver.Chrome("./chromedriver")
driver.get("https://www.instagram.com/explore/tags/ootd/")

#로그인 버튼: button.L3NKy
log_button = driver.find_element_by_css_selector("button.L3NKy")
log_button.click()
time.sleep(1)

#아이디 입력하기
input_id  = driver.find_elements_by_css_selector("label.f0n8F input:nth-of-type(1)")[0]
input_id.send_keys(instagram_id)

#비번 입력
input_pw  = driver.find_elements_by_css_selector("label.f0n8F input:nth-of-type(1)")[1]
input_pw.send_keys(instagram_pw)

#로그인하기: input.btn_global
log_button2 = driver.find_element_by_css_selector("button.L3NKy")
log_button2.click()
time.sleep(3)

#컨테이너: div.v1Nh3
cont = driver.find_elements_by_css_selector("div.Nnq7C >div >a")
cont = cont[:12]
time.sleep(1)

#메인텍스트: div.C4VMK span
for c in cont:
    c.click()
    time.sleep(1)

    text = driver.find_element_by_css_selector("div.C4VMK span").text
    print(text)
    print("="*50)

    time.sleep(1)
    close_btn = driver.find_element_by_css_selector("div.Igw0E button.wpO6b")
    close_btn.click()

# div.v1Nh3
# pip isntall Selenium
from selenium import webdriver
import time

chrome_driver_path = "C:\python2_visualcode\chromedriver.exe"
url = "https://www.naver.com/"
driver = webdriver.Chrome(chrome_driver_path)
driver.get(url)

# 로그인 버튼 클릭
driver.find_element_by_xpath('//*[@id="account"]/a').click() #xPath
# driver.find_element_by_css_selector('#account > a').click() #Selector
time.sleep(1)

# id,pw 입력
id = "lhj1234"
driver.find_element_by_xpath('//*[@id="id"]').send_keys(id)
pw = "abcdef"
driver.find_element_by_xpath('//*[@id="pw"]').send_keys(pw)

# popup - time 함수 많이 사용함
# driver.switch_to.window(driver.window_handles[-1]) # 최신 팝업창으로 이동
# driver.switch_to.window(driver.window_handles[0]) # 원래 창으로 복귀

# 입력창에 있는 텍스트 지우기
time.sleep(1)
driver.find_element_by_xpath('//*[@id="pw"]').clear()

time.sleep(5)
driver.close()
import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()
driver.get("http://www.baidu.com")
driver.implicitly_wait(10)

driver.find_element_by_id("kw").send_keys('selenium')
driver.find_element_by_id("su").click()
driver.find_element_by_link_text("Selenium_百度百科").click()

# jsStr = "return document.title"
# script = driver.execute_script(jsStr)
# print(script)
element = driver.find_element(By.ID, "kw")
jsStr = "arguments[0].setAttribute('style',arguments[1]);"
driver.execute_script(jsStr,element,"color:orange;border:4px solid orange;")

time.sleep(3)
driver.quit()
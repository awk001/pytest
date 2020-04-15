from time import sleep

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

d = webdriver.Firefox()
d.get("http://www.baidu.com")
d.implicitly_wait(10)
d.maximize_window()
element = d.find_element(By.ID, "kw")
action = ActionChains(d)
# action.send_keys("selenium")
# action.send_keys_to_element(d.find_element(By.ID,"kw"),"selenium",Keys.ENTER)
# 按下shift键输入的字母为大写
action.key_down(Keys.SHIFT).send_keys("abc").key_up(Keys.SHIFT).send_keys("abc")  # ABCabc
action.perform()
sleep(3)

d.quit()
import time

from selenium import webdriver

driver = webdriver.Firefox()
# driver.get("http://localhost:63342/PyCode/base/demo/report/file.html?_ijt=mnbcl0uuh9np4hj9n0crd2b7tt")
driver.get("https://www.juhe.cn/login")
driver.implicitly_wait(30)
# driver.find_element_by_id("file").send_keys("‪C:/Users/laptop-awk/Desktop/居居.docx")
driver.delete_all_cookies()

# action = ActionChains(driver)
# action.send_keys_to_element(driver.find_element_by_id("username"),"awk123456",Keys.TAB)
# action.send_keys_to_element(driver.find_element_by_id("password"),"awk9701103419",Keys.ENTER)
# action.perform()

# time.sleep(2)
# for cookie in driver.get_cookies():
#     print(cookie)
cookie = {'name': 'aliyungf_tc', 'value': 'AQAAAOw1IyhxkwwAakmGcVtHTHUO6gDJ', 'path': '/', 'domain': 'www.juhe.cn', 'secure': False, 'httpOnly': True}
driver.add_cookie(cookie)
cookie = {'name': 'acw_tc', 'value': '76b20fef15869334598367854e14924dfa4146b5b2713dba96a901e09c416d', 'path': '/', 'domain': 'www.juhe.cn', 'secure': False, 'httpOnly': True, 'expiry': 1589611862}
driver.add_cookie(cookie)
cookie = {'name': 'PHPSESSID', 'value': '74benbkqg917n8jgirtvrs9o83', 'path': '/', 'domain': '.juhe.cn', 'secure': False, 'httpOnly': False, 'expiry': 1586937061}
driver.add_cookie(cookie)
cookie = {'name': 'hasReg', 'value': 'reged', 'path': '/', 'domain': 'www.juhe.cn', 'secure': False, 'httpOnly': False, 'expiry': 1588229461}
driver.add_cookie(cookie)
cookie = {'name': 'jh-dtaf4a8u96q0iiqsba9g8a', 'value': '0', 'path': '/', 'domain': '.juhe.cn', 'secure': False, 'httpOnly': False, 'expiry': 1586937062}
driver.add_cookie(cookie)
cookie = {'name': 'XSRF-TOKEN', 'value': 'eyJpdiI6IitxSk1aSnRJVEdyWWFJd2JiY0d3bUE9PSIsInZhbHVlIjoidXVWbldOZGhtWGtMRXc5VXFZdXQ3NUF5MWRmRTVrdmNlQ1NNNVBCV2E2T0lGbkx2ZXFkUXA2Um92SlF1cElUXC9vQlkra0VtTjFUMkMrcnkydTVsc2xBPT0iLCJtYWMiOiI0MWU0MmQ1MTQzN2QyOTJmOTRlYTk0MmMyZmEyODM2MjFhM2JlNDI0ZTcyZWIzMjZiOWU0NWM5ZTJiYjBlZGY3In0%3D', 'path': '/', 'domain': '.juhe.cn', 'secure': False, 'httpOnly': False, 'expiry': 1586940662}
driver.add_cookie(cookie)
cookie = {'name': 'juhe_cn_session', 'value': 'eyJpdiI6ImZ5SGVYdDFBZk40QnFDZkx6bjR3NUE9PSIsInZhbHVlIjoiN3g0NlwvUGs2YTcxVVJoUUh3bEw2akhJQW13WWVNRlhBWFJSWUwyT2RKMjVkSE9tTElpUlR4emJMbXRpb2ZQWHZcL3hxVkloMXNQbFRCM3BFNDE5cnlBdz09IiwibWFjIjoiMzRlZmJiOTZmYzA4MmE1YWNmNDYyNjU0NmI2MzE2NzIzMTFkYzhlZjQyOWZhZDYyY2E0MWNmY2NiZGY1NDkxMCJ9', 'path': '/', 'domain': '.juhe.cn', 'secure': False, 'httpOnly': True, 'expiry': 1586940662}
driver.add_cookie(cookie)
time.sleep(3)
driver.get("https://www.juhe.cn/ucenter/account")




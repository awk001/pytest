from selenium import webdriver

driver = webdriver.Firefox()
driver.get("http://www.baidu.com")
driver.implicitly_wait(20)

driver.find_element_by_id("kw").send_keys('selenium')
driver.find_element_by_id("su").click()
# 显示页面大小
driver.set_window_size(600,600)
# 指定位置——上下滚动
# driver.execute_script("window.scrollBy(300,300)")
# time.sleep(2)
# driver.execute_script("window.scrollBy(300,300)")
# # 指定位置——左右滚动
# driver.execute_script("window.scrollTo(300,300)")
# time.sleep(2)
# driver.execute_script("window.scrollTo(300,300)")

# 以某个元素为目标
target = driver.find_element_by_partial_link_text("功能自动化测试工具——Selenium篇")
# 移动元素到页面末端
# driver.execute_script("arguments[0].scrollIntoView(false);",target)
# 移动元素到页面顶端
driver.execute_script("arguments[0].scrollIntoView();",target)
















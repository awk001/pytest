# 1.导包 UnitTest
import requests
import unittest
from time import *

from base.interface.sql import *
from selenium import webdriver


# 2.新建测试类


class TestLogin(unittest.TestCase):

# 3.前置条件
    def setUp(self):
        # 获取session对象
        self.session = requests.session()
        # url
        self.url = "http://localhost/ecshop/upload/index.php"
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get(self.url)
        self.driver.find_element_by_css_selector('img[src="themes/default/images/bnt_log.gif"]').click()
        pass
# 4.释放资源
    def tearDown(self):
        sleep(5)
        # 关闭session
        self.session.close()
        self.driver.quit()
        pass

# 登录成功
    def test_loginSuccess(self):
        # 请求登录
        r = self.session.get(self.url)
        self.driver.find_element_by_css_selector('input[name="username"]').send_keys('ecshop')
        self.driver.find_element_by_css_selector('input[name="password"]').send_keys('ecshop')
        self.driver.find_element_by_xpath('/html/body/div[7]/div[1]/form/table/tbody/tr[4]/td[2]/input[3]').click()

        print('响应状态码：' ,r.status_code)
        print(self.driver.find_element_by_xpath('//*[@id="ECS_MEMBERZONE"]/font/font').text)
        # 断言
        self.assertEqual(self.driver.find_element_by_xpath('//*[@id="ECS_MEMBERZONE"]/font/font').text, "ecshop",'NotEquals' )
        pass

# 登录失败，账号输入错误
    def test_login_errorUsername(self):
        # 请求登录
        r = self.session.get(self.url)
        self.driver.find_element_by_css_selector('input[name="username"]').send_keys('ecshop001')
        self.driver.find_element_by_css_selector('input[name="password"]').send_keys('ecshop')
        # 数据库查询当前用户
        user = connMySQL.data[0][2]
        self.driver.find_element_by_xpath('/html/body/div[7]/div[1]/form/table/tbody/tr[4]/td[2]/input[3]').click()

        print('响应状态码：', r.status_code)
        print(self.driver.find_element_by_xpath('//*[@id="ECS_MEMBERZONE"]/font/font').text)
        # 断言
        self.assertNotEqual(self.driver.find_element_by_xpath(
            self.driver.find_element_by_css_selector('input[name="username"]').text,user,'Equals'))
        pass

# 登录失败，密码错误
    def test_login_errorPwd(self):
        # 请求登录
        r = self.session.get(self.url)
        self.driver.find_element_by_css_selector('input[name="username"]').send_keys('ecshop')
        self.driver.find_element_by_css_selector('input[name="password"]').send_keys('ecshop001')
        # 根据用户名查询密码
        pwd = connMySQL.data[0][3]
        print("ecshop用户密码为：",pwd)
        # 确定登录
        self.driver.find_element_by_xpath('/html/body/div[7]/div[1]/form/table/tbody/tr[4]/td[2]/input[3]').click()

        print('响应状态码：', r.status_code)
        print(self.driver.find_element_by_xpath('//*[@id="ECS_MEMBERZONE"]/font/font').text)
        # 断言
        self.assertEqual(self.driver.find_element_by_xpath('//*[@id="ECS_MEMBERZONE"]/font/font').text, pwd,
                         'NotEquals')
        pass



if __name__ == "__main__":
    unittest.main()





























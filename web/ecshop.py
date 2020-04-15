from selenium import webdriver
from time import *
import unittest, yaml
from ddt import ddt, file_data
import unittest
import yaml
from time import *

from ddt import ddt, file_data
from selenium import webdriver


# 添加配置
# option = webdriver.ChromeOptions
# option.add_argument('disable-infobars')

def readFile():
    # 定义一个list集合
    params = []
    file = open("file.txt", 'r', encoding="UTF-8")
    for line in file.readline():
        params.append(line.strip('\n').split(","))
    return params

# 读取yml文件
file2 = open("testAct3.yml", encoding="UTF-8")
res = yaml.load(file2)
# print(res)

@ddt
class regAction(unittest.TestCase):

    def setUp(self) -> None:


        self.driver = webdriver.Chrome()
        self.driver.get("http://localhost/ecshop/upload/index.php")
        self.driver.maximize_window()

    def tearDown(self) -> None:
        sleep(10)
        self.driver.quit()

    # ************************************************************************************
    # 基本配置
    # def testAct1(self):
    #     pass
    # ************************************************************************************
    # 选择元素进行操作
    # def testAct2(self):
    #     self.driver.find_element_by_css_selector('img[src="themes/default/images/bnt_reg.gif"]').click()
    #     self.driver.find_element_by_id("username").send_keys("awk001")
    #     self.driver.find_element_by_id("email").send_keys("awk001@163.com")
    #     self.driver.find_element_by_id("password1").send_keys("awk001")
    #     self.driver.find_element_by_id("conform_password").send_keys("awk001")
    #     self.driver.find_element_by_css_selector('input[name="extend_field5"]').send_keys("18922228888")
    #     self.driver.find_element_by_css_selector('option[value="old_address"]').click()
    #     self.driver.find_element_by_css_selector('input[name="passwd_answer"]').send_keys("汉中")
    #     self.driver.find_element_by_xpath('/html/body/div[7]/div/form/table/tbody/tr[10]/td[2]/input[3]').click()
    # pass

    # ************************************************************************************
    # 使用data的变量进行赋值
    # @data("awk003","awk004")
    # def testAct2(self,username):
    #     self.driver.find_element_by_css_selector('img[src="themes/default/images/bnt_reg.gif"]').click()
    #     self.driver.find_element_by_id("username").send_keys(username)
    #     self.driver.find_element_by_id("email").send_keys(username+"@163.com")
    #     self.driver.find_element_by_id("password1").send_keys(username)
    #     self.driver.find_element_by_id("conform_password").send_keys(username)
    #     self.driver.find_element_by_css_selector('input[name="extend_field5"]').send_keys("18922228888")
    #     self.driver.find_element_by_css_selector('option[value="old_address"]').click()
    #     self.driver.find_element_by_css_selector('input[name="passwd_answer"]').send_keys("汉中")
    #     self.driver.find_element_by_xpath('/html/body/div[7]/div/form/table/tbody/tr[10]/td[2]/input[3]').click()
    # pass
    # ************************************************************************************
    # 使用yml文件进行赋值
    @file_data('testAct3.yml')
    def testAct3(self, **params):
        self.driver.find_element_by_css_selector('img[src="themes/default/images/bnt_reg.gif"]').click()
        self.driver.find_element_by_id("username").send_keys(params.get('username'))
        self.driver.find_element_by_id("email").send_keys(params.get('username')+"@163.com")
        self.driver.find_element_by_id("password1").send_keys('password')
        self.driver.find_element_by_id("conform_password").send_keys('password')
        self.driver.find_element_by_css_selector('input[name="extend_field5"]').send_keys(params.get('tel'))
        self.driver.find_element_by_css_selector('option[value="old_address"]').click()
        self.driver.find_element_by_css_selector('input[name="passwd_answer"]').send_keys("汉中")
        self.driver.find_element_by_xpath('/html/body/div[7]/div/form/table/tbody/tr[10]/td[2]/input[3]').click()
    pass
    # 测试数据
    # print(params.get('username'))
    # print(params.get('password'))
    # print(params.get('tel'))


if __name__ == "__main__":
    unittest.main()
    # suite = unittest.TestSuite()
    # suite.addTests(unittest.TestLoader().loadTestsFromName('ecshop.regAction.testAct3'))
    # runner = unittest.TestRunner()
    # runner.run(suite)
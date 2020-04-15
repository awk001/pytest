from locust import HttpLocust, TaskSet, task
# from selenium import webdriver
#
# driver = webdriver.Firefox()
# driver.implicitly_wait(20)
class AdminLoadTest(TaskSet):
    """
    创建后台管理站点压测类，需要继承TaskSet
    可以添加多个测试任务
    """
    def login(self):
        """
        登录实例方法
        :return:
        """
        self.client.post("http://localhost/ecshop/upload/admin/index.php",
                         {"username": "admin", "password": "admin123"})

    def logout(self):
        """
        登出实例方法
        :return:
        """
        self.client.get("http://localhost/ecshop/upload/admin/privilege.php?act=logout")

    def on_start(self):
        """
        当任何一个task调度执行之前,
        on_start实例方法会被调用
        先登录
        :return:
        """
        self.login()

    def on_stop(self):
        """
        当任何一个task调度执行之后,
        on_stop实例方法会被调用
        后登出
        :return:
        """
        self.logout()

    @task
    def admin_index(self):
        """
        对后台主页进行压测
        :return:
        """
        self.client.get("http://localhost/ecshop/upload/admin/")


class RunLoadTests(HttpLocust):
    """
    创建运行压测类
    """
    task_set = AdminLoadTest
    min_wait = 2000
    max_wait = 5000
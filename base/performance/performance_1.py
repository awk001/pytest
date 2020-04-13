# 1.导包
from locust import Locust,TaskSet,task

class MyTasks(TaskSet):
    '''
    创建测试任务类，需要继承TaskSet
    可以添加多个测试任务
    '''
    # 每个测试任务，往往会以实例方法的形式来呈现
    # 同时需要使用task装饰器来装饰测试任务
    @task
    def locust_1(self):
        print("你好，我是安文康，来自宝鸡，19年毕业")


class RunnTasks(Locust):
    '''
    创建运行测试类，需要继承Locust父类
    '''
    # 指定测试任务类，使用task_set覆盖父类的类属性
    task_set = MyTasks
    # 指定启动任务间隔的时间范围（单位毫秒）
    min_wait = 2000
    # 使用min_wait、max_wait覆盖父类的类属性
    max_wait = 5000
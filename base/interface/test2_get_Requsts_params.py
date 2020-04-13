'''
    目标：get请求方法演练
    案例：http://www.baidu.com
    请求：
        请求方法：GET
    参数：
        字典或字符串（推荐使用字典）
    响应：
        响应对象.url    获取请求URL
        响应对象.status_code    获取响应状态码
        响应对象.text   以文本形式显示响应内容
'''
# 1.导包
import requests
# 2.请求方式
url = "http://www.baidu.com"
# 定义字典-单个参数
# param = {"id": 1001}
# 多个键值对
# param = {"id": 1001,"name": "zhangsan"}
# 多个参数
# param = {"id": ['1001','1002']} # 不推荐
param = {"id": "1001,1002"}  # %2c ASCII码值为逗号

# requests_get = requests.get(url, params=param)
# 字符串形式编写
requests_get = requests.get(url, params="id=1005")
# 3.获取请求地址
urlAddr = requests_get.url
# 4.获取响应状态码
code = requests_get.status_code
# 5.以文本形式显示响应内容
text = requests_get.text

print(urlAddr)
print(code)
print(text)

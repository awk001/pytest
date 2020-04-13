'''
    目标：get请求方法演练
    案例：http://www.baidu.com
    请求：
        请求方法：GET
    响应：
        响应对象.url    获取请求URL
        响应对象.status_code    获取响应状态码
        响应对象.text   以文本形式显示响应内容
'''
# 1.导包
import requests
# 2.请求方式
requests_get = requests.get("http://www.baidu.com")
# 3.获取请求地址
url = requests_get.url
# 4.获取响应状态码
code = requests_get.status_code
# 5.以文本形式显示响应内容
text = requests_get.text

print(url)
print(code)
print(text)

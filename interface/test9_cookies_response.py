'''
    目标：响应对象常用方法
    1.cookies：
        获取响应cookie信息
    2.content：
        以字节码形式获取响应cookie信息
    案例：http://www.baidu.com

'''
import requests

# url = "http://www.baidu.com"
url_img = "http://www.baidu.com/img/bd_logo1.png?where=super"
requests_get = requests.get(url_img)

# 获取响应cookies
# cookies = requests_get.cookies
#
# content = requests_get.content
# 以文本形式解析图片
text = requests_get.text
# 以字节码形式解析图片
content = requests_get.content
# print(text)
print(content)

with open("./baidu.png","wb") as f:
    f.write(content)

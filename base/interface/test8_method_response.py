'''
    目标：响应对象常用方法
    1.encoding：
        1）获取请求编码
        2）设置响应编码
    2.headers：
        获取响应信息头信息
    案例：http://www.baidu.com

'''
import requests

url = "http://www.baidu.com"
requests_geta = requests.get(url)

# 查看默认请求编码
print('修改前的编码方式：',requests_geta.encoding)

# 设置请求编码
requests_geta.encoding = "utf-8"
print('修改后的编码方式：',requests_geta.encoding)

# 查看响应内容
print(requests_geta.text)

# 查看消息头
print(requests_geta.headers)



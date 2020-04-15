'''
    目标：requests库的post请求  参数data和json的区别
    案例：新增
    参数：
        1.json传入json字符串
        2.headers传入请求头信息内容
        将字典转换成json格式
    响应：
        响应对象.json()

'''

# 1.导包

import requests
# 2.调用post
# 请求url
url ='http://apis.juhe.cn/cook/query.php'
# 请求header
delete = requests.delete(url)

print(delete.status_code)

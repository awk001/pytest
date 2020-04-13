'''
    目标：requests库的post请求
    案例：新增
    参数：
        1.json传入json字符串
        2.headers传入请求头信息内容
    响应：
        响应对象.json()

'''

# 1.导包
import requests
# 2.调用post
# 请求url
url ='http://apis.juhe.cn/cook/query.php'
# 请求header
header = {"Content-Type": "application/json"}
data = {
        "data": [{
            "id": "45",
            "title": "秘制红烧肉",
            "tags": "家常菜;热菜;烧;煎;炖;红烧;炒锅",
            "imtro": "做红烧肉的豆亲们很多，大家对红烧肉的热爱更不用我说，",
            "ingredients": "五花肉,500g",
            "burden": "玫瑰腐乳,适量;盐,适量;八角,适量;草果,适量;香叶,适量;料酒,适量;米醋,适量;生姜,适量",
            "albums": ["http:\/\/img.juhe.cn\/cookbook\/t\/0\/45_854851.jpg"],
            "steps": [{
                "img": "http:\/\/img.juhe.cn\/cookbook\/s\/1\/45_0824e37faf00b71e.jpg",
                "step": "1.将五花肉煮至断生状态"
            }]}
        ]}

requests_post = requests.post(url=url, json=data, headers=header)
print("url:",requests_post.url)
print("状态码：", requests_post.status_code)
print("cookies：", requests_post.cookies)
print("内容：", requests_post.content)

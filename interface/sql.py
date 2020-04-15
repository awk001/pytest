import pymysql

# 打开数据库连接
class connMySQL:
    db = pymysql.connect( host ="127.0.0.1",
                         port = 3306,
                         user = "root",
                         database = "ecshop"
                        )
    # 使用cursor()方法创建一个游标对象cur （可以理解为激活数据库）
    cursor = db.cursor()

    # 使用execute()执行SQL语句
    sql = "select * from ecs_users"
    try:
        cursor.execute(sql)
        db.commit()
    except Exception as e:
        db.rollback()

    # 使用fetchall()方法获取查询结果 (接收全部的返回结果)
    data = cursor.fetchall()
    print(data[0][3])

    # 解决游标遍历慢的方法：一行一行去遍历，而不是一下全部读取出来
    # for i in cur:
    #     print (i)
    cursor.close()
    db.close()

def strr():
    s = "asdfefef,"
    print(s)

strr()


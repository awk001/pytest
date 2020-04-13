import pymysql,unittest

# 打开数据库连接
class pdbc:

    def setUp(self):
        # 数据库连接
        self.db = pymysql.connect(host ="127.0.0.1",
                             port = 3306,
                             user = "root",
                             database = "ecshop"
                            )
        # 使用cursor()方法创建一个游标对象cur （可以理解为激活数据库）
        self.cursor = self.db.cursor()

    def tearDown(self):
        self.cursor.close()
        self.db.close()

    # 封装执行sql
    def execute(self,sql):
        try:
            self.cursor.execute(sql)
        except Exception as e:
            self.db.rollback()
        self.db.commit()

    # select查询方法
    def test_select(self,database,**params):
        self.setUp()
        # 使用execute()执行SQL语句
        sql = "select "+ params +" from"+ database
        self.execute(sql)
        # 使用fetchall()方法获取查询结果 (接收全部的返回结果)
        data = self.cursor.fetchall()
        print(data)
        self.tearDown()
    # 数据添加方法
    def test_insert(self,database,**params):
        self.setUp()
        # 使用execute()执行SQL语句
        sql = "insert into "+database+ " values"+(params)
        self.execute(sql)
        self.tearDown()

    # 根据条件删除表数据
    def test_delete(self,database,condition,param):
        self.setUp()
        sql = "delete from "+database+" where "+condition+" = "+param
        self.execute(sql)
        self.tearDown()

    def test_update(self,database,num,condition=[],param=[]):
        self.setUp()
        sql = "update "+database+" set "
        for i in num:
            if i != 0:
                sql += condition[i] + "="+param[i]+","
                # 如果是最后一次拼接，那么在原基础上去掉后面的逗号
                if i == num:
                    sql[-1].replace(",", "")
            else:
                sql += condition[0] + "=" + param[0]
        # 执行sql语句
        self.execute(sql)
        self.tearDown()





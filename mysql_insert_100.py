import pymysql
conn = pymysql.connect(user="root", password="123456", port=3306,
                       db="test", host="localhost", charset="utf8")  # 数据库连接
cursor = conn.cursor()  # 获取游标

sql = "INSERT INTO user03 " \
      "(id,userName,passWrod,create_by)VALUES " \
      "(%s,%s,%s,%s)"  # 输入ql语句，%s的数量要与参数的数量对应
for i in range(1,101):
    cursor.execute(sql, (
    int(i),'user'+str(i),'123456','听风'))  # 传值，i为变量
    conn.commit()  # 提交事务
conn.close()  # 关闭数据连接

#以上代码为向数据库批量插入100条数据。

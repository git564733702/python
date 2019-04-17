#直接向数据库插入大量数据，用于自己有数据库权限时
import pymysql
conn = pymysql.connect(user="root", password="123456", port=3306,
                       db="guest01_test", host="localhost", charset="utf8")  # 数据库连接
cursor = conn.cursor()  # 获取游标

sql = "INSERT INTO sign_guest " \
      "(realname, phone, email, sign, event_id, create_time)VALUES " \
      "(%s,%s,%s,%s,%s,now())"  # 输入ql语句，%s的数量要与参数的数量对应，该表必须存在
for i in range(1,101):
    str_i = str(i)

    realname = "jack" + str_i
    phone = 13800110000 + i
    email = "jack" + str_i + "@mail.com"

    cursor.execute(sql, (realname,phone,email,0,1))  # 传值，i为变量
    conn.commit()  # 提交事务
conn.close()  # 关闭数据连接

#以上代码为向数据库批量插入100条数据。
#create_time字段用now()函数处理
#int格式+i，能固定数据长度，也叫自增（比如100+i；但000+i不行，因为000不是自然数）

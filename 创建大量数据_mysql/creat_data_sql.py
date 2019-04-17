# 生成大量sql插入语句，用于自己没有数据库权限时
f = open('guests.txt','w')
for i in range(1, 101):
    str_i = str(i)
    realname = "jack" + str_i
    phone = 13800110000 + i
    email = "jack" + str_i + "@mail.com"
    sql = 'INSERT INTO sign_guest (realname, phone, email, sign, event_id,create_time)' \
          ' VALUES("'+realname+'",'+str(phone)+ ',"'+email+'",0,1,now());'
    f.write(sql)
    f.write("\n")

f.close()

#create_time字段用now()函数处理
#int格式+i，能固定数据长度，也叫自增（比如100+i；但000+i不行，因为000不是自然数）

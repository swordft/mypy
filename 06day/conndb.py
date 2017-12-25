# 1. YUM安装MySQL-python
# 2. 导入mysql扩展模块 import MySQLdb as mysql
# 3. 连接数据库 db = mysql.connect(arguments...)
# 4. 建立游标,cur=db.cursor()，自此数据库初始化完成，可以干活了
# 5. 编写你的sql语句(增删改查)  sql = "*"
# 6. 执行sql语句 cur.execute(sql)

# 查询分为两种
# 1. 查询单条记录,cur.fetchone()
# 2. 查询多条记录,cur.fetchall()

# 查询多列优化
fields = ['id','name','name_cn','email','mobile']
sql = "SELECT %s FROM users" % ','.join(fields)
cur.execute(sql)

# 结果显示优化
users = []

for row in res:
    user = {}
    for i,k in enumerate(fields):
        user[k] = row[i]
    users.append(user)

#作业
# 1. 添加用户（单独页面）
# 2. 查看用户列表（单独页面）
# 3. 查看某一个用户的信息
# 4. 删除用户（按钮）
# 5. 更新数据（重点）

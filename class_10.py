from pymysql import Connection

# 连接 MySQL
conn = Connection(
    host='localhost',
    port=3306,
    user='root',
    password='123456',
    autocommit=True
)

print(conn.get_server_info())  # 打印 MySQL 服务器版本

cursor = conn.cursor()
conn.select_db('test')  # 选择数据库 'test'

# 插入数据（修正后的 SQL 语句）
cursor.execute("INSERT INTO student VALUES(1001, 'xj', 'xj2002')")

conn.close()  # 关闭连接
from pymysql import Connection


conn = Connection(
    host= 'localhost',
    port= 3306,
    user= 'root',
    password= '123456'

)

print(conn.get_server_info())

cursor = conn.cursor()
conn.select_db('test')
# cursor.execute("create table test_pymysql(id int);")
cursor.execute("select * from student;")
results = cursor.fetchall()

for r in results:
    print(r)


conn.close()
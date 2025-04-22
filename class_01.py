# 1 设计一个类
class Student:
    name = None    # 姓名
    gender = None # 性别
    nationality = None  # 国籍
    nation_place = None    # 惯技
    age = None    # 年龄

# 创建一个对象
stu_1 = Student()

# 对象属性进行赋值
stu_1.name = 'xj'
stu_1.gender = 'nan'
stu_1.nationality = 'cn'
stu_1.nation_place = 'jx'
stu_1.age = 23


# 获取对象中的记录的信息
print(stu_1.name)
print(stu_1.gender)
print(stu_1.nationality)
print(stu_1.nation_place)
print(stu_1.age)
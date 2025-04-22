class Student:
    name = None
    age = None
    tel = None

    def __init__(self, name, age, tel):
        self.name = name
        self.age = age
        self.tel = tel
        print("我是构造方法")

stu = Student('xj', 23, '10086')
print(stu.name)
print(stu.age)
print(stu.tel)
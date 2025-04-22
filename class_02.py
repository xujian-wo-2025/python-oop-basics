class Student:
    name = None
    def say_hi(self):
        print(f"大家好我是{self.name}")
    def say_lou(self, msg):
        print(f"大家好我是{self.name},{msg}")

stu_01 = Student()

stu_01.name = 'xj'
stu_01.say_hi()
stu_01.say_lou('are you ok')
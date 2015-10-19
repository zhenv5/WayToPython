class Student(object):
    count = 0
    books = []
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def printStudentInfo(self):
        print self.count
        print self.books
    @classmethod
    def printStudent(cls):
        #print cls.__name__
        #print dir(cls)
        print cls.count
        print cls.books
    @staticmethod
    def printInfo():
        print Student.count
        print Student.books
    pass

# books is class attributes
Student.books.extend(["Python","Javascript"])
print Student.books
# class can add class attribute after class definition
Student.hobbies = ["reading","sleeping"]
print Student.hobbies

print dir(Student)

stu = Student("Xiaoming",23)

# class instance
print stu.name
print stu.age

# class instance can add new attribute
stu.gender = "male"

print stu.gender

# class intance can access class attribute
print dir(stu)

stu.books.append("C++")
print stu.books

stu_1 = Student("Xiaohong",22)

# stu_1 will share the same class attribute with stu
# stu_1 doesn't have the gender attribute that belongs to stu

print dir(stu_1)
print stu_1.books


Student.printStudent()

stu.printStudent()

stu_1.printStudent()


Student.printInfo()

stu.printInfo()

stu_1.printInfo()

stu.count = 3
stu.books.append("C")

Student.printInfo()

stu.printInfo()

stu_1.printInfo()

Student.printStudent()

stu.printStudent()

stu_1.printStudent()

stu.printStudentInfo()
stu_1.printStudentInfo()




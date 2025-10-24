from os import remove


class Student :
    def __init__(self, firstname, lastname, birthyear, address, faculty, direction) :
        self.firstname = firstname
        self.lastname = lastname
        self.birthyear = birthyear
        self.address = address
        self.faculty = faculty
        self.direction = direction
        self.course = 1




    def get_firstname(self) :
        return self.firstname


    def get_lastname(self) :
        return self.lastname

    def full_name(self) :
        return f"{self.firstname} {self.lastname}"

    def get_age(self, now_year) :
        return now_year - self.birthyear

    def get_info(self) :
        result =  (f"{self.firstname} {self.lastname} {self.birthyear} - yil {self.address}da tug'ilgan."
                   f"\nHozirda {self.faculty} fakultetida {self.direction} yo'nalishida  {self.course} - kursda o'qiydi! ")
        return result

    def set_course(self, new_course) :
        self.course = new_course

    def update_course(self) :
        if self.course < 4 :
            self.course += 1
            return None
        else :
            return f"Kechrasiz {self.firstname} {self.lastname} allaqachon 4 - kursga o'tgan!"








student1 = Student('anvar', 'toshmatov', 2004, 'bandixon', 'axbarot', 'kampyuter ilimlari')
student2 = Student('anvar', 'toshmatov', 2004, 'bandixon', 'axbarot', 'kampyuter ilimlari')
student3 = Student('anvar', 'toshmatov', 2004, 'bandixon', 'axbarot', 'kampyuter ilimlari')
student4 = Student('anvar', 'toshmatov', 2004, 'bandixon', 'axbarot', 'kampyuter ilimlari')

# student1.course = 3  #   tafsiya etilmagan usul.
# print(student1.get_info())
# student1.set_course(4)
# print(student1.update_course())
# student2.update_course()
# print(student1.get_info())
# print(student2.get_info())



class Fan :
    def __init__(self, name) :
        self.name = name
        self.students = []
        self.students_number = 0


    def add_student(self, student) :
        self.students.append(student)
        self.students_number += 1

    def get_fan(self) :
        return self.name


    def get_students(self) :
        return [student.get_info() for student in self.students]

    def get_students_name(self) :
        return [student.full_name() for student in self.students]



    #  METHODLARNI CHIQARISH UCHUN METHOD
# def see_methods(klass) :
#     return [method for method in dir(klass) if '__' != method[0 : 2]]
#
#     #  METHODLARNI CHIQARISH UCHUN METHOD
# def get_methods(klass) :
#     return [method for method in dir(klass) if method.startswith("__") is not True]
#
# def get_method(klass) :
#     return [method for method in dir(klass) if method.startswith('__') == False ]


# method1 = see_methods(Fan)
# method2 = see_methods(Student)
# print(method1)
# print(method2)
# print(get_methods(Fan))
# print(get_methods(Student))
# print(get_method(Student))



fan1 = Fan('Matemetika')
fan2 = Fan('Oliy Matemetika')
fan3 = Fan('Chiziqli Matemetika')
fan4 = Fan('Matemetika Analiz')


# print(fan1.get_fan())

fan1.add_student(student1)
fan1.add_student(student2)
fan1.add_student(student3)
fan1.add_student(student4)

# print(fan1.students)
# print(fan1.students_number)
# print(fan1.get_students())
# print(fan1.get_students_name())


# print(dir(Student))   #   dir() klassning ichidagi methodlarni chiqaradi!
#   Natija:  ['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__',
#   '__getstate__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__',
#   '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__',
#   'full_name', 'get_age', 'get_firstname', 'get_info', 'get_lastname', 'set_course', 'update_course']
# print(dir(Fan))


# print(student1.__dict__)
# print(student2.__dict__.keys())
# print(student2.__dict__.values())
# print(get_method(student1))   #   obektning xususiyatlari va methodlarni chiqaradi
# print(dir(student1))
























































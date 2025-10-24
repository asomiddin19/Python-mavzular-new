# Avvalga darslarda yaratilgan obyektlarga (Shaxs, Talaba) turli dunder metodlarni qo'shishni mashq qiling.
#
#     Obyekt haqida ma'lumot (__rerp__)
#
#     Talabalarni bosqichi bo'yicha solishtirish (__lt__,__eg__ va hokazo)


from uuid import uuid4

class Person :
    def __init__(self, firstname, lastname, birthyear) :
        self.firstname = firstname
        self.lastname = lastname
        self.birthyear = birthyear


    def __repr__(self) :
        return f"{self.firstname} {self.lastname}"


    def get_firstname(self) :
        return self.firstname

    def get_lastname(self) :
        return self.lastname

    def get_age(self, now_year) :
        return now_year - self.birthyear

    def get_info(self) :
        info = f"{self.firstname} {self.lastname} {self.birthyear} - yilda tug'ilgan."
        return info



class Student(Person) :
    def __init__(self, firstname, lastname, birthyear, address, course, direction) :
        super().__init__(firstname, lastname, birthyear)
        self.address = address
        self.course = course
        self.direction = direction
        self.student_id = uuid4()


    def get_address(self) :
        return self.address

    def get_course(self) :
        return self.course

    def get_direction(self) :
        return self.direction


    def get_id(self) :
        return self.student_id

    def  __eq__(self, student) :  # tenglik uchun!
        return self.course == student.course

    def __lt__(self, student) :  # katta yoki kichik!
        return self.course < student.course

    def __le__(self, student) :  # katta yoki teng kichik yoki teng!
        return self.course <= student.course



class Group :
    def __init__(self, direction) :
        self.direction = direction
        self.students = []
        self.students_number = 0

    def __add__(self, *new_students) :
        for student in new_students :
            if isinstance(student, Student) :
                self.students.append(student)


    def get_student(self):
        return [student.get_info() for student in self.students]

    def get_student_number(self) :
        return self.students_number

    def get_name(self) :
        return self.direction

    def get_info(self) :
        info = (f"{self.direction} gurpasida {self.students_number} ta talaba bor."
                f"\nTalabalar: {[self.get_student()]}")
        return info









#  person class
person1 = Person('Alisher', 'usmonov', 2003)
person2 = Person('Alisher', 'usmonov', 2003)
person3 = Person('Alisher', 'usmonov', 2003)
person4 = Person('Alisher', 'usmonov', 2003)


# student class
student1 = Student('akmal', 'komilov', 2002, 'termiz', 3, 'SI')
student2 = Student('akmal', 'komilov', 2002, 'termiz', 4, 'IT')
student3 = Student('akmal', 'komilov', 2002, 'termiz', 2, 'IT')
student4 = Student('akmal', 'komilov', 2002, 'termiz', 4, 'DI')



# group class
group1 = Group('SI')
group2 = Group('SI')
group3 = Group('SI')
group4 = Group('SI')







# print(person1.get_info())
# print(student1)
# print(student2.get_info())
# print(student1.get_id())
# group3 + student4
# group3 + student3
# print(group3.get_student())
# print(student3 == student4)
# print(student1 > student4)
# print(student1 <= student2)


































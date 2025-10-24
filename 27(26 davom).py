
#      Avvalgi darslarimizda yaratgan Shaxs va Talaba klasslariga yopiq xususiyatlar qo'shing
#      va ularning qiymatini ko'rsatuvchi va o'zgartiruvchi metodlar yozing.
from uuid import uuid4
class Person :
    __person_number = 0
    __persons = {}
    __class_password = 'name0302'
    def __init__(self, firstname, lastname, birthyear) :
        self.firstname = firstname
        self.lastname = lastname
        self.birthyear = birthyear
        self.__passport_number = uuid4()
        Person.__person_number += 1
        Person.__persons[self.firstname] = self.__passport_number


    def get_firstname(self) :
        return self.firstname

    def get_lastname(self) :
        return self.lastname

    def get_birthyear(self) :
        return self.birthyear

    def get_age(self, now_year = 2025) :
        return now_year - self.birthyear


    def get_info(self) :
        info = (f"{self.firstname} {self.lastname} {self.birthyear} - yilda tug'ilgan."
                f"\nPasport raqami: {self.__passport_number}.")
        return info


    @classmethod
    def get_persons(cls) :
        return f"Foydalanuvchilar: {[person.title() for person in cls.__persons]}"

    @classmethod
    def get_person_id(cls) :
        print(f"Ro'yhatmizda jami {cls.__person_number} ta foydalanuvchi bor. ")
        n = 1
        for key, value in cls.__persons.items():
            print(f"{n}.Ismi: {key.title()}\tId raqami: {value}.")
            n += 1

    @classmethod
    def get_person_number(cls) :
        return cls.__person_number

    @classmethod
    def get_password(cls) :
        password = input("Kirish uchun paroni kiriting: ")
        if cls.__class_password == password :
            print(cls.__class_password)
        else:
            print("Parolni xato kiritdingiz!")

    @classmethod
    def get_data(cls, password) :
        if cls.__class_password == password :
            print(f"Jami foydalanuvchilar haqda malumot: {cls.__person_number} ta foydalanuvchi."
                  f"\n{cls.get_persons()}")
        else:
            print("Malumot yo'q!")



person1 = Person('alisher', 'sadullayev', 2003)
person2 = Person('anvar', 'sadullayev', 2003)
person3 = Person('said', 'sadullayev', 2003)
person4 = Person('komil', 'sadullayev', 2003)
person5 = Person('bobur', 'sadullayev', 2003)
person6 = Person('olim', 'sadullayev', 2003)


class Student(Person) :
    __students_number = 0
    __students = []
    __student_password = 'student12'
    def __init__(self, firstname, lastname, birthyear, course, address, direction) :
        super().__init__(firstname, lastname, birthyear)
        self.course = course
        self.address = address
        self.direction = direction
        Student.__students.append(self.firstname)
        Student.__students_number += 1




    def get_course(self) :
        return self.course

    def get_address(self) :
        return self.address

    def get_info(self) :
        info = (f"{self.firstname} {self.lastname} {self.birthyear} - yilda {self.address}da tug'ilgan."
                f"\n{self.direction} {self.course} - kurs talabasi.")
        return info

    def add_course(self) :
        self.course += 1

    def update_course(self, new_course) :
        self.course = new_course


    @classmethod
    def get_students(cls):
        info = (f"Guruximizda {cls.__students_number} ta talaba bor."
                f"\nUlarning ro'yhati: {cls.__students}.")
        return info


student1 = Student('jamshid', 'alimov', 2002, 3, 'termiz', 'axborot')
student2 = Student('alisher', 'saidov', 2002, 3, 'termiz', 'elektronika')
student3 = Student('said', 'vohidov', 2002, 3, 'termiz', 'ekotizim')
student4 = Student('shukur', 'qodirov', 2002, 3, 'termiz', 'konchlik')
print(student1.get_info())
# print(student1.get_persons())
# print(student1.get_students())

#  Yuqoridagi klasslarga talabalar_soni va odamlar_soni degan klassga oid xususiyatlar qo'shing.
# Klassga oid xususiyatlar bilan ishlash uchun maxsus @classmethod lar yozing







# print(person1.get_persons())
# person6.get_person_id()
# person6.get_data('name0302')
# person6.get_data('name030223')














































#  Talaba klassiga yana bir, fanlar degan xususiyat qo'shing.
#  Bu xususiyat parametr sifatida uzatilmasin va obyekt yaratilganida bo'sh ro'yxatdan iborat bo'lsin (self.fanlar=[])
#  Fan degan yangi klass yarating va bu klassdan turli fanlar uchun alohida obyektlar yarating.
#  Talaba klassiga fanga_yozil() degan yangi metod yozing. Bu metod parametr sifatida
#  Fan klassiga tegishli obyektlarni qabul qilib olsin va talabaning fanlar ro'yxatiga qo'shib qo'ysin.
#  Talabaning fanlari ro'yxatidan biror fanni o'chirib tashlash uchun remove_fan() metodini yozing.
#  Agar bu metodga ro'yxatda yo'q fan uzatilsa "Siz bu fanga yozilmagansiz" xabarini qaytarsin.




class Person:
    def __init__(self,firstname, lastname, passport_number, birthyear, address) :
        self.firstname = firstname
        self.lastname = lastname
        self.passport_number = passport_number
        self.birthyear = birthyear
        self.address = address

    def get_firstname(self) :
        return self.firstname

    def get_lastname(self) :
        return self.lastname
    def get_info(self) :
        info = (f"{self.firstname} {self.lastname}, {self.birthyear} - yilda {self.address}da tug'ilgan"
                f"\nPasport raqami: {self.passport_number}.")
        return info






class Student(Person) :
    def __init__(self, firstname, lastname, passport_number, birthyear,address, id_number, direction, birthplace):
        super().__init__(firstname, lastname, passport_number, birthyear, address)
        self.id_number = id_number
        self.direction = direction
        self.birthplace = birthplace
        self.course = 1
        self.lesson_list = []
        self.lessons_number = 0


    def get_id(self) :
        return self.id_number

    def get_direction(self) :
        return self.direction

    def get_birthplace(self) :
        return self.birthplace

    def add_lesson(self, *lessons) :
        self.lesson_list = [lesson for lesson in lessons]
        self.lessons_number += len(self.lesson_list)


    def get_lesson(self) :
        result = (f"{self.firstname} {self.lastname} {self.lessons_number} ta fanga yozilgan,  fanlar ro'yhati: "
                  f"\n{[lesson.get_name() for lesson in self.lesson_list]}")
        return result


    def remove_lesson(self, *lessons) :
        """self.lesson_list = [lesson for lesson in self.lesson_list if lesson not in lessons]"""
        for lesson in lessons :
            if lesson in self.lesson_list :
                self.lesson_list.remove(lesson)
            else:
                print(f"{lesson.get_name()} faniga yozilmagansiz!")






class Lesson :
    def __init__(self, name) :
        self.name = name


    def get_name(self) :
        return self.name





# Person kilassining obektlari
person1 = Person('hoshim', 'alimov', 'ps12345', 2002, 'Termiz')
person2 = Person('hoshim', 'alimov', 'ps12345', 2002, 'Termiz')
person3 = Person('hoshim', 'alimov', 'ps12345', 2002, 'Termiz')
person4 = Person('hoshim', 'alimov', 'ps12345', 2002, 'Termiz')
person5 = Person('hoshim', 'alimov', 'ps12345', 2002, 'Termiz')





#  Student klassining obektlari
student1 = Student('fazliddin', 'komilov', 'ps23942', 2001, 'Termiz', 'id', 'kampyuter', "termiz")
student2 = Student('fazliddin', 'komilov', 'ps23942', 2001, 'Termiz', 'id', 'kampyuter', "termiz")
student3 = Student('fazliddin', 'komilov', 'ps23942', 2001, 'Termiz', 'id', 'kampyuter', "termiz")
student4 = Student('fazliddin', 'komilov', 'ps23942', 2001, 'Termiz', 'id', 'kampyuter', "termiz")
student5 = Student('fazliddin', 'komilov', 'ps23942', 2001, 'Termiz', 'id', 'kampyuter', "termiz")
student6 = Student('fazliddin', 'komilov', 'ps23942', 2001, 'Termiz', 'id', 'kampyuter', "termiz")




# Lesson kilasining obektlari
lesson1 = Lesson('Matimatika')
lesson2 = Lesson('Oliy Matimatika')
lesson3 = Lesson('Chiziqli Matimatika')
lesson4 = Lesson('Diskret Matimatika')
lesson5 = Lesson('Ona tili')
lesson6 = Lesson('Kimyo')
lesson7 = Lesson('Fizika')


student1.add_lesson(lesson1, lesson2, lesson3, lesson4, lesson5)
# print(student1.get_lesson())
student1.remove_lesson(lesson1, lesson2, lesson6)
print(student1.get_lesson())




















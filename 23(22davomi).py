class Person :
    def __init__(self, firstname, lastname, passport_number, birthyear, address) :
        self.firstname = firstname
        self.lastname = lastname
        self.passport_number = passport_number
        self.birthyear = birthyear
        self.address = address



    def get_firstname(self) :
        return self.firstname

    def get_lastname(self) :
        return self.lastname

    def get_fullname(self) :
        return self.firstname, self.lastname

    def get_passport(self) :
        return self.passport_number

    def get_birthyear(self) :
        return self.birthyear

    def get_age(self, year = 2025) :
        return year - self.birthyear

    def get_address(self) :
        return self.address

    def get_info(self) :
        info = f"Fuqoro ma'lumotlari: {self.firstname.title()} {self.lastname.title()}, {self.birthyear} - yilda {self.address.title()} shaxrida tug'ilgan."
        info += f"\nPasport raqami: {self.passport_number}."
        return info



person1 = Person('alisher', 'akmalov', 'ps12345', 2001, 'Termiz')
person2 = Person('alisher', 'akmalov', 'ps12345', 2001, 'Termiz')
person3 = Person('alisher', 'akmalov', 'ps12345', 2001, 'Termiz')
person4 = Person('alisher', 'akmalov', 'ps12345', 2001, 'Termiz')
person5 = Person('alisher', 'akmalov', 'ps12345', 2001, 'Termiz')

# print(person1.get_age())
# print(person1.get_info())


class Student(Person) :
    def __init__(self, firstname, lastname, passport_number, birthyear, address, birthplace, student_id, direction) :
        super().__init__(firstname, lastname, passport_number, birthyear, address)
        self.birthplace = birthplace
        self.student_id = student_id
        self.direction = direction
        self.course = 1

    def get_id(self) :
        return self.student_id

    def get_course(self) :
        return self.course

    def get_direction(self) :
        return self.direction

    def get_info(self) :
        info = (f"Talaba ma'lumotlari: {self.firstname} {self.lastname}, {self.course} - kurs talabasi, {self.birthyear} - yilda {self.address} shaxrida tug'ilgan,"
                f"\nYo'nalish nomi: {self.direction}, pasport raqami: {self.passport_number}, id raqami: {self.student_id} "
                f"\nTug'ilgan joyi: {self.birthplace.get_birt_place()}")
        return info




class Birthplace :
    def __init__(self, house, street, district, region) :
        self.house = house
        self.street = street
        self.district = district
        self.region = region


    def get_birt_place(self) :
        birthplace = f"{self.region.title()} viloyati, {self.district} tumani, {self.street} ko'chasi, {self.house} - uy."
        return birthplace



student1_place = Birthplace(23, 'Yashnar', 'Bandixon', 'Surxandaryo')
student2_place = Birthplace(23, 'Yashnar', 'Bandixon', 'Surxandaryo')
student3_place = Birthplace(23, 'Yashnar', 'Bandixon', 'Surxandaryo')
student4_place = Birthplace(23, 'Yashnar', 'Bandixon', 'Surxandaryo')
student5_place = Birthplace(23, 'Yashnar', 'Bandixon', 'Surxandaryo')




student1 = Student('Komil', 'alimov', 'ps12943', 2003, 'bandixon', student1_place, 'id12345', 'Kampyuter injnering')
student2 = Student('Komil', 'alimov', 'ps12943', 2003, 'bandixon', student2_place,'id12345', 'Kampyuter injnering')
student3 = Student('Komil', 'alimov', 'ps12943', 2003, 'bandixon',student3_place, 'id12345', 'Kampyuter injnering')
student4 = Student('Komil', 'alimov', 'ps12943', 2003, 'bandixon', student4_place,'id12345', 'Kampyuter injnering')
student5 = Student('Komil', 'alimov', 'ps12943', 2003, 'bandixon', student5_place,'id12345', 'Kampyuter injnering')


# print(student1.get_info())
# print(student1.get_direction())
# print(person1.get_info())
# print(student1.birthplace.get_birt_place())
print(student1.get_info())





































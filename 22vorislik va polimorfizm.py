

class Person :
    def __init__(self, firstname, lastname, passport_number, birthyear, address) :
        self.firstname = firstname
        self.lastname = lastname
        self.passport_number = passport_number
        self.birthyear = birthyear
        self.address = address


    def get_name(self) :
        return self.firstname


    def get_firstname(self) :
        return self.firstname

    def get_fullname(self) :
        return self.firstname, self.lastname

    def get_passport(self) :
        return self.passport_number


    def get_age(self, now_year = 2025) :
        return now_year - self.birthyear


    def get_address(self) :
        return self.address


    def get_info(self) :
        info = f"Shaxs malumot: {self.firstname}, {self.lastname} {self.birthyear} - yil {self.address}da tu'gilgan."
        info += f"\nPasport raqami: {self.passport_number}, yoshi {self.get_age()} da."
        return info



person1 = Person('alisher', 'alimov', '1234ps', 2003, "Teriz")
person2 = Person('alisher', 'alimov', '1234ps', 2003, "Teriz")
person3 = Person('alisher', 'alimov', '1234ps', 2003, "Teriz")
person4 = Person('alisher', 'alimov', '1234ps', 2003, "Teriz")
person5 = Person('alisher', 'alimov', '1234ps', 2003, "Teriz")


print(person1.get_name())
print(person1.get_info())



class Student(Person):
    def __init__(self, firstname, lastname, passport_number, birthyear, address, id_number, direction) :
        super().__init__(firstname, lastname, passport_number, birthyear, address)
        self.id_number = id_number
        self.direction = direction
        self.course = 1


    def get_id(self) :
        return self.id_number


    def get_direction(self) :
        return self.direction

    def get_course(self) :
        return self.course

    def add_course(self) :
        self.course += 1

    def update(self, new_course) :
        self.course = new_course




student1 = Student('alisher', 'anvarov', 'ps123', 2003 , 'Termiz', 'id12345',"Kampyuter injnering")
student2 = Student('alisher', 'anvarov', 'ps123', 2003, 'Termiz', 'id12345',"Kampyuter injnering")
student3 = Student('alisher', 'anvarov',  'ps123',2003, 'Termiz', 'id12345',"Kampyuter injnering")
student4 = Student('alisher', 'anvarov', 'ps123',2003,  'Termiz', 'id12345',"Kampyuter injnering")
# print(student1.get_info())
















































a = 24   #  bu yerda a o'zgaruvchi obekt int class dan yaratilgan obekt hisoblanadi!
# print(type(a))   # Natija: <class 'int'>

matn = 'assalomu alaykum'    #  bu matn ham str classdan yaratilagn obekt
# print(type(matn))   #  Natija: <class 'str'>

#  bularning metod va hususiyatlari mavjud misol uchun matn yaniy str classda upper() metodi
#  mavjud hususiyati ""  qo'shtirnoq belgsning ichiga yozladi!



def salom() :
    print("Assalomu alaykum ")


# print(type(salom))  #  Natija:   <class 'function'>   salom nomli obekt function klassga tegishli ekan!






class Talaba :
    def __init__(self, firstname, lastname, birthyear, adress) :
        self.firstname = firstname
        self.lastname = lastname
        self.birthyear = birthyear
        self.adress = adress


    def get_firstname(self) :
        return self.firstname


    def get_lastname(self) :
        return self.lastname


    def get_age(self, now_year) :
        return now_year - self.birthyear


    def tanishtir(self) :
        return f"Talaba malumot: Ismi {self.firstname}, familyasi {self.lastname}, tug'ilgan yili {self.birthyear} - yil, yashash joyi {self.adress}."







student1 = Talaba('asomiddin', 'abduqahharov', 2005, 'termiz')
student2 = Talaba('asomiddin', 'abduqahharov', 2005, 'termiz')
student3 = Talaba('asomiddin', 'abduqahharov', 2005, 'termiz')
student4 = Talaba('asomiddin', 'abduqahharov', 2005, 'termiz')
student5 = Talaba('asomiddin', 'abduqahharov', 2005, 'termiz')


# print(student1.tanishtir())
# print(student2.get_lastname())
# print(student1.get_age(2025))


#  Web sahifangiz uchun foydalanuvchi (user) klassini tuzing. Klassning xususiyatlari sifatida
#  odatda ijtimoiy tarmoqlar talab qiladigan ma'lumotlarni kiriting (ism, foydalanuvchi ismi, email, va hokazo)

class User :
    def __init__(self, firstname, lastname, username, phone_number, email, password) :
        self.firstname = firstname
        self.lastname = lastname
        self.username = username
        self.phone_number = phone_number
        self.email = email
        self.password = password


    def get_firstname(self) :
        return self.firstname


    def get_lastname(self) :
        return self.lastname

    def get_username(self) :
        return self.username

    def get_phone_number(self) :
        return self.phone_number

    def get_email(self) :
        return self.email

    def get_password(self) :
        return self.password

user1 = User('abdulloh', 'anvar', 'anvar_user', '+998930501030', 'asomiddin0519@gmail.com', 'backend_19')
user2 = User('abdulloh', 'anvar', 'anvar_user', '+998930501030', 'asomiddin0519@gmail.com', 'backend_19')
user3 = User('abdulloh', 'anvar', 'anvar_user', '+998930501030', 'asomiddin0519@gmail.com', 'backend_19')
user4 = User('abdulloh', 'anvar', 'anvar_user', '+998930501030', 'asomiddin0519@gmail.com', 'backend_19')
user5 = User('abdulloh', 'anvar', 'anvar_user', '+998930501030', 'asomiddin0519@gmail.com', 'backend_19')

# print(user5.get_firstname())
# print(user5.get_password())




#  Klassga bir nechta metodlar qo'shing, jumladan get_info() metodi foydalanuvchi haqida yig'ilgan ma'lumotlarni
#  chiroyli qilib chiqarsin (masalan: "Foydalanuvchi: alijon1994, ismi: Alijon Valiyev, email: alijon1994@gmail.com).



class Inson :
    def __init__(self, firstname, lastname, birthyear, adress ) :
        self.firstname = firstname
        self.lastname = lastname
        self.birthyear = birthyear
        self.adress = adress

    def get_firstname(self) :
        return self.firstname

    def get_age(self, now_year) :
        return now_year - self.birthyear

    def get_info(self, now_year) :
        return f"Malumotlar: Ismi {self.firstname}, familyasi {self.lastname}, \ntug'ilgan yili {self.birthyear}, {self.adress}da tug'ilgan, yoshi {self.get_age(now_year)} da."

    def get_adress(self) :
        return f"{self.firstname} {self.birthyear} - yilda {self.adress}da tug'ilgan."


inson1 = Inson('alisher', 'alimov', 2003, 'termiz')
inson2 = Inson('alisher', 'alimov', 2003, 'termiz')
inson3 = Inson('alisher', 'alimov', 2003, 'termiz')
inson4 = Inson('alisher', 'alimov', 2003, 'termiz')
inson5 = Inson('alisher', 'alimov', 2003, 'termiz')


# print(inson4.get_info(2025))
# print(inson4.get_adress())



























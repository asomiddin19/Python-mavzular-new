#  Yuqoridagi Shaxs klassidan boshqa turli voris klasslar yaratib ko'ring (masalan Professor, Foydalanuvchi, Sotuvchi, Mijoz va hokazo)
#  Har bir klassga o'ziga hoz xususiyatlar va metodlar yuklang.
#
# Barcha yangi klasslar uchun get_info() metodini qayta yozib chiqing.
#
# Voris klasslardan yana boshqa voris klass yaratib ko'ring. Misol uchun Foydalanuvchi klassidan Admin klassini yarating.
#
# Admin klassiga foydalanuvchida yo'q yangi metodlar yozing, masalan, ban_user() metodi konsolga "Foydalanuvchi bloklandi" degan matn chiqarsin.

class Person :
    def __init__(self, firstname, lastname, birthyear, passport_number, address) :
        self.firstname = firstname
        self.lastname = lastname
        self.birthyear = birthyear
        self.passport_number = passport_number
        self.address = address

    def get_firstname(self) :
        return self.firstname

    def get_lastname(self) :
        return self.lastname

    def get_age(self, now_year) :
        return now_year - self.birthyear

    def get_passport(self) :
        return self.passport_number


    def get_info(self, now_year) :
        return f"Malumot: {self.firstname}, {self.lastname} {self.birthyear} - yilda {self.address}da tug'ilgan."






class User(Person) :
    def __init__(self, firstname, lastname, birthyear, passport_number, address, user_name, password, login) :
        super().__init__(firstname, lastname, birthyear, passport_number, address)
        self.user_name = user_name
        self.password = password
        self.login = login


    def get_user(self) :
        return  self.user_name


    def get_password(self) :
        password = input("Kirish uchun parol kiriting: ")
        if password == self.password :
            print('Tabriklayman kirdingiz!')
            savol = input(
                          "\n1.Parol o'zgartrish"
                          "\n2.Parolni ko'rish: "
            )
            if savol == '1' :
                new_password = input("Yangi parolni kiriting: ")
                self.password = new_password
                print("Tabriklayman parol o'rnatildi!")
            else:
                print(f"Sizning parolingiz: {self.password}")
        else:
            print("Parol xato!")

    def get_logen(self) :
        savol = input("Parolni kiritng: ")
        if savol == self.password :
            print(f"Login: {self.login}")
        else:
            print("Parol xato!")

    def get_info(self, now_year = 2026) :
        savol = input("Malumotlarni olish uchun parolni kiriting: ")
        if savol == self.password :
            info = (f"Malumotlar: {self.firstname} {self.lastname} {self.birthyear} - yilda {self.address}da tug'ilgan."
                    f"\nUser name: {self.user_name}, Paroli: {self.password}, Login: {self.login}.")
        else:
            info = "Parolni xato kiritdingiz!"
        return info



class UserAdmin(User) :
    def __init__(self, firstname, lastname, birthyear, passport_number, address, user_name, password, login, admin_password) :
        super().__init__(firstname, lastname, birthyear, passport_number, address, user_name, password, login)
        self.admin_password = admin_password

    def get_admin(self) :
        savol = input("Admin panel uchun parol kiritng: ")
        if savol == self.password :
            result = self.admin_password
        else:
            result = "Parol xato!"
        return result

    def ban_user(self, user) :
        return f"{user.get_firstname()} bloklandi!"





person1 = Person('olim', 'alimov', 1998, 'ps12345', 'termiz')
person2 = Person('olim', 'alimov', 1998, 'ps12345', 'sho\'rchi')
person3 = Person('olim', 'alimov', 1998, 'ps12345', 'bandixon')
person4 = Person('olim', 'alimov', 1998, 'ps12345', 'deynov')



user1 = User('akbar', 'komilov', 2003, 'ps12345','bandixon', 'fronted', 'fronted02', 'akbar_olimov')
user2 = User('akbar', 'komilov', 2003, 'ps12345','sho\'rchi', 'fronted', 'fronted02', 'akbar_olimov')
user3 = User('akbar', 'komilov', 2003, 'ps12345', 'denov','fronted', 'fronted02', 'akbar_olimov')
user4 = User('akbar', 'komilov', 2003, 'ps12345', 'denov','fronted', 'fronted02', 'akbar_olimov')



user_admin1 = UserAdmin('akbar', 'komilov', 2003, 'ps12345', 'denov','fronted', 'fronted02', 'akbar_olimov', 'backend_19')




# print(person1.get_info(2025))
# print(user1.get_info(2025))
print(user_admin1.ban_user(user2))






























































#      AMALIY ISH

#  1 Avto degan yangi klass yarating. Unga avtomobillarga doir bo'lgan bir nechta xususiyatlar
#  (model, rang, korobka, narh va hokazo) qo'shing. Ayrim xususiyatlarga standart qiymat bering (masalan, kilometer=0)


#  2 Avto ga oid obyektning xususiyatlarini qaytaradigan metodlar yozing
#     get_info() metodi avto haqida to'liq ma'lumotni matn ko'rinishida qaytarsin


#  3 Avto ga oid obyektning xususiyatlarini yangilaydigan metodlar yozing.
#     update_km() metodi son qabul qilib olib, avtomobilning yurgan kilometrajini yangilab borsin



class Avto :
    def __init__(self, model, colour, car_box, year, price) :
        self.model = model
        self.colour = colour
        self.car_box = car_box
        self.price = price
        self.year = year
        self.km = 0



    def get_model(self) :
        return self.model

    def get_colour(self) :
        return self.colour

    def get_car_box(self) :
        return self.car_box

    def get_price(self) :
        return self.price

    def get_year(self) :
        return self.price

    def get_km(self) :
        return self.km

    def set_km(self, new_km) :
        self.km = new_km


    def get_info(self) :
        return f"Mashina malumot: {self.model} rangi {self.colour}, turi {self.car_box}, \nyili {self.year}, yurgan yo'li {self.km} km {self.price}$ ."


    def add_km(self, add_km) :
        self.km += add_km


def get_method(klass) :
    return [method for method in dir(klass) if method.startswith('__') is False ]


car1 = Avto('malibu', 'qora', 'avtomat', 2025, 40)
car2 = Avto('gentra', 'oq', 'mexanik', 2023, 35)
car3 = Avto('spark', 'qizil', 'avtomat', 2022, 25)
car4 = Avto('cobalt', 'kumush', 'mexanik', 2024, 30)
car5 = Avto('captiva', 'ko‘k', 'avtomat', 2021, 45)



car1.add_km(30000)
# print(car1.get_info())
# print(get_method(car1))
# print(get_method(Avto))




#  4 Yangi, Avtosalon degan klass yarating va kerakli xususiyatlar bilan to'ldiring
#  (salon nomi, manzili, sotuvdagi avtomobillar va hokazo)
#  5 Avtosalonga yangi avtomobillar qo'shish uchun metod yozing
#  6 Avtosalondagi avtomobillar haqida ma'lumot qaytaruvchi metod yozing
#  7 Yuqoridagi obyektlar va ularga tegishli metodlarni tekshirib ko'ring
#  8 dir() funksyasi va __dict__ metodi yordamida o'zingiz yozgan va Pythondagi turli klass
#  va obyektlarning xususiyatlari va metodlarini toping (dir(str), dir(int) va hokazo)



class Avtosalon :
    def __init__(self, name, address) :
        self.name = name
        self.address = address
        self.cars = []
        self.cars_number = 0

    def get_name(self) :
        return self.name

    def get_address(self) :
        return self.address

    def add_car(self, car) :
        self.cars.append(car)
        self.cars_number += 1


    def add_cars(self, *cars_new) :
        self.cars = [car for car in cars_new]
        self.cars_number += len(cars_new)


    def get_cars(self) :
        return [car.get_model() for car in self.cars]

    def get_info(self) :
        return f"{self.name} {self.address} shaxrida joylashgan.\nUnda {self.cars_number} ta avtomobil bor.\nAvtolar: {self.get_cars()}."



salon1 = Avtosalon("Surxon Avto", 'Termiz')
salon2 = Avtosalon("Surxon Avto", 'Termiz')
salon3 = Avtosalon("Surxon Avto", 'Termiz')
salon4 = Avtosalon("Surxon Avto", 'Termiz')


salon1.add_car(car1)
salon2.add_cars(car1, car2, car3, car4, car5)
# print(salon2.get_cars())
# print(salon2.get_info())
print(get_method(Avto))
print(get_method(Avtosalon))













from uuid import uuid4


class Car :
    __password = 'backend_19'
    __car_number = 0
    __cars = []
    def __init__(self, make, model, colour, year, km, price) :
        self.make = make
        self.model = model
        self.colour = colour
        self.year = year
        self.price = price
        self.__km = km
        self.__id  = uuid4()
        Car.__car_number += 1
        Car.__cars.append(self.model)
        Car.__password = 'backend_19'

    @classmethod
    def get_cars(cls) :
        return cls.__cars


    @classmethod
    def get_cars_number(cls) :
        return cls.__car_number


    @classmethod
    def get_password(cls):
        return cls.__password


    def get_make(self) :
        return self.make

    def get_model(self) :
        return self.model

    def get_colour(self) :
        return self.colour

    def get_year(self) :
        return self.year

    def get_km(self) :
        return self.__km

    def get_id(self) :
        return self.__id

    def get_price(self) :
        return self.price

    def add_km(self, new_km) :
        if new_km >= 0 :
            self.__km += new_km
        else:
            print("Mashinaning kmni kamaytrib bo'lmaydi!")

    def get_info(self) :
        return (f"Mashina malumotlari: {self.make} {self.model} {self.colour} rang"
                f" {self.year} - yilda ishlab chiqarilgan {self.__km} km yurgan {self.price} $ \nMashinaning id raqami: {self.__id}")





class CarSalon:
    def __init__(self, name, address) :
        self.name = name
        self.address = address
        self.cars = []
        self.cars_number = 0

    def get_name(self) :
        return self.name

    def get_address(self):
        return self.address.get_info()


    def add_car(self, car) :
        self.cars.append(car)
        self.cars_number += 1

    def get_info(self) :
        info = (f"Avto salonimiz haqida malumot: \n{self.name}da {self.cars_number} ta mashina bor, mashinalarimiz: "
                f"\n{[car.get_model() for car in self.cars]}"
                f"\nBizning manzil: {self.get_address()}.")
        return info




class Address:
    def __init__(self, house, street, district, region) :
        self.house = house
        self.street = street
        self.district = district
        self.region = region

    def get_info(self) :
        info = f"{self.region} viloyati {self.district} tumani {self.street} ko'chasi {self.house} - uy."
        return info







#  Mashinalar
car1 = Car('GM', 'malibu', 'qora', 2025, 200, 35)
car2 = Car('GM', 'malibu', 'qora', 2025, 200, 36)
car3 = Car('GM', 'malibu', 'qora', 2025, 200, 35)
car4 = Car('GM', 'malibu', 'qora', 2025, 200, 38)
car5 = Car('GM', 'malibu', 'qora', 2025, 200, 38)
car6 = Car('GM', 'malibu', 'qora', 2025, 200, 38)
car7 = Car('GM', 'malibu', 'qora', 2025, 200, 38)


#  Salon manzli
salon1_address = Address(12, 'Yangi ariq', 'Termiz', 'Surxandaryo')



# Salonlar
carsalon1 = CarSalon('Surxon Avto', salon1_address)


carsalon1.add_car(car1)
carsalon1.add_car(car2)
carsalon1.add_car(car3)
carsalon1.add_car(car4)



# print(carsalon1.get_address())
# print(carsalon1.get_info())

# car1.add_km(234)
# print(car1.get_id())
# print(car1.get_info())
print(car1.get_cars())
print(car1.get_password())
print(car1.get_cars_number())













































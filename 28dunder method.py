


class Avto:
    cars = []
    cars_number = 0
    def __init__(self, make, model, colour, year, km , price):
        self.make = make
        self.model = model
        self.colour = colour
        self.year = year
        self.km = km
        self.price = price
        Avto.cars.append(self)
        Avto.cars_number += 1


    def __repr__(self) :
        info = f"{self.make} {self.model} {self.colour} {self.year} - yil {self.km} km yurgan {self.price}$."
        return info

    def get_model(self) :
        return self.model

    def get_km(self) :
        return self.km

    def set_km(self, new_km) :
        self.km = new_km

    def update_km(self, update_km ) :
        self.km = update_km


    @classmethod
    def get_cars(cls) :
        return cls.cars

    @classmethod
    def get_cars_number(cls) :
        return cls.cars_number



class AvtoSalon:
    def __init__(self, name, address) :
        self.name = name
        self.address = address
        self.salon_cars = []
        self.salon_cars_number = 0



    def get_name(self) :
        return self.name

    def get_address(self) :
        return self.address.get_address()

    def add_cars(self, *cars) :
        for car in cars :
            self.salon_cars.append(car)
            self.salon_cars_number += len(cars)

    def get_cars(self) :
        cars_info = (f"{self.name} {self.salon_cars_number} ta mashina mavjud "
                     f"\nMashinalar: {[car.get_info() for car in self.salon_cars]}."
                     f"\Manzli: {self.get_address()}.")
        return cars_info


class Address :
    def __init__(self, region, district, street, house) :
        self.region = region
        self.district = district
        self.street = street
        self.house = house

    def get_address(self) :
        info = f"{self.region.title()} viloyati {self.district.title()} tumani {self.street.title()} ko'chasi {self.house} - uy."
        return info



car1 = Avto('GM', 'malibu', 'qora', 2023, 3000, 23)
car2 = Avto('GM', 'damas', 'qora', 2023, 3000, 6)
car3 = Avto('GM', 'cobolt', 'qora', 2023, 3000, 12)
car4 = Avto('GM', 'matiz', 'qora', 2023, 3000, 7)


salon1_address = Address('Surxandaryo', 'termiz', 'Navoiy', 23)
salon2_address = Address('Surxandaryo', 'termiz', 'Navoiy', 23)
salon3_address = Address('Surxandaryo', 'termiz', 'Navoiy', 23)
salon4_address = Address('Surxandaryo', 'termiz', 'Navoiy', 23)


salon1 = AvtoSalon('Surxon Avto', salon1_address)
salon2 = AvtoSalon('Surxon Avto', salon2_address)
salon3 = AvtoSalon('Surxon Avto', salon3_address)
salon4 = AvtoSalon('Surxon Avto', salon4_address)


# print(salon3.get_address())
print(salon1.get_cars())














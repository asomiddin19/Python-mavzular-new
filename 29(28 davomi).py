

class Avto :
    cars = []
    number_cars = 0
    def __init__(self, make, model, colour, year, price, km, owner) :
        self.make = make
        self.model = model
        self.colour = colour
        self.year = year
        self.price = price
        self.km = km
        self.owners = [owner]
        self.cars.append(self)
        self.number_cars += 1



    def get_model(self) :
        return self.model

    def get_price(self) :
        return self.price

    def get_info(self) :
        info = f"{self.make} {self.model} {self.colour} {self.year} - yil {self.km} km yurgan {self.price}$."
        return info

    def add_owner(self, new_owners) :
        self.owners.append(new_owners)

    def get_owner(self) :
        return [owner for owner in self.owners]

    def __repr__(self):
        result = f"{self.make} {self.model} {self.price}$."
        return  result

    def __eq__(self, avto) :   # tenglik uchun
        return self.price == avto.price

    def __lt__(self, avto) :
        return self.price < avto.price

    def __le__(self, avto) :
        return self.price <=  avto.price

    def __len__(self) :
        return len(self.owners)





car1 = Avto('GM', 'malibu', 'qora', 2025, 35, 3000, 'davron')
car2 = Avto('GM', 'matiz', 'qora', 2025, 3, 3000, 'gm')
car3 = Avto('GM', 'cobolt', 'qora', 2025, 13, 3000, 'gm')
car4 = Avto('GM', 'gentra', 'qora', 2025, 15, 3000, 'gm')
car5 = Avto('GM', 'kaptiva', 'qora', 2025, 25, 3000, 'gm')
car6 = Avto('GM', 'kaptiva', 'qora', 2025, 25, 3000, 'gm')
car7 = Avto('GM', 'kaptiva', 'qora', 2025, 25, 3000, 'gm')
car8 = Avto('GM', 'kaptiva', 'qora', 2025, 25, 3000, 'gm')


# print(car1)
# print(car2)
# print(car3)
# print(car5.get_info())
# print(car1 == car2)
# print(car1 < car3)
# print(car1 <= car2)
# car1.add_owner('olim')
# print(car1.get_owner())
# print(len(car1))
# print(car2)
# print(car1.get_owner())




class AvtoSalon :
    def __init__(self, name, address ) :
        self.name = name
        self.address = address
        self.cars = []
        self.cars_number = 0


    def get_name(self) :
        return self.name

    def add_cars(self, *new_cars) :
        for car in new_cars :
            if isinstance(car, Avto) :
                self.cars.append(car)
                self.cars_number += 1

    def get_cars(self ) :
        return [car.get_info() for car in self.cars]

    def get_cars_number(self) :
        return self.cars_number

    def get_info(self) :
        info = (f"{self.name}da {self.cars_number} ta avtomobil bor"
                f"\n{self.address.get_address()} da joylashgan "
                f"\nMashinalari: {self.get_cars()}")
        return info

    def __len__(self) :
        return len(self.cars)


    def __getitem__(self, index) :
        return self.cars[index]

    def __setitem__(self, index, new_car) :
        self.cars[index] = new_car


    def __call__(self, *new_cars) :
        if new_cars :
            for car in new_cars :
                self.add_cars(car)
        else:
            return [car.get_model() for car in self.cars]


    def __add__(self, other_salon) :
        if isinstance(other_salon, AvtoSalon) :
            new_salon = AvtoSalon( f"{self.address} {other_salon.address}", f"{self.name} {other_salon.name}")
            new_salon.cars = self.cars + other_salon.cars
            new_salon.cars_number = self.cars_number + other_salon.get_cars_number()
            return new_salon







class Address :
    def __init__(self, region, district, street, number_house) :
        self.region = region
        self.district = district
        self.street = street
        self.number_house = number_house



    def get_address(self) :
        info = f"{self.region.title()} viloyati {self.district.title()} tumani {self.street.title()} ko'chasi {self.number_house} - uy."
        return info







salon1_address = Address('surxandaryo', 'termiz', 'navoiy', 54)
salon2_address = Address('surxandaryo', 'angor', 'yangi ariq', 54)
salon3_address = Address('surxandaryo', 'bandixon', 'chinor', 54)
salon4_address = Address('surxandaryo', 'denov', 'bog\'ishamol', 54)



salon1 = AvtoSalon('Surxon Avto', salon1_address)
salon2 = AvtoSalon('GM Avto', salon1_address)
salon3 = AvtoSalon('RM Avto', salon1_address)
salon4 = AvtoSalon('SA Avto', salon1_address)

salon1.add_cars(car1, car2, car3)
salon2.add_cars(car8, car7, car5, car6)

# print(salon1.get_info())
# print(len(salon1))
# salon1[0] = car5
# print(salon1[:])
# salon1(car8, car7)
print(salon1())
print(salon2())
salon1_2 = salon1 + salon2
print(salon1_2.get_info())









































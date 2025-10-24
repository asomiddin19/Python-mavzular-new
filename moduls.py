#   FUNKSIYALAR


def avto_info(kompaniya, model, colour, year, price, km) :
    cars = {
        'kompaniya' : kompaniya,
        'model' : model,
        'colour' : colour,
        'year' : year,
        'price' : price,
        'km' : km
    }
    return cars


def avto_kirit() :
    cars = []
    while True :
        kompaniya = input("Kompaniya: ")
        model = input('Model: ')
        colour = input("Rangi : ")
        year = input("Yili: ")
        price = input("Narxi: ")
        km = input("Yurgan yo'li: ")
        cars.append(avto_info(kompaniya, model, colour, year, price, km))
        savol = input("Yana qo'shasizmi (ha/yo'q): ")
        if savol == "yo'q" :
            break
    return cars


def avto_malumot(avtos) :
    return f"{avtos['kompuyter']}, {avtos['model']}, {avtos['year']}, {avtos['price']}."







































































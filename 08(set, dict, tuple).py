# Python Tuples (Tuple’lar)
#
# Nima? Tuple’lar ham tartiblangan ma’lumotlar to‘plami, lekin o‘zgartirilmaydigan (immutable).
# Elementlar qavs ( ) ichida yoki qavslarisiz yoziladi.
# Xususiyatlari:
#
# Elementlarni o‘zgartirish, qo‘shish yoki o‘chirish mumkin emas.
# Takrorlanuvchi elementlarga ruxsat beradi.
#
#
# Misol:
# pythonmevalar = ('olma', 'anor', 'olma')
# # mevalar[1] = 'nok'  # Bu xato beradi, o'zgartirib bo'lmaydi
# print(mevalar)  # Natija: ('olma', 'anor', 'olma')
#
# Qachon ishlatish? Ma’lumotlarning o‘zgarmasligi kerak bo‘lgan holatlarda (masalan, kunlar, oylar kabi doimiy qiymatlar).
#



























#    Python Sets (To‘plamlar)
#
# Nima? To‘plamlar tartibsiz (unordered) va o‘zgartirilishi mumkin bo‘lgan (mutable) elementlar to‘plamidir. Elementlar jingalak qavs { } ichida saqlanadi.
# Xususiyatlari:
#
# Takrorlanuvchi elementlarga yo‘l qo‘yilmaydi (agar bir xil element qo‘shilsa, faqat bitta nusxasi saqlanadi).
# Indeks orqali murojaat qilib bo‘lmaydi.
#
#
# Misol:
# pythonmevalar = {'olma', 'anor', 'olma'}  # Takrorlanmaydi
# mevalar.add('nok')  # Qo'shish
# print(mevalar)  # Natija: {'olma', 'anor', 'nok'} (tartibi tasodifiy)
#
# Qachon ishlatish? Takrorlanishni oldini olish yoki noyob elementlarni saqlash kerak bo‘lganda (masalan, foydalanuvchilar ro‘yxati).



# meva = {'olma', 'anor', 'olcha', 'banan'}
# meva.add('olma')
# meva.add("shaftoli")
# print(meva)
#
# meva.clear()
# print(meva)
# meva.add("olma")
# meva.add("sabzi")
# meva.add("anjir")
# meva.add("rediska")
# print(meva)
# copy_meva = meva.copy()
# print(meva)
# print(copy_meva)


# meva1 = {'olcha', 'olma', 'kartoshka', 'piyoz', 'banan', 'anjir', 'kaktus', 'anor', 'nok'}
# meva2 = {'olcha', 'xurmo', 'sedana', 'apilsin', 'kartoshka', 'banan'}
# meva3 = {'kartoshka', 'banan', 'olma', 'mandarin', 'shaftoli', 'kaktus'}
# meva_difrence = meva1.difference(meva2, meva3)    #   meva1dan meva2 da va meva3da bor va uchalasida bo'lgan elementlarni olib tashlaydi.
# print(meva_difrence)


#
# set1 = {1, 2, 3, 4}
# set2 = {3, 4, 5}
# result = set1.difference(set2)
# print(result)  # Natija: {1, 2}
# print(set1)    # Asl to'plam o'zgarmaydi: {1, 2, 3, 4}


# set1 = {1, 2, 3, 4}
# set2 = {3, 4, 5}
# set1.difference_update(set2)
# print(set1)    # Asl to'plam o'zgardi: {1, 2}



# cars1 = {'mers', 'malibu', 'bmw', 'damas', 'jentra'}
# cars2 = {"kaptiva", 'malibu', 'gelik', 'audio', 'ferrari'}
# # cars = cars1.difference(cars2)
# # print(cars)
# # cars1.difference_update(cars2)
# # print(cars1)
#
#
# print(cars1)
# cars1.discard('mers')
# cars1.discard("bmw")
# print(cars1)
#
#
# ikki_bor = cars1.intersection(cars2)#   okkisida ham bor elementni qaytaradi
# print(ikki_bor)
#
#
# son1 = {1, 2, 3, 4, 5, 6, 7}
# son2 = {1, 2, 3, 4}
# result = son1 < son2
# result1 = son2 < son1   #  katta tarafdagning ichda kichik tarafning barcha elementlari bo'lsa True qaytaradi.
#
# # print(result)
# # print(result1)
#
#
# son3 = {1, 2, 3, 4, 5}
# son4 = {12, 23, 34, 11, 43}
# result_is = son3.isdisjoint(son4)   # to'plam elementlari kesishmasa True qaytaradi
# print(result_is)
#
# result_iss = son3.issubset(son4)
# print(result_iss)


#   1  Bo‘sh bir to‘plam yarating va unga 4 ta raqam qo‘shing (add ishlatib).
# sonlar = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
# print(sonlar)
# sonlar.remove(1)
# sonlar.remove(4)
# sonlar.remove(6)
# print(sonlar)
# sonlar.pop()
# sonlar.pop()
# print(sonlar)
#
# sonlar.add(23)
# sonlar.add(34)
# sonlar.add(39)
# sonlar.add(48)
# print(sonlar)


# #  2  Ikki to‘plamni ({1, 2, 3} va {3, 4, 5}) kesishmasini (common elements) toping.
# son1 = {1, 3, 4, 2, 6, 7, 9, 12, 54, 23}
# son2 = {23, 34, 56, 67, 87, 1, 4, 7, 9, 21, 2}
# son3 = set(list(son2) + list(son1))
#
# print(son3)
#
# kesishma = len(son1) + len(son2) - len(son3)
# print(f"Ikki setning kesishmasi {kesishma} ga teng")


#
# #  3  To‘plamdan ({10, 20, 30, 20, 10}) takrorlanuvchi elementlarni avtomatik o‘chirib, natijani chop eting.
# sonlar = [1, 2, 4, 1, 2, 5, 7, 4, 6, 8, 9, 3, 4, 12, 1, 2, 3, 4, 5, 6]
# print(sonlar)
# set_sonlar = set(sonlar)
# print(set_sonlar)



# #   4   Ikki to‘plamni ({1, 2, 3} va {4, 5, 6}) birlashtirib, yangi to‘plam yarating.
# son1 = {1, 2, 3, 4, 5, 6}
# son2 = {7, 8, 9, 10, 11, 12, 13}
# set_sonlar = set(list(son1) + list(son2))
# print(set_sonlar)
# print(type(set_sonlar))



# #  5   To‘plamda ({1, 2, 3, 4, 5}) 3 raqamining borligini tekshiring.
# sonlar = {1, 2, 3, 4, 5, 6, 7, 8}
# len_1 = len(sonlar)
# son = int(input("Son kiriting to'plamda bo'lsa 0, bo'lmasa 1 : "))
# sonlar.add(son)
#
# print(f"Javob : {len(sonlar) - len_1 }")


# #   6.  Foydalanuvchidan 6 ta so‘z olib, ularni to‘plamga joylashtirib, takrorlanishni oldini oling.
# soz1 = input("So'z kiriting: ")
# soz2 = input("So'z kiriting: ")
# soz3 = input("So'z kiriting: ")
# soz4 = input("So'z kiriting: ")
# soz5 = input("So'z kiriting: ")
# soz6 = input("So'z kiriting: ")
#
# sozlar = {soz1, soz2, soz3, soz4, soz5, soz6}
#
# print(sozlar)



# #   7   Ikki to‘plamning ({1, 2, 3, 4} va {3, 4, 5, 6}) farqini (faqat birinchi to‘plamga xos elementlar) toping.
# set1= {1, 2, 3, 4}
# set2 = {3, 4, 5, 6}
# result = set1 - set2
# print(result)









































#   Python Dictionaries (Lug‘atlar)
#
# Nima? Lug‘atlar kalit-qiymat (key-value) juftliklaridan iborat tartibsiz to‘plamdir. Jingalak qavs { } ishlatiladi, lekin kalit va qiymatlar ikkiga bo‘linadi (key: value).
# Xususiyatlari:
#
# Kalitlar noyob bo‘lishi kerak, qiymatlar esa o‘zgartirilishi mumkin.
# Indeks emas, kalit orqali murojaat qilinadi.
#
#
# Misol:
# pythonmevalar = {'olma': 5, 'anor': 3}  # Kalit:qiymat
# mevalar['nok'] = 2  # Yangi juftlik qo'shish
# print(mevalar)  # Natija: {'olma': 5, 'anor': 3, 'nok': 2}
#
# Qachon ishlatish? Ma’lumotlarni kalitlar orqali bog‘lab saqlash kerak bo‘lganda (masalan, ism va yoshni bog‘lash).




# d = {'key1', 'key2', 'key3'}
# result_d = dict.fromkeys(d)
# print(result_d)
#
#
# x = {'key1', 'key2', 'key3' }
# y = 1, 2, 3, 4, 5
# result_dict = dict.fromkeys(x, y)
# print(result_dict)
#
#
# cars = {
#     'name' : "Malibu",
#     'prabek' : "200000",
#     "model" : "chevralet",
#     'year' : "2020"
#
# }
# car = cars.get('name')
# print(car)
#
# car_standart = cars.get('prabek', '50000')
# car_standart1 = cars.get("petno", 0)   #  petno kaliti mavjud bo'lmasa standart qiymat berishga yordam beradi.
# print(car_standart)
# print(car_standart1)
#
# cars['year'] = '2024'
# x = cars.items()
# print(x)
#
#
# print(cars.keys())
#
# del_v = cars.pop("year")
# print(del_v, "  ", cars)
#
# del_pop = cars.popitem()
# print(del_pop, cars)


#     Bo‘sh bir lug‘at yarating va unga 3 ta kalit-qiymat juftligini qo‘shing (masalan, ism: yosh).
inson = {
    'name' : "Asomiddin",
    'lastname' : "Abduqahharov",
    'age' : 20,
    'year' : 2005
}

print(inson)


# #  Lug‘atdan ({'olma': 5, 'anor': 3}) ‘olma’ kalitiga mos qiymatni chop eting.
# meva = {
#     'olma' : 4,
#     'olcha' : 9,
#     "anor" : 12,
#     'apilsin' : 3
# }
# savol = input("Mevani kiriting: ")
# result = meva.get(savol)
# print(result)


# #   Lug‘atga ({'a': 1, 'b': 2}) yangi kalit-qiymat juftligini qo‘shing va yangi qiymatni yangilang
# sonlar = {
#     'w' : 1,
#     'b' : 2,
#     'a' : 3,
#     'd' : 4
# }
#
# sonlar.update({'a' : 12})
# sonlar.update({'v' : 23})
# print(sonlar)

# #  Lug‘atdagi ({'x': 10, 'y': 20, 'z': 30}) barcha kalitlarni ro‘yxat sifatida oling.
#
# sonlar = {
#     'w' : 1,
#     'b' : 2,
#     'a' : 3,
#     'd' : 4
# }
#
# sonlar_list = list(sonlar.keys())
# print(sonlar_list)
#
#
#
# #   Lug‘atdan ({'olma': 5, 'anor': 3}) ‘anor’ kalitini o‘chirib tashlang.
# mevalar = {
#     'olma' : 5,
#     'anor' : 12,
#     'olcha' : 23,
#     'ananas' : 32
# }
#
# savol = input("Qaysi mevani olib tashlamoqchisiz: ")
# result = mevalar.pop(savol)
# print(result, '  ',  mevalar)



# #   Foydalanuvchidan 2 ta ism va yoshini so‘rab, ularni lug‘at sifatida saqlang.
# ism1 = input("1-ismni kiriting: ")
# ism2 = input('2-ismni kiriting: ')
# year1 = int(input(f"{ism1} ni yoshni kiriting: "))
# year2 = int(input(f"{ism2} ni yoshni kiriting: "))
#
# malumot = {}
# malumot['name1'] = ism1
# malumot['name2'] = ism2
# malumot['age1'] = year1
# malumot['age2'] = year2
# print(malumot)



#  Lug‘atdagi ({'a': 1, 'b': 2, 'c': 1}) qiymatlar yig‘indisini hisoblang.
sonlar = {
    'a' : 5,
    'b' : 2,
    'c' : 3,
    'd' : 4
}

list_sonlar = list(sonlar.values())
yig = sum(list_sonlar)
print(f"Qiymatlar yig'indisi: {yig}")
























































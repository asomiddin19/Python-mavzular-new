#  1  student nomli lug‘at yarating va unga quyidagi ma'lumotlarni kiriting:

student = {
    'firstname' : 'Asomiddin',
    'lastname' : 'abduqahharov',
    'age' : 20,
    'birthday' : 2005,
    'adress' : 'bandixon',
    'kurs' : 3
}

#print(f"Talaba {student['firstname'].title()} {student['lastname'].title()} {student['birthday']} - yilda {student['adress']}da tug'ilgan.")



#  2 ug‘atga yangi element qo‘shish
# Yuqoridagi student lug‘atiga "universitet": "TATU" kalit-so'zini qo‘shing.

student['unver'] = 'TATU'
#print(student)


#  3. Lug‘atdan qiymat olish
# student lug‘atidan "ism" qiymatini chop eting.
#print(student['firstname'])


#  4. Lug‘atda elementni o‘zgartirish
# student lug‘atidagi "yosh" qiymatini 23 ga o‘zgartiring.
student['birthday'] = 2002
student['age'] = 23
#print(student)



#   5. Lug‘atdan elementni o‘chirish
# student lug‘atidan "kurs" kalit-so‘zini o‘chirib tashlang.
# print(student)
# del student['kurs']
# print(student)



#  6. in operatori bilan tekshirish
# student lug‘atida "familiya" kaliti borligini tekshiring.
# savol = input("Lug'atdagi kalitso'zni kiriting: ")
# if savol.lower() in student.keys():
#     print(student.get(savol))
# else:
#     print(f"{savol} kalit so'zi lug'atning ichida mavjudemas!")










#  7. .get() metodidan foydalanish
# .get() metodi yordamida "ism" va "manzil" kalitlarini xavfsiz tarzda oling.
# firstname = student.get('firstname', 'mavjud emas!')
# adress = student.get('adress', 'mavjud emas!')
# student.update({'baxo' : 5})
# print(firstname, adress)
# print(student)




#  8. Bo‘sh lug‘at yaratish
# mahsulotlar nomli bo‘sh lug‘at yarating.
mahsulotlar = {

 }


#  9. for yordamida lug‘at elementlarini chiqarish
# student lug‘atining barcha kalit va qiymatlarini for sikli yordamida chiqaring.'

# for key, qiymat in student.items() :
#     print("Kalit : ", key)
#     print("Qiymat : ", qiymat)
#


#  10. Lug‘atni uzunligini topish
# student lug‘atidagi elementlar sonini toping.
uzunlik = len(student)
# print(f"Student lug'atida {uzunlik} ta element bor.")
# print(student)




#  11. Qiymatlar bo‘yicha filterlash
# Quyidagi lug‘atdan qiymati 50 dan katta bo‘lgan mahsulotlarni toping:


narxlar = {
    "olma": 45,
    "banan": 60,
    "anor": 55,
    "uzum": 40,
    "shaftoli": 70,
    "nok": 50,
    "gilos": 30,
    "behi": 65,
    "limon": 35,
    "apelsin": 75,
    "mandarin": 68,
    "kivi": 90,
    "qulupnay": 25,
    "smorodina": 35,
    "hurmo": 60
}

# for key , qiymat in narxlar.items() :
#     if qiymat > 50 :
#         print(f"{key.title()}ning narxi {qiymat} ga teng.")



#  12. Ikkita lug‘atni birlashtirish
# Ikkita lug‘atni birlashtiring:

narxlar1 = {
    "olma": 45,
    "banan": 60,
    "anor": 55,
    "uzum": 40
}

narxlar2 = {
    "asal": 35,
    "kartoshka": 70,
    "anjir": 45,
    "sabzi": 30,
    'olcha' : 35,
    "olxo'ri" : 80
}


# for key, qiymat in narxlar1.items() :
#     narxlar2[key] = qiymat
# print(narxlar2)


# narxlar1.update(narxlar2)
# print(narxlar1)




#   13. Qiymatlar ro‘yxati bo‘lgan lug‘at
# Quyidagi ko‘rinishda lug‘at yarating:

sinflar = {
    'sinf1' : ['alisher', 'abror', 'said', 'fozil', 'komil', 'sherzod'],
    'sinf2' : ['salim', 'akmal', 'sarvinoz', 'komil', 'jamshid', 'jaloliddin'],
    'sinf3' : ['davron', 'hakim', 'lobar', 'qobil', 'anvar', 'shokir', 'begzod'],
    'sinf4' : ['elbek', 'amir', 'abdulloh', 'jafar', 'elmurod', 'hojimurod', 'dilmurod']
}

# for sinf, talabalar in sinflar.items() :
#     # print('\n',sinf.title())
#     # for name in talabalar :
#     #     print(name.title())



#  14. Lug‘at ichida lug‘at
# Talabalar haqidagi lug‘at yarating:

students = {
    'ali': {'lastname': 'anvarov', 'age': 20, 'kurs': 2, 'adress': 'termiz'},
    'sobir': {'lastname': 'fozilov', 'age': 23, 'kurs': 2, 'adress': 'angor'},
    'anvar': {'lastname': 'komilov', 'age': 21, 'kurs': 2, 'adress': 'bandixon'},
    'davron': {'lastname': 'Normuminov', 'age': 25, 'kurs': 2, 'adress': 'boysun'}
}

# for key, qiymat in students.items() :
#     print(key, qiymat)


#   15. .values() va .keys() metodlari
# student lug‘atidagi barcha qiymatlar va kalitlarni alohida chiqarib bering.
# print('Kalitlar : ', student.keys())
# print('Qiymatlar: ', student.values())



#  16. Qiymatni o‘zgartirib, qayta saqlash
# student lug‘atida "yosh" ni 1 yilga oshirib, yangilab saqlang.
# print(student)
# yosh = student.get('age') + 1
# student['age'] = yosh
# print(student)


#   17. Foydalanuvchidan ma’lumot olib lug‘atga joylash
# Foydalanuvchidan ism, yosh, va manzil so‘rab, user lug‘atiga joylang.
# user = {
#
# }
#
# firstname = input("ism: ")
# lastname = input("familya: ")
# age = int(input('yosh: '))
# adress = input('manzil: ')
# user['firstname'] = firstname
# user['lastname'] = lastname
# user['age'] = age
# user['adress'] = adress
# print(user)



# user = {
#     'firstname' : input('ism: '),
#     'lastname' : input('familya: '),
#     'age' : int(input('yosh: ')),
#     'adress' : input('manzil: ')
# }
# print(user)


#  18. Qiymatlar ustida hisob-kitob
# Quyidagi lug‘atda barcha qiymatlar yig‘indisini toping:
ballar = {
    "matematika": 89,
    "fizika": 75,
    "informatika": 92,
    'kimyo' : 68,
    'ona-tili' : 85,
    'ingliz tili' : 73
}
yigindi = sum(ballar.values())
# print(yigindi)


#   19. Lug‘atni ro‘yxatga aylantirish
# Lug‘atdagi barcha kalitlarni ro‘yxat ko‘rinishida oling:
# list_student = list(student.keys())
# print(list_student)



#  20. Lug‘atlar ro‘yxatini yaratish
# 3 nafar talabani aks ettiruvchi lug‘atlar ro‘yxatini tuzing:

talabalar = [
    {'lastname': 'anvarov', 'age': 20, 'kurs': 2, 'adress': 'termiz'},
    {'lastname': 'fozilov', 'age': 23, 'kurs': 2, 'adress': 'angor'},
    {'lastname': 'komilov', 'age': 21, 'kurs': 2, 'adress': 'bandixon'},
    {'lastname': 'Normuminov', 'age': 25, 'kurs': 2, 'adress': 'boysun'}
]
# for i in talabalar:
#     for d, g in i.items() :
#         print(d, g)






















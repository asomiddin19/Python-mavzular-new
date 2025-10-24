
# *args USULI
# Agar funksiya qabul qiladigan parametrlar soni noaniq bo'lsa, va parametrlar yagona qiymatlar ko'rinishida uzatilsa,
# funksiya yaratishda argumentdan avval yulduzcha qo'yiladi (*arguments).



# def summa(*sonlar) :
#     yig = 0
#     for son in sonlar :
#         yig += son
#     return yig
# print(summa(1, 23, 5, 45))
# yig = summa(12, 23, 45, 32, 23)
# print(yig)



def summa(x, y, *sonlar) :
    yig = 0
    for son in sonlar :
        yig += son
    return x + y + yig

# print(summa(12, 2, 5, 6,8))
# print(summa(23, 12, 2))



def avto_qay(kompaniya, model, **malumotlar) :
    malumotlar['kompaniya'] = kompaniya
    malumotlar['model'] = model
    return malumotlar

avto1 = avto_qay('chevrolet', 'malibu', year = 2021, price = 23000, turi = 'mexanika')
avto2 = avto_qay('chevrolet' , 'nexia', year = 2023, price = 5000, turi = 'mexanika')
avto3 = avto_qay('chevrolet' , 'nexia', year = 2023, price = 5000, turi = 'mexanika')
avto4 = avto_qay('chevrolet' , 'nexia', year = 2023)
avto5 = avto_qay('chevrolet' , 'nexia', year = 2023)
cars = [avto1, avto2, avto3, avto4, avto5]

# for car in cars:
#     print(f"{car['kompaniya']} {car['model']} {car['year']} narxi: {car.get('price', 'Nomalum')}")





#   Istalgancha sonlarni qabul qilib, ularning ko'paytmasini qaytaruvchi funksiya yozing
def kop_number(*numbers) :
    kop_yig = 1
    for son in numbers :
        kop_yig *= son
    return kop_yig



# print(kop_number(2, 3, 1, 2, 4,))
# print(kop_number(1, 2, 3, 4, 5))


# Talabalar haqidagi ma'lumotlarini lug'at ko'rinishida qaytaruvchi funkisya yozing.
# Talabaning ismi va familiyasi majburiy argument, qolgan ma'lumotlar esa ixtiyoriy
# ko'rinishda istalgancha berilishi mumkin bo'lsin.

def malumot(firstname, lastname, **datas) :
    datas['firstname'] = firstname
    datas['lastname'] = lastname
    return datas

student1 = malumot('asomiddin', 'abduqahharov', year = 2005, age = 20, cours = 3)
student2 = malumot('Qosim', 'Samarov', year = 2005, age = 20, cours = 1)
student3 = malumot('Akmal', 'alimov', year = 2005, age = 20, cours = 2)
student4 = malumot('Shavkat', 'Sayfiyev', year = 2005, age = 20, cours = 4)





#  Eng kichik sonni topadigan funksiya yozing.
def kichik_son(*numbers) :
    if not numbers :
        print("Malumot kiritilmadi!")
    result = max(numbers)
    return result

# print(kichik_son(1, 4, 2, 5, 13, 32, 11, 8, 23))


# Kiritilgan sonlarning o‘rtachasini hisoblaydigan funksiya yozing.
def orta(*numbers) :
    if not numbers :
        return 'malumot yo\'q'
    else:
        yig = sum(numbers)
        arfme = yig /(len(numbers))
        return arfme


# print(orta(1, 2, 3, 4, 5, 6, 7, 8))
# print(orta(1, 2))
# print(orta())



#  Istalgancha matn qabul qilib, hammasini katta harfga o‘tkazib qaytaradigan funksiya yozing.
def matn_big(*text) :
    result = []
    for soz in text :
        result.append(soz.upper())
    return " ".join(result)

# print(matn_big("Assalomu alaykum men asomiddin man", "salom men sen ", 'lasas dsda'))


#  Matnlarni qabul qilib, uzunroq bo‘lganini qaytaradigan funksiya yozing.
def qaytar(*matnlar) :
    result = max(matnlar, key = len )
    return result

# print(qaytar('salom', 'men', 'kimning', 'qolda', 'fe', 'int', 'hamma'))
# print(qaytar('salom', 'kam', 'limon', 'albatta', 'kelmoqchi'))



#  Sonlarni qabul qilib, faqat juftlarini ro‘yxat qilib qaytaradigan funksiya yozing.
def juft_son(*numbers) :
    jufts = []
    for son in numbers :
        if son % 2 == 0 :
            jufts.append(son)
    return jufts

# print(juft_son(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 9, 10, 11, 12, 13, 14, 15, 16))




# Sonlarni qabul qilib, faqat toqlarini qaytaradigan funksiya yozing.

def toq_qay(*numbers) :
    toqs = []
    for son in numbers :
        if son % 2 == 1 :
            toqs.append(son)
    return toqs


# print(toq_qay(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 9, 10, 11, 12, 13, 14, 15, 16))

#  Sonlarni qabul qilib, ularni kvadratlarini ro‘yxat qilib qaytaradigan funksiya yozing.
def kv_qay(*numbers) :
    kv_list = []
    for son in numbers :
        kv_list.append(son ** 2)
    return kv_list

# print(kv_qay(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 9, 10, 11, 12, 13, 14, 15, 16))


#  Talaba haqida ma’lumot chiqaradigan funksiya yozing (ism, familiya, yosh, kurs).


def data_student(firstname, lastname, age, **datas) :
    datas['firstname'] = firstname
    datas['lastname'] = lastname
    datas['age'] = age
    return f"Talaba: {datas['firstname']} {datas['lastname']} yoshi {datas['age']} da "

# print(data_student('asomiddin', 'abduqahharov', 20, adress = 'termiz', cours = 3, fakultet = 'axborot'))

def data_st(**datas) :

    for kalit, qiymat in datas.items() :
        print(f"{kalit.title()} : {qiymat}.")


# print(data_st(lastname = 'abduqahharov', firstname = 'asomiddin', age = 20, cours = 3, year = 2005))


#  Mashina haqida ma’lumot chiqaradigan funksiya yozing (model, rang, yil, narx).
def cars_data(**datas) :
    result = "Mashinalar haqda malumotlar:\n"
    for key, value in datas.items() :
        result += f"Kalit: {key.title()}. Qiymat: {value}.\n"
    return result

# print(cars_data(kompaniya = 'GM', model = 'malibu', year = 2025, km = 2000, price = 25000))



# *args orqali har xil qiymatlar kiritilsin, **kwargs orqali "faqat_sonlar=True"
# yoki "faqat_matn=True" bo‘lsa, mos ravishda faqat son yoki faqat matnlarni ajratib qaytaradigan funksiya yozing.































































































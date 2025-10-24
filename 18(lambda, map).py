

uzunlik = lambda r, pi : 2 * pi * r
# print(uzunlik(6, 3.14))

# kvadrat = lambda son : son ** 2
# print(kvadrat(8)


# daraja = lambda asos, daraja : asos ** daraja
# print(daraja(3, 4))
# print(daraja(5, 2))
# print(daraja(7, 3))


def daraja(n) :
    return lambda number : number ** n

kvadrat = daraja(2)
# print(kvadrat(4))
# print(kvadrat(8))

# kub = daraja(3)
# print(kub(5))
# print(kub(9))
# print(daraja(3)(2))



from math import sqrt

sonlar = list(range(1, 30))
kvadrat_ildiz = list(map(sqrt, sonlar))
# print(kvadrat_ildiz)

# numbers = list(range(1, 100))
# ildiz = list(map(sqrt, numbers))

# def ildiz(number) :
#     if 0 <= number :
#         return sqrt(number)
#     else:
#         return "Xato xabar!"

# savol = int(input("Son kiriting: "))
# result = ildiz(savol)
# print(f"Siz kiritgan son {savol} ga teng uning ildizi: {result} ga teng!")

# def daraja2(number) :
#     return number * number

# sonlar = list(range(1, 10))
# kvadrat_list = list(map(daraja2, sonlar))
# print(kvadrat_list)

# lambda_list = list(map(lambda a : a * a, sonlar))
# print(lambda_list

# numbers1 = [1, 2, 4, 8, 5, 12]
# numbers2 = [4, 3, 6, 7, 8, 10]
# yig_list = list(map(lambda x, y : x + y, numbers1, numbers2))
# print(yig_list)



#  Sonlar ro‘yxatidagi hamma sonlarni 2 ga bo‘lish.
# numbers1 = list(range(1, 20))
# ikki_bol = list(map(lambda a : a / 2, numbers1))
# print(ikki_bol)


# Sonlar ro‘yxatidagi har bir elementni 10 ga qo‘shish
# qosh = list(map(lambda a: a + 10, numbers1))
# print(qosh)



#  Berilgan ro‘yxatdan har bir sonning manfiy qiymatini olish.
# manfiy_list = list(map(lambda a : -1 * a, numbers1))
# print(manfiy_list)


#  Sonlar ro‘yxatidagi har bir elementni stringga aylantirish.
# str_sonlar = list(map(lambda a : str(a), numbers1))
# print(str_sonlar)



import random
sonlar1 = random.sample(range(1, 200), 15)
# print(sonlar1)
def juftmi(a) :
    return a % 2 == 0

# print(juftmi(12))
# print(juftmi(11))

juft_list = list(filter(juftmi, sonlar1))
# print(juft_list)

def toq_son(b) :
    return b % 2 == 1

toq_list = list(filter(toq_son, sonlar1))
# print(toq_list)





numbers1 = random.sample(range(200), 30)
# print(numbers1)
juft_sonlar = list(filter(lambda son: son % 2 == 0, numbers1))
toq_sonlar = list(filter(lambda son: son % 2 == 1, numbers1))
# print(juft_sonlar)
# print(toq_sonlar)


mevalar = ['olma', 'anor', 'shaftoli', 'suv', 'olcha', 'somsa', 'daraxt', 'orol', 'pamidor', 'qovun', 'shakar', 'tarvuz', "olx'ri", 'oyoq']
harf = 'o'
sozlar = list(filter(lambda soz : soz.startswith(harf), mevalar))
# print(sozlar)


sozlar_len = list(filter(lambda soz: len(soz) > 5, mevalar))
# print(mevalar)
# print(sozlar_len)


































#  Matnlar ro‘yxatidagi har bir elementni kattalashtirish (upper()).
matn = ['olma', 'anor', 'savat', 'somsa', 'kiyim', 'kepka', 'daraxt', 'qovun', 'dars']
matn_list = list(map(lambda soz : soz.upper(), matn))
# print(matn_list)


#  Matnlar ro‘yxatidagi har bir elementni kichraytirish (lower()).
sozlar = ['OLMA', 'ANOR', 'SAVAT', 'SOMSA', 'KIYIM', 'KEPKA', 'DARAXT', 'QOVUN', 'DARS']
kich_soz = list(map(lambda soz : soz.lower(), sozlar))
# print(kich_soz)


#  Matnlar ro‘yxatidan har bir elementning birinchi harfini olish.
element = ['olma', 'anor', 'savat', 'somsa', 'kiyim', 'kepka', 'daraxt', 'qovun', 'dars']
harflar = list(map(lambda soz: soz[0], element))
# print(harflar)



#  Matnlar ro‘yxatidan har bir elementning oxirgi harfini olish.
oxrgi_harf = list(map(lambda soz: soz[-1], element))
# print(oxrgi_harf)




#  Sonlar ro‘yxatidan juft sonlar ro‘yxatini yasash (map bilan True/False tekshirish).
# numbers = list(range(1, 20))
# qiymat = list(map(lambda son: son % 2 == 0, numbers ))
# print(qiymat)



#  Sonlar ro‘yxatidan toqlarni aniqlash (x % 2 != 0).















































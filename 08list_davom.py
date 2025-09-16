

# cars = ['nexia', 'malibu', 'bmw', 'audio', 'gentra', 'damas', 'matiz', 'jentra', 'captiva', 'gelik']
# print(cars)
# cars.sort()   # sort method ro'yhat elementlarni alifbo tartibida taxlab beradi.
# print(cars)
#
#
# cars.sort(reverse=True)   #  Alifboga teskari tartiblab beradi (reverse - teskari).
# print(cars)
# print(sorted(cars))  #  bu method yani sorted da asil ro'yhat o'zgarmay qoladi.
# print(cars)
#
# print(sorted(cars, reverse=True))
# print(cars)
#
#
# cars.reverse()    # reverse() method yordamida ro'yhatni teskari qilsak bo'ladi.
# print(cars)
# cars_len = len(cars)
# print(cars_len)
#
#
#
# sonlar = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
# sonlar.reverse()
# print(sonlar)
#
#
# uzunlik = len(sonlar)
# print(uzunlik)
#

#
# numbers = list(range(1, 20))
# print(numbers)
#
#
# toq_sonlar = list(range(1, 30, 2))
# print(toq_sonlar)
#
#
# juft_sonlar = list(range(0, 40, 2))
# print(juft_sonlar)
#
#
# max_qiy = max(juft_sonlar)
# print(max_qiy)
#
# min_qiy = min(juft_sonlar)
# print(min_qiy)
#
# narxlar = [1200, 2300, 3000, 4200, 8200, 4100, 1700, 3500, 2500, 4600]
# arzon = min(narxlar)
# qimmat = max(narxlar)
# yigindi = sum(narxlar)
#
#
# print(f"Siz olgan maxsulotlar ichda eng arzoni: \n{arzon} so'm, eng qimmati: {qimmat} so'm va jammi summa: {yigindi} so'm.")



# car_s = ['bmw', 'damas', 'ki', 'audio', 'cherry', 'audio', 'mers', 'gentra', 'bwd', 'nexia']
# print(car_s[0:3])    # 0-indexdan boshlab 3-indexgacha oladi (yaniy 3-index olinmaydi.)
# print(car_s)
#
#
# print(car_s[:2])   #  brinchi index berilmagan holatda 0-indexdan boshlab ketadi.
# print(car_s[3:])    # oxirgi index berilmagan holatda oxirigacha chiqarad.
#
#
# my_cars = car_s      #  Bu yo'l bilan kopy qilmoqchi bo'lih xato sababi bunda bitta ro'yhat shakklanadi va ikki nom ostida bitta ro'yhat .
# print(my_cars)
# print(car_s)
#
# my_cars.remove("bmw")
# my_cars.remove('nexia')
# print(my_cars)
# print(car_s)

#  my_cars = car_s      #  Bu yo'l bilan kopy qilmoqchi bo'lih xato sababi bunda bitta ro'yhat shakklanadi va ikki nom ostida bitta ro'yhat .
#  To'g'ri usul my_cars = car_s[ : ]  bunda ro'yhatning boshidan oxrigacha copy qilib beradi.


# buyumlar = ['kosa', 'piyola', 'qoshiq', 'finjon', 'tareka', "cho'mich", 'pichoq']
#
# k_buyum = buyumlar[:]
#
# buyumlar.append("bonka")
# buyumlar.append("istakan")
#
# k_buyum.remove("cho'mich")
# k_buyum.remove("kosa")
#
# print(buyumlar)
# print(k_buyum)




#   TUPLES   --->>>  O'zgarmas ro'yxat.

# cars = ('bmw', 'audio', 'mers', 'damas', 'fura', 'kamaz', 'captiva', 'malibu')
# print(cars)

#     cars.appned("jipp")  tuples ga element qo'shib bo'lmaydi.
#     cars[1] = 'jipp'   bu usul ham ishlamaydi o'zgarmas ro'yhatda (tuples)
#      cars.remove("bmw")  bundan ham foydalana olmaymiz.
# del cars[1]  xato beradi.
# print(cars)

# #  tuple ni o'zgartrishning yo'li list ga o'tqazish.
# print(type(cars))  # Natija: tuple
# list_cars = list(cars)
# print(type(list_cars))    #  Natija: list
#
#
# # list_cars.remove('bmw')
# # list_cars.remove('mers')
# print(list_cars)
#
# list_cars.append("jipp")
# list_cars.append("gelik")
# print(list_cars)
# print(cars)
# cars = tuple(list_cars)
# print(cars)
# print(sorted(cars))   #   sorted()  Har qanday iterable (tuple, list, set) bilan ishlaydi.
# copy_cars = cars[:]
# cars_k = cars[1:4]
# print(copy_cars)
# print(cars_k)




# sonlar = (9, 3, 7, 1, 4, 8, 12, 34, 11, 83, 24, 31, 38)
# print(type(sonlar))
# print(sonlar)
# tuple_son  = tuple(sorted(sonlar))
# print(tuple_son)
# print(type(sonlar))



#  AMALYOT

# #   O'zingizga ma'lum davlatlarning ro'yxatini tuzing va ro'yxatni konsolga chiqaring
# davlatlar = ["O'zbekiston", "AQSH", "Anglya", "Qozog'iston", "Hindiston", 'Meksika', 'Italiya', "Qirg'iziston", 'Arabiston', "Ummon", "Ispaniya"]
# print(davlatlar)
# davlatlar.reverse()   #  reverse orqali teskari qilishimiz mumkun.
# print(davlatlar)
#
#
#
# #   Ro'yxatning uzunligini konsolga chiqaring
# #   Ro'yxatning uzunligi, ya'ni uning ichidagi elementlar sonini aniqlash uchun len() funktsiyasidan foydalanamiz:
# print(f"Siz bergan davlatlar ro'yxatida {len(davlatlar)} ta davlat bor.")
#
#
# #    sorted() funktsiyasi yordamida ro'yxatni tartiblangan holda konsolga chiqaring
# print(sorted(davlatlar))
#
# #  sorted() yordamida ro'yxatni teskari tartibda konsolga chiqaring
# print(sorted(davlatlar, reverse=True))
#
#
# #  Asl ro'yxatni qaytadan konsolga chiqaring
# davlatlar.reverse()
# print(davlatlar)
#
#
#
# #
# # sort() metodi yordamida ro'yxatni avval alifbo bo'yicha, keyin esa alifboga teskari tartibda konsolga chiqaring
#
# davlatlar.sort()
# print(davlatlar)
# print(sorted(davlatlar, reverse=True))



# #   120 dan 1200 gacha bo'lgan juft sonlar ro'yxatini tuzing
# juft_sonlar = list(range(120, 1200, 2))
# print(juft_sonlar)
#
#
# #  Ro'yxatdagi sonlar yig'indisini hisoblang va konsolga chiqaring
# yigindi = sum(juft_sonlar)
# print(yigindi)
#
#
# #   Ro'yxatdagi eng katta va eng kichik son o'rtasidagi ayirmani hisoblang va konsolga chiqaring
# ayrma = max(juft_sonlar) - min(juft_sonlar)
# print(f"{max(juft_sonlar)} dan {min(juft_sonlar)} dan ayirmasi {ayrma} ga teng.")
#
#
#
# #   Ro'yxatdagi elementlar sonini hisoblang
# print(f"Ro'yxatda {len(juft_sonlar)} ta element bor.")
#
#
# #   Ro'yxatning boshidan, o'rtasidan va oxiridan 20 ta qiymatni konsolga chiqaring
# uzunlik1 = len(juft_sonlar[:20])
# uzunlik2 = len(juft_sonlar[260:280])
# uzunlik3 = len(juft_sonlar[520:])
# print(uzunlik1, uzunlik2, uzunlik3)
# print(f"Boshidagi 20 ta element : {juft_sonlar[:20]}"
#       f"\nO'rtadagi 20 ta element: {juft_sonlar[260:280]}"
#       f"\nOxirgi 20 ta element: {juft_sonlar[520:]}")





#   taomlar degan ro'yxat yarating va ichiga istalgan 5ta taomni kiriting
toamlar = ["osh", 'manti', 'somsa', 'gril', "go'sh"]




#    nonushta degan yangi ro'yxatga taomlardan nusxa oling
nonushta = toamlar[:]
# print(nonushta)



#    Yangi ro'yxatda faqat nonushtaga yeyiladigan taomlarni qoldiring, va qo'shimcha 2 ta taom qo'shing
nonushta.remove('manti')
nonushta.remove("gril")
del nonushta[2]
# print(nonushta)
nonushta.append("choy")
nonushta.append("cho'poncha")
nonushta.append("sho'rva")
# print(nonushta)







#    Ikkala ro'yxatni ham (taomlar va nonushta) konsolga chiqaring
# print(toamlar)
# print(nonushta)


#   Yuqoridagi nonushta ro'yxatini o'zgarmas ro'yxatga aylantiring va nonushta[0] = "qaymoq va non" deb qiymat berib ko'ring.
tuple_nonushta = tuple(nonushta)
print(type(tuple_nonushta))

nonushta = list(tuple_nonushta)
nonushta[0] = "qaymoq"
print(nonushta)
nonushta[0] = 'non'
nonushta = tuple(nonushta)
print(type(nonushta))






























































































































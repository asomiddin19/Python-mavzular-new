

# mevalar = ['olma', 'anor', 'nok', 'olcha', 'banan', 'xurmo']
# narhlar = [20000, 12000, 30000, 25000, 40000, 21000]
# sonlar = ['bir', 'ikki', 3, 4, 5, 6, 7, 8]
# ismlar = []

# print(mevalar)
# print(ismlar)

# print(mevalar[0])  # index bilan murojat qilish 0 - index brinchi elementga teng.
# print(mevalar[1])
#
# print(mevalar[-1])  # orqadan sanashda -1 index orqadagi birinchi elementni chiqarib beradi.
# print(mevalar[-6])
#
# mevalar[0] = 'anjir'   #  Olma anjirga o'zgaradi
# print(mevalar)
#
# mevalar[1] = mevalar[0]
# print(mevalar)

# mevalar[0] = mevalar[3] = mevalar[4]  # hammasi 4- indexdagi mevaga o'zgaradi.
# print(mevalar)
# mevalar[2] = mevalar[-1] =mevalar[2]
# print(mevalar)



# mevalar = ['olma', 'anor', 'nok', 'olcha', 'banan', 'xurmo', "o'rik"]
#
# # append()
# mevalar.append("olxo'ri")   # append eng oxriga qo'shib beradi
# print(mevalar)
#
# mevalar.insert(0, 'ananas')   # insert indexi bilan qo'shadi
# mevalar.insert(1, 'shaftoli')
# print(mevalar)

#
# cars = []
#
# cars.append('cobolt')
# cars.append('nexia')
# cars.append("damas")
# cars.append("matiz")
#
# print(cars)
#
# cars.insert(1,"trekker")
# print(cars)
#
# del cars[0]   # del methodi index bo'yicha o'chradi
# del cars[-1]
# print(cars)
#
# cars.append('nexia2')
# cars.append("nexia3")
# cars.insert(0, 'gentra')
# cars.insert(1, "captiva")
# print(cars)
#
#
# cars.remove('nexia2')    # remove qiymati bilan o'chrish
# cars.remove('nexia3')
# print(cars)
#
#
# hayvonlar = ['it', 'sigir', 'kuchuk', "qo'y", 'it', 'mushuk', 'echki']
# hayvonlar.remove('it')    # siz bergan elementning ro'yhat ichida birinchi kelganini o'chrib tashlaydi.
# print(hayvonlar)


#
# bozorlik = ['un', "yog'", 'tuz', 'kartoshka', 'piyoz', "lag'mon"]
# olingan = bozorlik.pop(0)   # pop() methodi shu indexdagi elementni sug'rib oladi.
# print(olingan)
# print(bozorlik)
#
# olingan1 = bozorlik.pop()   # index berilmaganda ro'yhatdagi eng oxirgi elementni oladi.
# print(olingan1)
# print(bozorlik)



# #  ismlar degan ro'yxat yarating va kamida 3 ta yaqin do'stingizning ismini kiriting
# ismlar = ["Og'abek", 'Azizbek', 'Nodirbek', "Habibullo", "Umid"]
# ismlar.append('Alisher')
# print(ismlar)
#
# ismlar.insert(1, "Hojakbar")
# print(ismlar)
#
# ismlar.remove('Umid')
# print(ismlar)
#
#
# del ismlar[1]
# print(ismlar)
#
#
# ismlar.pop()
# print(ismlar)
#
# #  Ro'yxatdagi har bir do'stingizga qisqa xabar yozib konsolga chiqaring:
# print(f"Assalomu alaykum {ismlar[0]} yaxshimisan.")
# print(f"{ismlar[1]} zo'rmisan nima gaplar.")
# print(f"Zo'rmi {ismlar[2]} nima gaplar.")


# #   sonlar deb nomlangan ro'yxat yarating va ichiga turli sonlarni yuklang (musbat, manfiy, butun, o'nlik).
# sonlar = [1, 3, 6, -2, -4, 23, 20, -23, 2.1, -8, -5.4, 8, 5, -6, -4.5]
#
#
# #  Yuqoridagi ro'yxatdagi sonlar ustida turli arifmetik amallar bajarib ko'ring.
# #  Ro'yxatdagi ba'zi sonlarning qiymatini o'zgartiring, ba'zilarini esa almashtiring.
#
# yig = sonlar[0] + sonlar[1] + sonlar[2]
# print(yig)
#
# ay = sonlar[0] - sonlar[4] - sonlar[8] - sonlar[3]
# print(ay)
#
# kop = sonlar[1] * sonlar[3] + sonlar[5] - sonlar[7]
# print(kop)
#
# sonlar[0] = sonlar[2]
# sonlar[1] = 12
# sonlar[3] = 15
# print(sonlar)
#
#
# sonlar.remove(12)
# print(sonlar)
#
# sonlar.insert(1, 23)
# print(sonlar)
#
# del sonlar[2]
# print(sonlar)
#
#
# sonlar.pop()
# sonlar.pop()
# sonlar.append(23)
# print(sonlar)



# #   t_shaxslar va z_shaxslar degan 2 ta ro'yxat yarating va biriga o'zingiz eng ko'p hurmat qilgan tarixiy shaxslarning,
# #   ikkinchisiga esa zamonamizdagi tirik bo'lgan shaxslarning ismini kiriting.
# #   Yuqoridagi ro'yxatlarning har biridan bittadan qiymatni sug'urib olib (.pop()), quyidagi ko'rinishda chiqaring:
#
# t_shaxslar = ["Imom Buxoriy", "Alisher Navoiy", "Amir Temur", "Muhammad Yusuf", "Ibn Sino"]
# z_shaxslar = ["Hamzat Chimayev", "Islam Mahachiv", "Umar Nurmagamedov", "Habib Nurmagamedov"]
#
# t_shaxs = t_shaxslar.pop()
# print(f"{t_shaxs.upper()} tibbiyot sohasiga katta rivoj qo'shgan inson bo'ladi.")
#
# z_shaxs = z_shaxslar.pop()
# print(f"{z_shaxs} chechinistonlik ufc jangchsi haqiqiy erkak.")
#



#  friends nomli bo'sh ro'yxat tuzing va unga .append()
#  yordamida 5-6 ta mehmonga chaqirmoqchi bo'lgan do'stlaringizni kiriting.

friends = []
friends.append("Og'abek")
friends.append("Umid")
friends.append("Sanjar")
friends.append("Akmal")
friends.append("Shuxrat")
friends.append("Sardor")
friends.append("Salim")
friends.append("Anvar")
print(friends)

#   Yuqoridagi ro'yxatdan mehmonga kela olmaydigan odamlarni .remove() metodi yordamida o'chrib tashlang.
friends.remove("Umid")
friends.remove("Akmal")
friends.remove("Shuxrat")

del friends[1]
del friends[2]
print(friends)


#  Ro'yxatning oxiriga, boshiga va o'rtasiga yangi ismlar qo'shing
friends.insert(0, "Asomiddin")
friends.insert(2, "Jamshid")
friends.insert(-1, "Davron")
print(friends)



# Yangi mehmonlardeb nomlangan bo'sh ro'yxat yarating. .pop() va .append() metodlari yordamida
# mehmonga kelgan do'stlaringizning ismini friends ro'yxatidan sug'urib olib, mehmonlar ro'yxatiga qo'shing.

mehmonlar = []
mehmonlar.append(friends.pop(1))
mehmonlar.append(friends.pop(2))
mehmonlar.append(friends.pop(3))
mehmonlar.append(friends.pop(0))
print(friends)
print(mehmonlar)















































































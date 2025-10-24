#  1 dan 10 gacha bo‘lgan sonlarni while yordamida ekranga chiqaring.
# number = 1
# while number <= 10 :
#     print(number)
#     number += 1


#  10 dan 1 gacha bo‘lgan sonlarni kamayib chiqaring.
# number = 10
# while number != 0 :
#     print(number)
#     number -= 1



#  Foydalanuvchidan son so‘rab oling va while orqali shu sondan 0 gacha tushib boring.

# number = int(input("Butun son kiriting: "))
# while number != 0 :
#     if number > 0 :
#         print(number)
#         number -= 1
#     else:
#         print(number)
#         number += 1


#  1 dan 100 gacha bo‘lgan faqat juft sonlarni while bilan chiqaring.

# number = int(input("Son kiriting: "))
# son =  1
# while son != number :
#     if son % 2 == 0 :
#         print(son)
#     son += 1


#  5. 1 dan 50 gacha bo‘lgan toq sonlarning yig‘indisini hisoblang.
# son = int(input("Son kiriting: "))
# number = 1
# yigindi_toq = []
# while number < son :
#     if number % 2 != 0 :
#         yigindi_toq.append(number)
#     number += 1
# print(f"1 dan boshlab {max(yigindi_toq) + 1} gacha bo'lgan toq sonlar yi'gindisi sonlar yig'indsi: {sum(yigindi_toq)}")



#  6 Foydalanuvchidan matn so‘rang va while orqali harflarini bittalab chiqaring.
# matn = input("Biror bir mating kiriitng: ").upper()
# number = 0
# while  number < len(matn) :
#     print(matn[number])
#     number += 1




#  7   Matndagi belgilar sonini while yordamida sanang.
# matn = list(input("Matn kiriting: "))
# sanoq = 0
# while matn :
#     matn.pop()
#     sanoq += 1
# print(sanoq)




#  8  Berilgan matnda nechta a harfi borligini while orqali toping.
# matn = list(input("Matin kiriting: "))
# belgi = input("Yuqoridagi matinni ichidagi qaysi belgni sanamoqchisiz: ")
# belgi_son = 0
# takror = 0
# while takror < len(matn) :
#     if belgi == matn[takror] :
#         belgi_son += 1
#     takror += 1
# print(f"[{''.join(matn)}] ichida '{belgi}' {belgi_son} ta bor.")



#   9. Foydalanuvchidan parol so‘rang. To‘g‘ri parol kiritilmaguncha while davom etsin.
# parol = input("Assalomu alaykum parolni kiriting: ")
# while True :
#     if parol != "asomiddin" :
#         parol = input("Parolni qayta kiriting: ")
#     else:
#         break
# print("Parol to'g'ri.")



#  10. Foydalanuvchi “stop” deb yozmaguncha while davom etib, ism so‘rasin.
# friends = []
# while True :
#     name = input("Ism kiriting (stop) dasturni to'xtatadi.: ")
#     if name == 'stop' :
#         break
#     else:
#         friends.append(name)
#         print(f"{name} ro'yxatga qo'shildi.")
# print("Dastur to'xtadi.")
# print(friends)


#   11  Foydalanuvchi kiritgan sonning faktorialini while orqali hisoblang.
# number = int(input("Son kiriting: "))
# son = 1
# fak = 1
# while number => son :
#     fak *= son
#     son += 1
# print(fak)



# Foydalanuvchidan son kiriting, uning raqamlari yig‘indisini while yordamida toping.
# number = input("Son kiritng: ")
# jamlash = 0
# ind = 0
# while True:
#     if len(number) != ind :
#         jamlash += int(number[ind])
#         print(f"{number[ind]} qo'shildi.")
#         ind += 1
#     else:
#         break
# print(f"{number} ning raqamlari yig'indisi: {jamlash}")





# Foydalanuvchi son kiritsin. while orqali shu sonning barcha bo‘luvchilarini chiqaring.
# number = int(input("So kiriting: "))
# son = 1
# buluvchilar = []
# while son <= number :
#     if number % son == 0 :
#         buluvchilar.append(son)
#     son += 1
# print(buluvchilar)


#  1 dan foydalanuvchi kiritgan songacha bo‘lgan barcha sonlarning yig‘indisini toping (while).



















# 1 dan foydalanuvchi kiritgan songacha bo‘lgan barcha sonlarning yig‘indisini toping (while).
#
# 1 dan 100 gacha bo‘lgan sonlar orasida faqat 3 ga karralilarni while bilan chiqaring.
#
# Ro‘yxatdagi barcha elementlarni while yordamida ekranga chiqaring.
#
# Ro‘yxatdagi faqat juft sonlarni while orqali chiqarib bering.
#
# Ro‘yxatdagi elementlarning yig‘indisini while yordamida hisoblang.
#
# Ro‘yxatda nechta manfiy son borligini while orqali aniqlang.
#
# Ro‘yxatdagi eng katta elementni while orqali toping.
#
# Lug‘atdagi barcha kalit:qiymat juftliklarini while yordamida chiqaring.
#
# Lug‘atdagi kalitlarni bittalab while orqali chiqarib bering.
#
# Lug‘atda berilgan kalitni topmaguncha foydalanuvchidan so‘raydigan dastur tuzing (while).
#
# Lug‘atdagi qiymatlarning umumiy yig‘indisini while orqali hisoblang (agar son bo‘lsa).
#
# Lug‘atdagi eng katta qiymatni while yordamida aniqlang.






























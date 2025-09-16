# mehmonlar = ['asomiddin', 'alisher', 'abdulloh', 'amirxon', 'farxod', 'komil', 'akbar', 'sardor']
#
# for mehmon in mehmonlar :
#     print(f"Assalomu alaykum yaxshimisiz {mehmon.title()} !")


# sonlar = list(range(1, 13))
# for son in sonlar :
#     print(f"{son} ning kvadrati {son ** 2} ga teng!")
#


# numbers = list(range(1, 21))
# numbers_kv = []
# for number in numbers :
#     numbers_kv.append(number**2)
# print(f"Sonlar to'plami : {numbers}")
# print(f"Sonlarning kvadrati : {numbers_kv}")


# friends = []
# print("Eng yaqin do'stingizni 5 tasni kiriting!")
#
#
# for friend in range(0, 5) :
#     friends.append(input(f"{friend + 1} - do'stingizni kiriting : "))
# print(friends)

#
# #   Kamida 5 elementdan iborat ismlar degan ro'yxat tuzing, va ro'yxatdagi har bir ismga takrorlanuvchi xabar yozing
# names = ['Akmal', 'alisher', 'sherzod', 'sherxon', 'komil', 'toxirxon']
# for name in names :
#     print(f"Assalomu alaykum {name.title()} yaxshimisiz!")
#


#   Yuoqirdagi tsikl tugaganidan so'ng, ekranga "Kod n marta takrorlandi" degan
#   xabarni chiqaring (n o'rniga kod necha marta takrorlanganini yozing)
#
# names = ['alisher', 'mvlon', 'akmal', 'husan', 'umar', 'abdulloh']
# for name in names :
#     print(f"Salom {name.title()}")
# print(f"Kod {len(names)} martta takrorlandi.")



# #   10 dan 100 gacha bo'lgan toq sonlar ro'yxatini tuzing. Ro'yxatning xar bir elementining kubini yangi qatordan konsolga chiqaring.
# toq_sonlar = list(range(11, 100, 2))
# kub_sonlar = []
# for son in toq_sonlar :
#     kub_sonlar.append(son ** 3)
# print(toq_sonlar)
# print(kub_sonlar)



# #  Foydalanuvchidan 5 ta eng sevimli kinolarini kiritshni so'rang, va kinolar degan ro'yxatga saqlab oling.
# #  Natijani konsolga chiqaring.
# kinolar = []
# for kino in range(5) :
#     kinolar.append(input(f"{kino + 1} - kinoni kiriting: "))
# print(kinolar)




# #    Foydalanuvchidan bugun nechta odam bilan uchrashganini (suhbatlashganini) so'rang, va
# #    har bir suhbatlashgan odamning ismini birma-bir so'rab ro'yxatga yozing. Ro'yxatni konsolga chiqaring.
#
#
# suxbat = int(input("Assalomu alaykum bugun necha kishi bilan uchrashdingiz: "))
# uchrashganlar = []
# for i in range(suxbat) :
#     uchrashganlar.append(input(f"{i + 1} - uchrashgan odamingizni kiriting: "))
# print(f"Siz bugun {suxbat} ta odam bilan uchrashgansiz. \nUchrashganlar ro'yxati : {uchrashganlar} ")




# #  1 dan N gacha sonlarni chiqarish
# # Shart: Foydalanuvchi N sonini kiritadi. 1 dan N gacha bo'lgan sonlarni chiqaring.
# son = int(input("Assalomu alaykum son kiriting: "))
# for i in range(1, son + 1) :
#     print(i)




# #  2. Sonlar yig'indisi
# # Shart: 1 dan N gacha bo'lgan sonlar yig'indisini hisoblang.
# son = int(input("Son kiriting: "))
#
# yig = 0
# for i in range(1, son+1 ):
#     yig += i
# print(yig)
#
# sonlar = list(range(1, son+1))
# yig_sonlar = sum(sonlar)
# print(yig_sonlar)


#
# #  3. Juft sonlarni chiqarish
# # Shart: 1 dan N gacha bo'lgan juft sonlarni chiqaring.
# son = int(input("Son kiriting : "))
# for i in range(2, son + 1, 2) :
#     print(i)


# #  4. Toq sonlarni chiqarish
# # Shart: 1 dan N gacha bo'lgan toq sonlarni chiqaring.
# son = int(input("Son kiriting: "))
# for i in range(1, son + 1, 2) :
#     print(i)
#



# #  5. Sonning kvadratlari
# # Shart: 1 dan N gacha bo'lgan sonlarning kvadratlarini chiqaring.
#
# son = int(input("Son kiriting : "))
# for i in range(1, son + 1) :
#     print(i ** 2)


# #  6. Sonning teskari tartibda chiqarish
# # Shart: N dan 1 gacha bo'lgan sonlarni teskari tartibda chiqaring.
# son = int(input("Son kiriting : "))
# sonlar = list(range(1, son + 1))
# sonlar.reverse()
# for i in sonlar :
#     print(i)
# son = int(input("Son kiriting : "))
# for i in range(son , 0, -1) :
#     print(i)



# #  7. 3 ga bo'linadigan sonlar
# # Shart: 1 dan N gacha 3 ga bo'linadigan sonlarni chiqaring.
#
# son = int(input("Son kiriting : "))
# for i in range(1, son + 1) :
#     if i % 3 == 0 :
#         print(i)


# #  Sonning raqamlari yig'indisi
# # Shart: Berilgan N sonining raqamlari yig'indisini toping.
# son = input("Son kiriting: ")
# son.endswith('')
# y = 0
# for i in son:
#     y += int(i)
# print(y)



# #  9. Faktorial hisoblash
# # Shart: N sonining faktorialini hisoblang (N!).
# n = int(input("Son kiriting : "))
# kop = 1
# for i in range(1, n + 1) :
#     kop *= i
# print(kop)



# # 10. Harfli yulduzcha
# # Shart: N qatorli yulduzcha piramidasini chiqaring.
# n = int(input("Son kiriting : "))
# for i in range(1, n + 1) :
#     print(i * '*')



#  Fibonachchi ketma-ketligi
# Shart: Dastlabki N ta Fibonachchi sonini chiqaring (0, 1, 1, 2, 3, 5, ...).
n = int(input("Son kiriting: "))
a = 0
b = 1
for i in range(0, n) :
    a = b
    b = a + b
    print(a)










































































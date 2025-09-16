# cars = ['audio', 'mers', 'bmw', 'jentra', 'gelik', 'ki']
# for car in cars :
#     if car == 'ki' or car == 'bmw' :
#         print(car.upper())
#     else :
#         print(car.title())
#
#
# name = input("Assalomu alaykum ismingizni kiriting: ")
# if name.lower() != 'asomiddin' :
#     print(f"Uzur {name.title()} biz Asomiddinni kirita olamiz!")
# else :
#     print('Assalomu alaykum Asomiddin xush kelibsiz!')


# savol = float(input("7*8 javobni kiriting: "))
# if savol != 42 :
#     print("Javobingiz xato!")


# age = int(input("Assalomu alaykum yoshingizni kiriting : "))
# if age < 18 :
#     print("Afsuski sizga kirish mumkin emas!")
# elif 18 <= age <= 40 :
#     print("Siz tizimga mofaqiyatli kirdingiz!")
# else :
#     print("Siz tizimga kira olmaysiz!")



# password = input("Password kiriting 5 tadan kam bo'lmagan: ")
# login = input("Login kiriting (6 ta belgi) : ")
# if len(password) < 5 or len(login) < 6 :
#     print("Kechrasiz login yoki password xato kiritildi!")
# else:
#     print("Siz tizimga samarali ro'yxatdan o'tdingiz!")
#     savol_password = input("Pasword : ")
#     savol_login = input("Login : ")
#     if savol_password == password and savol_login == login :
#         print("Tizimga kirdingiz!")
#     elif savol_login == login or savol_password == password :
#         print("Password yoki login xato!")
#     else:
#         print("Xato!")


# year = int(input("Assalomu alaykum tug'ilgan yilingizni kiriting: "))
# age = 2025 - year
# if 18 <= age :
#     print(f"Siz {age} yoshdasiz kirishingiz mumkin!")
# else :
#     print(f"Siz {age} yoshdasiz tizimga kira olmaysiz!")


# age = int(input("Yoshingizni kiriting: "))
# if age >= 18 : print(f"Siz {age} yoshdasiz. Maktabni bitirib bo'lgansiz!")


# y, x = int(input("Birinchi sonni kiriting: ")), int(input("Ikkinchi sonni kiriting: "))
# print("x > y") if x > y  else print("y > x")

# a, b = int(input("a = ")), int(input("b = "))
# print('a > b') if a > b else print('b > a')


# age = int(input("Yoshingz nechida: "))
# if age < 12 :
#     print("Kirish sizga tekin!")
# elif 18 > age :
#     print("Kirish sizga 5000 so'm!")
# else :
#     print("Kirish narxi 10000 so'm!")


# age = int(input("Yoshingiz nechida: "))
# if age < 12 :
#     narh = 0
# elif age < 18 :
#     narh = 1000
# elif age < 30 :
#     narh = 2000
# elif age < 40 :
#     narh = 3000
# else :
#     narh = 5000
# print(f"Kirish narxi {narh} so'm! ")



# day = input("Assalomu alaykum bugun nima kun : ")
# if day.lower() == 'yakshanba' or day.lower() == 'shanba' :
#     print("Bugun damolish kuni!")
# else :
#     print("Bugun ish kuni!")



# day = input("Assalomu alaykum bugun kun nima: ")
# celsi = float(input("Xarorat qanday: "))
# if day.lower() == "yakshanba" and celsi >= 35 :
#     print("Bugun dam olish kuni! Cho'milishga boramiz.")
# elif day.lower() == "yakshanba" and celsi < 35 :
#     print("Bugun yakshanba uyda dam olamiz!")
# else :
#     print("Bugun ishga boramiz!")

# narx = 20000
# choy = True
# non = True
#
# if choy and non :
#     narx += 10000
# elif choy or non :
#     narx += 3000
# print("Jami narx: ", narx)


# choy = True
# non = False
# manti = True
# somsa = False
# salat = True
# osh = False
# narx = 25000
# if salat :
#     narx += 3000
#     print("Mijoz 3000 ga salat oldi.")
# if choy :
#     narx += 2500
#     print("Mijoz 2500 ga choy oldi.")
# if non :
#     narx += 1400
#     print("Mijoz 1400 ga non oldi.")
# if manti :
#     narx += 6000
#     print("Mijoz 6000 ga manti oldi.")
# if somsa :
#     narx += 5000
#     print(f"Mijoz 5000 ga somsa oldi.")
# if osh :
#     narx += 9000
# print(f"Jami narx : {narx} so'm!")


# menu = ['somsa', 'jiz', "cho'poncha", 'salat', 'asarti', 'shashlik', 'baliq', 'manti']
# savol = input("Mijoz nima ovqat buyurtma qilasiz: ")
# if savol.lower() in menu :   #  in operatori yordamida biz ro'yxatning tarkibida ma'lum bir element borligini tekshirishimiz mumkin.

#     print(f"Siz {savol} buyurtma qildingiz!")
# else :
#     print(f"Afsuski siz buyurtma qilgan {savol} yo'q.")



#
# cars = ['mers', 'bmw', 'gelik', 'nexia', 'jentra', 'ferrari', 'sanata']
# car = input("Mashina kiriting: ")
# if car.lower() not in cars :    # not in operatori yordamida esa biror element ro'yxatda yo'qligini tekshirishimiz mumkin.
#     print(f"Ro'yxatda {car} yo'q")
# else :
#     print(f"Ro'yxatda {car} avto mobili mavjud")



# menu = ['somsa', 'jiz', "cho'poncha", 'salat', 'asarti', 'shashlik', 'baliq', 'manti', 'tort', 'shrinlik']
# buyurtma = ['qiyma', 'toviq', 'grel',"cho'poncha", 'salat', 'asarti', 'shashlik',]
# if buyurtma :
#     for buy in buyurtma :
#         if buy.lower() in menu :
#             print(f"Sizning buyurtmangiz {buy} menuda bor")
#         else :
#             print(f"{buy} menuda mavjud emas")
# else :
#     print("Ro'yhat bo'sh!")



# #  Foydalanuvchidan juft son kiritishni so'rang. Agar foydalanuvchi juft son kiritsa "Rahmat!",
# #  agar toq son kiritsa "Bu son juft emas" degan xabarni chiqaring.
# son = int(input("Assalomu alaykum juft son: "))
# if son % 2 == 0:
#     print(f"{son} juft son raxmat!")
# else :
#     print(f"{son} juft son emas!")



# # Foydalanuvchi yoshini so'rang, va muzeyga kirish uchun chipta narhini quyidagicha chiqaring:
# #
# # Agar foydalanuvchi 4 yoshdan kichkina yoki 60 dan katta bo'lsa bepul
# #
# # Agar foydalanuvchi 18 dan kichik bo'lsa 10000 so'm
# #
# # Agar foydalanuvchi 18 dan katta bo'lsa 20000 so'm
#
# year = int(input("Yoshingizni kiriting: "))
# if year > 60 or year < 4 :
#     print("Kirish tekin!")
# elif year < 18 :
#     print("Sizga kirish 10000")
# elif 18 <= year :
#     print("Kirish 20000")
# else :
#     print("Xato!")


# #  Foydalanuvchidan ikita son kiritishni so'rang, sonlarni solishtiring va ularning teng yoki katta/kichikligi haqida xabarni chiqaring
# son1 = int(input("1-son : "))
# son2 = int(input("2-son : "))
# if son1 > son2 :
#     print(f"{son1} katta {son2} dan")
# elif son2 == son1 :
#     print(f"{son1} = {son2}")
# else :
#     print(f"{son1} kichik {son2} dan")


#      mahsulotlar degan ro'yxat yarating va kamida 10 ta turli mahsulotni kiriting.
#      Yangi, savat degan bo'sh ro'yxat yarating va foydalanuvchidan savatga kamida 5 ta mahsulot kiritishni so'rang.
#      Savatdagi elementlarni, mahsulotlar ro'yxati bilan solishtiring va qaysi biri ro'yxatda bo'lsa "Mahsulot do'konimizda bor" aks holda, "Mahsulot do'konimizda yo'q" degan xabarlarni chiqaring.

# maxsulotlar = ['olma', 'skutr', 'usb', 'nexia', 'ruchka', 'daftar', 'sichqoncha', "so'mka", 'telefon', 'daraxt', 'archa']
# savat = []
#
# son = int(input("Nechta maxsulot kiritmoqchisiz:"))
#
# for i in range(0, son) :
#     savat.append(input(f"{i + 1} - maxsulot: "))
# for maxs in savat :
#     if maxs in maxsulotlar :
#         print(f"{maxs} maxsulotlarning ichida bor")
#     else:
#         print(f"{maxs} maxsulotlar ichida yo'q")

#  Yuqoridagi dasturni quyidagicha o'zgartiring: foydalanuvchidan 5 ta mahsulot kiritishni so'rang.
#  Foydalanuvchi so'ragan va do'konda bor mahsulotlarni yang, bor_mahsulotlar degan ro'yxatga,
#  do'konda yo'q mahsulotlarni esa mavjud_emas degan ro'yxatga qo'shing.  Agar mavjud_emas ro'yxati bo'sh bo'lsa,
#  "Siz so'ragan barcha mahsulotlar do'konimizda bor" degan xabarni, aks
#  holda esa "Quyidagi mahsulotlar do'konimizda yo'q: ....." degan xabarni chiqaring.





# #  1. Sonning musbat yoki manfiy ekanligini aniqlash
# # # Foydalanuvchidan son kiritishni so‘rang va u musbat, manfiy yoki nol ekanligini aniqlang.
# # number = int(input("Son kiriting: "))
# # if number > 0 :
# #     print('Musbat')
# # elif number == 0 :
# #     print("Nol")
# # else :
# #     print("Manfiy")


#
# #  2. Yosh bo‘yicha toifalash
# # Foydalanuvchidan yosh kiritishni so‘rang va u bola (0-12),
# # o‘smir (13-19), kattalar (20-59) yoki qariyalar (60+) toifasiga kirishini aniqlang.
#
# age = int(input("Yosh: "))
# if 0 <= age <= 12 :
#     print("U bola")
# elif 13 <= age <= 19 :
#     print("O'smir")
# elif 20 <= age <= 59 :
#     print("Katta")
# else :
#     print("Qariya")



#
# #  3. Baholarni harfga aylantirish
# # Foydalanuvchidan 0-100 oralig‘idagi bahoni so‘rang va uni quyidagi mezonlar bo‘yicha harfli bahoga aylantiring:
#
# baxo = int(input("Baho : "))
# if 0 <= baxo <= 59 :
#     print('F')
# elif 60 <= baxo <= 69 :
#     print("D")
# elif 70 <= baxo <= 79 :
#     print("C")
# elif 80 <= baxo <= 89 :
#     print("B")
# elif 90 <= baxo <= 100 :
#     print("A")
# else:
#     print("Xato!")


# #  4. Kabisa yili
# # Foydalanuvchidan yil kiritishni so‘rang va u kabisa yili ekanligini aniqlang
# # (kabisa yili 4 ga bo‘linadi, lekin 100 ga bo‘linsa, 400 ga ham bo‘linishi kerak).
# year = int(input("Yilni kiriting: "))
#
# if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
#     print("Kabisa yili!")
# else :
#     print("Kabisa yili emas!")










































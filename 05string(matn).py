

# ism = "Asomiddin"
# familya = "Abduqahharov"
# yosh = '20'
#
# print(f"Mening ismim {ism}, Familyam {familya}, Yoshim {yosh} da.")

# MAHSUS BELGILAR

# print('Hello world')
# print("Hello \tworld")
# print("Hello \nworld")


# STRING METHODLAR
# last_name = "asomiddin"
# first_name = ' abduqahharov'
# full_name = last_name + first_name
# fullname = f"{last_name},{first_name}"
# print(last_name.upper())    # Natija ASOMIDDIN
# print(full_name.upper())    # ASOMIDDIN ABDUQAHHAROV
# print(fullname.upper())


# lastname = 'ASOMIDDIN'
# firstname = "ABDUQAHHAROV"
# print(lastname.lower())   #  Natija: asomiddin
# print(firstname.lower())  # Natija: abduqahharov
#
# print(lastname.title())    # Natija: Asomiddin
# print(firstname.title())   # Natija abduqahharov
#
# matn = "CAPITALIZE METHOD FULL MATNING BRINCHI HARFNI KATTA QILADI."
# print(matn.title())   # Natija: Capitalize Method Full Matning Brinchi Harfni Katta Qiladi.
# print(matn.capitalize())   # Natija: Capitalize method full matning brinchi harfni katta qiladi.



# meva = "              olma            "
# print(meva)   # Natija:           olma
# print(f"Men {meva.lstrip()} ni yaxshi ko'raman")   # lstrip() chap tarafdagi bo'shliqni olib tashlaydi.
# print(f"Men {meva.rstrip()} ni yaxshi ko'raman.")    # rstrip() o'ng tarafdagi bo'shliqni olib tashlaydi.
# print(f"Men {meva.strip()}  ni yaxshi ko'raman.")    # strip() ikki tarafdagi bo'shliqni ham olib tashlaydi.
# print(f"Men {meva} ni yaxshi ko'raman .")   # asil holatida.


# INPUT

# savol = input("Iltimos ismingizni kiriting: ")
# print(f"Assalomu alaykum {savol.title()} tanishganimdan xursandman.")




# Yuqoridagi o'zgaruvchilarni jamlab, quyidagi ko'rinishda konsolga chiqaring:
# Diqqat uzun kodlarni \ belgisi yordamida keyingi qatorga
# ko'chirish mumkin
matn = "Assalomu alaykum \t belgi matining orasni ochib beradi.\nBubelgi esa keyingi qatorga o'tqazib beradi."
print(matn)


# #Yuqoridagi o'zgaruvchilarning qiymatini foydalanuvchidan so'rang.
# viloyat = input("Viloyatingizni kiriting: ").title()
# tuman = input("Tuman: ").title()
# mahalla = input("Mahalla: ").title()
# kocha = input("Ko'cha: ").title()
# nomer = input("Ko'cha raqami: ").title()
# print(f"Sizning yashash joyingiz:\n{viloyat, tuman, mahalla, kocha, nomer}")




# Yuqoridagi matnni konsolga chiqarishda har bir verguldan keyin yangi qatorga yozing
viloyat = input("Viloyat : ")
tuman = input("Tuman : ")
mahalla = input("Mahalla : ")
kocha = input("Ko'cha : ")

print(f"{viloyat}, \n{tuman}, \n{mahalla}, \n{kocha}")



# Yuqoridagi o'zgaruvchilarni f-string yordamida, yangi manzil deb nomlangan o'zgaruvchiga yuklang
manzil = f"Ko'cha: {kocha}, mahalla: {mahalla}, tuman: {tuman}, viloyat: {viloyat}."
print(manzil)




#manzil ga biz yuqorida o'rgangan metodlarni qo'llab ko'ring.
print(viloyat.upper())
print(tuman.title())
print(mahalla.capitalize())
print(kocha.lower())

































































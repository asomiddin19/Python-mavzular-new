from moduls import avto_info, avto_kirit, avto_malumot


# avto1 = avto_info('gm', 'malibu', 'qora', '2021', 2300, 1000)
# print(avto1)

# cars = avto_kirit()
# for car in cars:
#     print(f"{car['kompaniya']}, {car['model']} yili {car['year']} rangi {car['colour']} {car['km']} km yurgan narxi : {car['price']}.")

import math

# print(math.sqrt(12))
# print(math.log2(16))

import random

# print(random.randint(1, 100))
# print(random.randint(100, 200))
# print(random.randint(300, 400))


ismlar = ['asomiddin', 'alisher', 'abdulloh', 'komil', 'davron', 'jafar', 'davlat', 'homid']
# print(random.choice(ismlar))  tasodifiy element chiqaradi.

# ism = random.choice(ismlar)
# print(ism)
# print(random.choice(ism))

# sonlar = list(range(1, 200, 4))
# son = random.choice(sonlar)
# print(son)


# numbers = list(range(1, 20))
# print(numbers)
# random.shuffle(numbers)
# print(numbers)


def oyin() :
    print("Salom men bilan son o'ylab top o'ynini o'ynaysizmi!")
    while True :
        savol = input("Ha o'ynayman (1), Yo'q o'ynamayman (0): ")
        if savol.lower() == "0" :
            print("Dasturni yakunladingiz!")
            break
        tasnif = "Ajoyib o'yin shartlarni tushuntraman! "
        tasnif += "\nMen 1 dan 20 gacha sonlar orasdan son o'ylayman siz topishga harakat qilib ko'rasiz!"
        print(tasnif)
        son_bot = random.randint(1, 20)
        oylagan_son = "Men bir son o'yladim siznigcha qaysi sonni o'yladim: "
        while True :
            number = input(oylagan_son)
            if son_bot == int(number) :
                savol += "Yana o'ynashni hohlaysizmi!\nHa o'ynayman (1), Yo'q o'ynamayman (0): "
                print("Ajoyib siz topdingiz!")
                break
            elif son_bot < int(number) :
                oylagan_son = "Men o'ylagan sonni qayta kiriting: "
                print(f"Dasturni to'xtatish uchun 'exit' deb yozing \nSiz kiritgan {number} soni men o'ylagan sondan katta")
                continue
            elif son_bot > int(number) :
                oylagan_son = "Men o'ylagan sonni qayta kiriting: "
                print(f"Dasturni to'xtatish uchun 'exit' deb yozing \nSiz kiritgan {number} soni men o'ylagan sondan kichik")
                continue
            elif oylagan_son == "exit" :
                break
# print("Dastur to'xtadi")
# oyin(

































































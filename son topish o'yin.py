
import random
# def son_top1() :
#     print("Assalomu alaykum keling men siz bilan son top o'ynini o'ynaymiz!")
#     savol = ''
#     while savol != "yo'q" :
#         print("1 dan 10 gacha son o'yladim topishga xarakat qilib ko'ring >>> ")
#         ozgaruv_matn = "Son kiriting: "
#         random_son = random.randint(1, 11)
#         sikl_taxmin = 1
#         while True :
#             foyda_son = int(input(ozgaruv_matn))
#
#             if foyda_son == random_son :
#                 print(f"Tabriklayma men o'ylagan son {random_son} edi.\nSiz {sikl_taxmin} ta urnishda topdingiz!")
#                 break
#             elif foyda_son > random_son :
#                 print(f"Siz o'ylagan son {foyda_son} o'ylagan sonimdan katta!")
#                 ozgaruv_matn = "Yana harakat qilib ko'ring "
#                 sikl_taxmin += 1
#
#                 continue
#             elif foyda_son < random_son :
#                 print(f"Siz o'ylagan son {foyda_son} o'ylagan sonimdan kichik!")
#                 ozgaruv_matn = "Yana harakat qilib ko'ring "
#                 sikl_taxmin += 1
#
#                 continue
#         savol = input("Yana o'ynaymizmi (ha/yo'q) : ")
#     print("Dastur yakunlandi!")
# son_top1()



def son_top2() :
    savol = "Keling enid siz son o'ylaysiz men topishga harakat qilib ko'raman!"
    print(savol)
    qiymat = ''
    sikl_tavak = 1
    bosh_r = 1
    tuga_r = 11
    boshlash = input("O'yinni boshlash uchun interni bosing: ")

    while qiymat != "yo'q" :
        bot_random = random.randint(bosh_r, tuga_r)

        foy_son = input(f"Siz o'ylagan son {bot_random} ga teng.Ha to'g'ri (t) "
                        f"\nYo'q men o'ylagan son {bot_random} dan katta (+), Kichik (-): ")


        if foy_son.lower() == 't' :
            print(f"Ajoyib men siz o'ylagan sonni {sikl_tavak} ta urnishda topibman!")
            break

        elif foy_son == '+' :
            bosh_r = bot_random
            print("yana harakat qilib ko'raman!")
            sikl_tavak += 1
            continue

        elif foy_son == '-' :
            tuga_r = bot_random
            print("Yana harakat qilib ko'raman!")
            sikl_tavak += 1
            continue
        qiymat = input("Yana o'ynaymizmi (ha/yo'q) : ")

son_top2()











































































def name_qay(lastname, firstname, father_name = '') :
    if father_name :
        result = f"Talaba malumot: {lastname} {firstname} otasning ismi {father_name}. "
    else:
        result = f"Talaba malumot: {lastname} {firstname}"
    return result
#
# print('davron', 'fozilov', 'shavkat')
# print('salim', 'salimov')
# print('akmal', 'komilov', 'sayfiddin')

def oraliq(min , max) :
    sonlar = []
    while min < max :
        sonlar.append(min)
        min += 1
    return sonlar

# print(oraliq(1, 23))
# print(oraliq(123, 1234))


def oraliq_step(min, max, qadam = 1) :
    sonlar = []
    while min < max :
        sonlar.append(min)
        min += qadam
    return sonlar

# print(oraliq_step(1, 23, 3))
# print(oraliq_step(23, 168, 4))



def avto_dict(kompaniya, model, rang, karobka, yil, narx = None) :
    avto = {
        'kompaniya' : kompaniya,
        'model' : model,
        'rang' : rang,
        'karobka' : karobka,
        'yil' : yil,
        'narx' : narx
    }
    return avto


# print("Aftomobillar ro'yhatni yaratib beruvchi dastur!")
#
# afto_list = []
#
# while True :
#     print("Malumotlarni kiriting! ", end=' --->>>')
#     kompaniya = input("Avtoning kompaniyasni kiriting: ")
#     model = input("Modelni kiriting: ")
#     rang = input("Rangni kiriting: ")
#     karobka = input("Karobkasni kiriting: ")
#     year = input("Yilni kiriting: ")
#     price = input('Narxni kiriting: ')
#     avto = avto_dict(kompaniya, model, rang, karobka, year, price)
#     afto_list.append(avto)
#     savol = input("Yana mashina qo'shasizmi (1/0): ")
#     if savol == '0' :
#         break
# print("Dastur yakunlandi!")
#
# print(f"\nKiritilgan mashinalar ro'yhati bilan tanishing!")
# n = 1
# for car in afto_list :
#     if car['narx'] :
#         price = car['narx']
#     else :
#         car['narx'] = 'Nomalum'
#     print(f"{n} - avtomobil. {car['kompaniya'].title()} kompaniyasi, modeli {car['model']}, "
#           f"\nrangi {car['rang']}, karobkasi {car['karobka']}, yili {car['yil']} narxi {car['narx']} ")
#     n += 1


# list = [1, 2, 5, -6, 12, -23, 34]
# print(count_manfiy(list))


def sum_number(x, y) :
    return f"{x} + {y} = {x + y}"

# print(sum_number(12, 3))


def hello_fun(name = '') :
    return  f"Assalomu alaykum {name.title()}"

# print(hello_fun('Alisher'))
# print(hello_fun())


def numbers_sum(*numbers) :
    sum_numbers = 0
    for number in numbers :
        sum_numbers += number
    return sum_numbers
# print(numbers_sum(1,2,3,4,5,6,7,8,9,10))



def list_print(**kwargs) :
    return kwargs
# print(list_print(firstname = 'Alisher', lastname = "Akmalov", age = 23, course = 3, direction = 'IT server'))

def tashqi() :
    print('Tashqi')
    def ichki() :
        print('Ichki')
    ichki()

# tashqi()


def like_range(start, end,) :
    list_like = []
    while start < end :
        list_like.append(start)
        start += 1
    return list_like
# print(like_range(1, 16))


def baxolash(talabalar) :
    baxolar_dict = {}
    while talabalar :
        name = talabalar.pop()
        baxo = int(input(f"{name.title()}ning baxosni kiriting: "))
        baxolar_dict[name.title()] = baxo
    return baxolar_dict


# talabalar = ['asomiddin', 'abdulloh', 'komil', 'sanjar', 'ubaydulloh', 'ikrom', 'fozil', 'jaxongir', 'mamurjon']
# result = baxolash(talabalar[:])
# # print(result)
# for talaba, baxo in result.items() :
#     print(f"{talaba}ning baxosi {baxo} ball.")




#      Matnlardan iborat ro'yxat qabul qilib, ro'yxatdagi har bir matnning birinchi harfini katta harfga o'zgatiruvchi funksiya yozing.

# def matn_qay(text_list) :
#     text_result = []
#     text_list1 = text_list[:]
#     while text_list1 :
#         element = text_list1.pop()
#         text_result.append(element.capitalize())
#     return text_result



# ismlar = ["ali", "vali", "dilshod", "ozoda", "zarina", "javohir", "malika", "sherzod", "gulnoza", "sardor"]
# print(matn_qay(ismlar))
# print(ismlar)

#      Yuoqirdagi funksiyani asl ro'yxatni o'zgartirmaydigan va yangi ro'yxat qaytaradigan qilib o'zgartiring

def matn_qay(matn_list) :
    result = []
    for soz in matn_list :
        result.append(soz.capitalize())
    return result


# ismlar = ["ali", "vali", "dilshod", "ozoda", "zarina", "javohir", "malika", "sherzod", "gulnoza", "sardor"]
# print(matn_qay(ismlar))
# print(ismlar)


#    Darsimiz davomida yozgan bahola funksiyasini .pop() metodidan
#    foydalanmasdan va asl ro'yxatga o'zgartirish kiritmasdan faqat lug'at qaytaradigan qilib yozing.

def baxola_fan(talabalar) :
    result = {}
    for talaba in talabalar :
        baxo = int(input(f"{talaba.title()}ning baxosni kriting: "))
        result[talaba.title()] = baxo
    return result

# ismlar = ["ali", "vali", "dilshod", "ozoda", "zarina", "javohir", "malika", "sherzod", "gulnoza", "sardor"]
# print(baxola_fan(ismlar))
# print(ismlar)






# Funksiyalar bo‘yicha katta topshiriqlar to‘plami

# Son qabul qilib, uning kvadratini qaytaruvchi funksiya yozing.
def numer_kv(number) :
    print(f"{number} ning kvadrati: {number ** 2}")

# numer_kv(4)
# numer_kv(7)




# Ikki son qabul qilib, ularning yig‘indisini qaytaruvchi funksiya yozing.
def ikki_son(number1, number2) :
    result = number1 + number2
    print(result)

# ikki_son(13, 20)
# ikki_son(203, 241)





# Foydalanuvchi kiritgan so‘zni teskari qilib qaytaruvchi funksiya yozing.
def teskari(text) :
    matn = list(text)
    matn.reverse()
    print(''.join(matn))
# teskari('asomiddin men 20 da')




# Son qabul qilib, juft yoki toq ekanini aniqlaydigan funksiya yozing.
def number_an(number) :
    if number % 2 == 0 :
        print(f"{number} soni juft son.")
    else:
        print(f"{number} soni toq son.")

# number_an(24)
# number_an(347)





# Son qabul qilib, musbatmi yoki manfiyligini aniqlaydigan funksiya yozing.
def aniq_la(number) :
    if number > 0 :
        print("Musbat")
    else:
        print("Manfiy")

# aniq_la(23)
# aniq_la(-12)
# aniq_la(-19)


#   Matn qabul qilib, undagi eng uzun so‘zni qaytaruvchi funksiya yozing.
# def max_matn(text) :
#
#     matn = {}
#     for soz in text.split(' ') :
#         matn[len(soz)] = soz
#         soz_max = max(matn)
#         result = matn[soz_max]
#     return result
# print(max_matn("Assalomuas alaykum men asomiddin men 20 yoshdaman sen necha yoshdas "))


# def max_qiy(matn) :
#     sozlar = matn.split()
#     soz = max(sozlar, key = len)
#     return soz
# print(max_qiy("The Campeon Nacional de Liga de Primera División, commonly known as the Primera División or LaLiga, and officially known "))


#  Son qabul qilib, tub sonmi yoki yo‘qmi aniqlaydigan funksiya yozing.

def tub_aniq(number) :
    if number <= 1 :
        return "Tub emas"

    for son in range(2, int(number ** (1/2)) + 1)  :
        if number % son == 0 :
            return "Tub emas"
    return "Tub son"


# print(tub_aniq(22))
# print(tub_aniq(21))
# print(tub_aniq(19))
tub_aniq(34)


#   Ro‘yxat qabul qilib, undagi nechta manfiy son borligini qaytaruvchi funksiya yozing.

def count_manfiy(new_list) :
    count_mn = 0
    for number in new_list :
        if number < 0 :
            count_mn += 1
    return f"{count_mn} ta manfiy son bor"



























































































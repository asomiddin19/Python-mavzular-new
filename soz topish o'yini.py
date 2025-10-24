import random

sozlar = [
    # Kundalik buyumlar
    "kitob", "qalam", "daftar", "stol", "kursi", "oyna", "eshik", "deraza", "telefon", "noutbuk",
    "kompyuter", "sumka", "soat", "oyoq", "bosh", "qo‘l", "ko‘z", "quloq", "til", "tish",

    # Tabiat
    "daraxt", "gul", "barg", "yomg‘ir", "qor", "shamol", "quyosh", "oy", "osmon", "yulduz",
    "tog‘", "daryo", "ko‘l", "cho‘l", "o‘rmon", "yer", "havо", "bulut", "bahor", "yoz",

    # Hayvonlar
    "ot", "sigir", "qo‘y", "echki", "it", "mushuk", "qush", "burgut", "kapalak", "ari",
    "ilon", "baliq", "tovuq", "xo‘roz", "tulki", "bo‘ri", "ayiq", "fil", "jirafa", "maymun",

    # Oziq-ovqat
    "non", "sut", "osh", "sho‘rva", "choy", "qahva", "olma", "anor", "uzum", "shaftoli",
    "tarvuz", "qovun", "sabzi", "piyoz", "bodring", "pomidor", "gosht", "tuxum", "asal", "qaymoq",

    # His-tuyg‘ular
    "xursand", "baxtli", "g‘amgin", "dono", "aqlli", "mehribon", "shirin", "achchiq", "jahldor", "kamtar",
    "sabrli", "shod", "qiziq", "qattiqqo‘l", "oqilona", "do‘stona", "yaxshi", "yomon", "go‘zal", "xunuk",

    # Texnika va zamonaviy hayot
    "internet", "kod", "dastur", "robot", "sun’iy", "intellekt", "elektr", "avtomobil", "samolyot", "raketa",
    "poezd", "tramvay", "avtobus", "velosiped", "radio", "televizor", "kamera", "printer", "klaviatura", "sichqoncha"
]



def aniqla_harf(harf, soz) :
    return harf in soz

print(aniqla_harf('a', 'matn'))




def soz_top() :
    print("Keling so'z topish o'yinini o'ynaymiz!\nMen so'z o'ylayman siz harflar bilan topishga xarakat qilib ko'rasiz!")
    random_soz = random.choice(sozlar)



















































































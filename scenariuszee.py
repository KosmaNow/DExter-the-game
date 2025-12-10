import statystyki
from szukanieofiary import szukanie_ofiary
from rozprawa import rozprawa_rrr
from spanie import spanie_s
from walka import walka_z_doaksem
from random import randint


def scenariusz_b():
    print("Godzina 15:15 Miami. Twoje mieszkanie.")
    print("Policja stoi pod twoim mieszkaniem w celu ochrony cię przed Jamesem Doaksem.")
    print("Czy jesteś gotowy na drugi sezon? (tak/nie)")

    inp = input("> ")
    if inp == "tak":
        while True:
            print("Co chcesz zrobić?")
            print("0... Wyjdź")
            print("1... Iść spać")
            print("2... Znaleźć kolejną ofiarę")
            print("3... Zabić Jamesa Doaksa")
            print("4... Uwolnić Jamesa Doaksa")
            print("5... Zabijasz lajle")
            print("6... Wracasz do lajly")
            print("7...Przyznajesz się policji")

            inp = input("> ")

            if inp == "0":
                break
            elif inp == "1":
                spanie_s()
            elif inp == "2":
                szukanie_ofiary()
            elif inp == "3":
                walka_z_doaksem()
            elif inp == "4":
                walka_z_doaksem()
            elif inp == "5":
                statystyki.punkty_misji = statystyki.punkty_misji + 1
                print("dostałeś 1 punkt misji")
            elif inp == "6":
                statystyki.punkty_misji = statystyki.punkty_misji - 1
                print("dostałeś -1 punkt misji")
            elif inp == "7":
                rozprawa_rrr()
    else:
        print("Może następnym razem")


def scenariusz_a():
    print("godzina 16")
    print("biney nieżyje")
    statystyki.punkty_misji = statystyki.punkty_misji - 1
    print("dostałeś -1 punkt misji")


def scenariusz_c():
    print("po0daj 3 liczby pierwsza od jeden do 100 druga od 1 do 100 trzecia od jeden do pięciu")
    a = int(input(""))
    b = int(input(""))
    c = int(input(""))
    for i in range(c):
        x = randint(a,b)
        print(x)

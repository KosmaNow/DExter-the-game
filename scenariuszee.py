#sc
import statystyki
from szukanieofiary import szukanie_ofiary
from random import randint
from rozprawa import rozprawa_rrr
from spanie import spanie_s
from walka import walka_z_doaksem
pu = statystyki.punkty_misji 
def scenariusz_b():
    print("Godzina 15:15 Miami. Twoje mieszkanie.")
    print("Policja stoi pod twoim mieszkaniem w celu ochrony cię przed Jamesem Doaksem.")
    print("Czy jesteś gotowy na drugi sezon? (tak/nie)")

    inp = input("> ").lower()
    if inp == "tak":
        print("Zaczynamy!\n")
        
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
                print("Powrót do menu...")
                break
            elif inp == "1":
                print("Idziesz spać...")
                spanie_s()
            elif inp == "2":
                print("Szukasz ofiary...")
                szukanie_ofiary()
            elif inp == "3":
                print("Próbujesz zabić Doaksa...")
                print("Doaks się uwolnił    ")
                walka_z_doaksem()
            elif inp == "4":
                print("Uwalniasz Doaksa...")
                print("o nie walka z doaksem")
                walka_z_doaksem()
            elif inp == "5":
                print("zabijasz Lajle")
                rrr = 1
                pu += rrr
                print(f"dostałeś {rrr} punkt misji")
                print(f"teraz twoje punkty misji wynoszą {pu}")
            elif inp == "6":
                print("wracasz do lajly")
                ggg = -1
                pu += ggg
                print(f"dostałeś {ggg} punkt misji")
                print(f"teraz twoje punkty misji wynoszą {pu}")
            elif inp == "7":
                print("Przynajesz się na policji")
                rozprawa_rrr()
            else:
                print("Niepoprawny wybór!")
    else:
        print("Może następnym razem...")
def scenariusz_a(): 
    print("godzina 16")
    print("biney nieżyje")
    ggg = -1
    pu += ggg
    print(f"dostałeś {ggg} punkt misji")
    print(f"teraz twoje punkty misji wynoszą {pu}")




def scenariusz_c():
    print("I wonder if Rita is looking at this same moon at this same moment. I like that - connected by light. The dark passenger has been fighting against it, trying to keep me all to himself.")  
    print("po0daj 3 liczby " \
    "pierwsza od jeden do 100" \
    "druga od 1 do 100" \

    "trzecia od jeden do pięciu")
    print("a/b/c")
    a = (int(input("")))
    b = (int(input("")))
    c = (int(input("")))
    for i in range(c):
        x = (randint(a,b))
        print(x)

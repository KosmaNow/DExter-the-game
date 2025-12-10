
import time
import statystyki
from random import randint



def k_t():
    print("witaj w kalkulatorze pola trójkąta")
    print("h ....")
    print("pod.....")
    h = float(input())
    a = float(input())
    wy = a * h / 2
    print("pole twojego  trójkąta wynosi", wy)
    return wy


def szukanie_ofiary():
    print("będziesz szukał ofiary")
    print("ile prób cchesz mieć ?")
    pr = int(input())

    prwtkorzytane = 0

    for i in range(pr):
        prwtkorzytane = prwtkorzytane + 1
        print("próba", prwtkorzytane, "z", pr)

        print("twoja ofiara jest za rogiem")
        time.sleep(1)

        print("możesz zrobić dwie rzeczy")
        print("1.... zaatakować")
        print("2.... poczekać")
        inp = input(">>>>")

        if inp == "1":
            print("ofiara uceikła")
            if prwtkorzytane >= pr:
                print("przekroczyłes maks prób")
                statystyki.dex_hp = 0
                return None
            continue

        elif inp == "2":
            print("Czego chcesz użyć ?")
            print("a... młotka")
            print("b... strzxykawki")
            inp = input(">>>>")

            if inp == "a":
                print("ofiara wyrwała się i ucieka")
                if prwtkorzytane >= pr:
                    print("przekroczyłes maks prób")
                    statystyki.dex_hp = 0
                    return None
                continue

            elif inp == "b":
                print("ofiara uśpiona i w bagażniku")
                while statystyki.ofira_hp > 0 and statystyki.dex_hp > 0:
                    print("musisz jechać do starego portu")
                    time.sleep(1)
                    print("o nie jakiś świr z bronią grozi ci że jak nie obliczysz pola trójkąta to cie zabije")
                    print("wysokość wynosi 6 a podstawa 10 ")
                    wynik = k_t()
                    print("Mów")
                    inp = float(input())

                    if inp == 30:
                        print("świr kończy live")
                    else:
                        print("zabija cię deksiii")
                        statystyki.dex_hp = statystyki.dex_hp - 100

                    print("Jesteś nad ofiarą z fake biney")
                    time.sleep(1)
                    print("pozbądz się ofiary")
                    inp = input("")

                    if inp == "tak":
                        statystyki.ofira_hp = statystyki.ofira_hp - 100
                        statystyki.punkty_misji = statystyki.punkty_misji + 1
                    else:
                        statystyki.dex_hp = statystyki.dex_hp - 100
                        statystyki.punkty_misji = statystyki.punkty_misji - 1

                    if prwtkorzytane >= pr:
                        print("przekroczyłes maks prób")
                        statystyki.dex_hp = 0
                        return None

    print("Nie udało ci się złapać ofiary w żadnej liczbie prób")
    statystyki.dex_hp = 0
    return None
from random import randint
import statystyki

def walka_z_doaksem():
    print("walcz z doaksem.............1")

    while statystyki.dex_hp > 0 and statystyki.doakes_hp > 0:
        print("Co robisz >")
        print("1....Atak doaks")
        print("2....Leczysz sie")
        print("3    tańczysz makarene")

        inp = input(">>>>")

        if inp == "1":
            obrazenia = randint(20 ,40)
            statystyki.doakes_hp = statystyki.doakes_hp - obrazenia
            print("zadajesz", obrazenia, "obrazen doaksowi")
            print("teraz doaks ma", statystyki.doakes_hp, "hp")
            ob = randint(30,35)
            statystyki.dex_hp = statystyki.dex_hp - ob
            print("doaks dał ci", ob, "hp sobie")
            print("teraz  masz", statystyki.dex_hp, "hp")
        elif inp == "2":
            lecz = randint(10,70)
            statystyki.dex_hp = statystyki.dex_hp + lecz
            print("zadajesz", lecz, "hp sobie")
            print("teraz  masz", statystyki.dex_hp, "hp")
            lec = randint(20,50)
            statystyki.doakes_hp = statystyki.doakes_hp + lec
            print("doaks otrzymał", lec, "hp")
            print("doaks ma teraz", statystyki.doakes_hp, "hp")
        elif inp == "3":
            supermakarenaobrazenia = -100
            statystyki.doakes_hp = statystyki.doakes_hp - supermakarenaobrazenia
            print("doaks ma teraz", statystyki.doakes_hp, "hp")

        if statystyki.doakes_hp <= 0:
            print("pokonałeś doaksa")
            statystyki.punkty_misji = statystyki.punkty_misji + 1
            print("dostałeś 1 punkt misji")
            break
        if statystyki.dex_hp <= 0:
            print("przegrałeś z doaksem")
            break

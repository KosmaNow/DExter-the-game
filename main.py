from scenariuszee import scenariusz_a, scenariusz_b, scenariusz_c

print("Witaj Który sezon wybierasz")
print("a... sezon 1")
print("b... sezon 2")
print("c... sezon 4")
print("d... sezon 8")

s = 0
while s < 1:
    inp = input(" ")
    if inp == "a":
        scenariusz_a()
    elif inp == "b":
        scenariusz_b()
    elif inp == "d":
        print("Deb nie żyje a ty popłynołeś w burze")
        print("Nie żyjesz")
        s = s + 1
    elif inp == "c":
        scenariusz_c()
        s = s + 1
    else:
        print("Ten sezon jeszcze nie jest gotowy.")


   
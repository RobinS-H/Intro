from random import randint
from colorama import Fore

pengar = 100
rundor = 0
spel = True

while spel:
    print(Fore.WHITE + "Du har "+ Fore.GREEN + f"{pengar}kr")
    if pengar <= 0:
        print(Fore.WHITE + "Du har för lite pengar")
        print(Fore.RED + "Du har förlorat")
        print(Fore.WHITE + "Du klarade "+ Fore.RED + f"{rundor} " + Fore.WHITE + "rundor")
        rundor = 0
        pengar = 100
        print()
        print("Försök igen")
        print()
        continue
    svar = input(Fore.WHITE + "Vill du spela? ")
    print()
    if svar == "ja" or svar == "JA" or svar == "Ja":
        tärning1 = randint(1, 6)
        tärning2 = randint(1, 6)
        print("Tärning1 blev " + Fore.CYAN + f"{tärning1}")
        print(Fore.WHITE + "Tärning2 blev "+ Fore.CYAN + f"{tärning2}")
        print()
        if tärning1 == tärning2:
            print(Fore.WHITE + "Tärningarna blev lika")
            print(Fore.GREEN + "Du vann")
            print(Fore.WHITE + "Du fick " +  Fore.GREEN + f"{tärning1+tärning2}kr")
            pengar = pengar + tärning1 + tärning2
            print()
            print(Fore.WHITE + "Du har nu " + Fore.GREEN + f"{pengar}kr")
            print()
            rundor = rundor + 1
            continue
        else:
            if tärning1 != tärning2:
                print(Fore.WHITE + "Tärningarna blev olika")
                print(Fore.RED + "Du förlorade")
                print(Fore.WHITE + "Du förlorade "+ Fore.RED + f"{tärning1+tärning2}kr")
                pengar = pengar - (tärning1 + tärning2)
                print()
                print(Fore.WHITE + "Du har nu "+ Fore.GREEN + f"{pengar}kr")
                print()
                rundor = rundor + 1
                continue
    else:
        continue


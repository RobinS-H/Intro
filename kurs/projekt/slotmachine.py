from random import randint
from time import sleep
from colorama import Fore

pengar = 100
lista = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "W"]

while True:

    print(Fore.WHITE + "Pengar: " + Fore.GREEN + str(int(pengar)))
    print()

    # hur mycket ska bettas, på hur många spins?

    bet = input(Fore.WHITE + "Bet? ")
    if bet.isdigit() == True:
        bet = int(bet)
        if bet > pengar or bet < 1:
            print(f"Skriv ett bet mellan 1 och {pengar}")
            continue
        else:
            print("Ditt bet är " + Fore.GREEN + str(bet))
    else:
        print("Skriv ett riktigt bet.")
        continue
    auto_spins = input(Fore.WHITE + "Spins? ")
    if auto_spins.isdigit() == True:
        auto_spins = int(auto_spins)
        if auto_spins < 1:
            print("Skriv ett tal högre än 0")
            continue
        else:
            print("Dina spins är " + Fore.BLUE + str(auto_spins))
    else:
        print("Skriv ett riktigt tal.")
        continue

    # spins

    while auto_spins > 0 and pengar >= bet:

        vinst = 0
        pengar -= bet
        

        rad1 = False
        rad2 = False
        rad3 = False

        print()
        print(Fore.WHITE + "Pengar: " + Fore.GREEN + str(pengar))
        print()

        # symboler

        s1 = lista[randint(0,9)]
        s2 = lista[randint(0,9)]
        s3 = lista[randint(0,9)]
        s4 = lista[randint(0,9)]
        s5 = lista[randint(0,9)]
        s6 = lista[randint(0,9)]
        s7 = lista[randint(0,9)]
        s8 = lista[randint(0,9)]
        s9 = lista[randint(0,9)]


        sleep(0.5)
        print(Fore.WHITE + s1 + " | " + s2 + " | " + s3)
        sleep(0.5)
        print(s4 + " | " + s5 + " | " + s6)
        sleep(0.5)
        print(s7 + " | " + s8 + " | " + s9)
        sleep(0.5)
        print()
        
        # vinst beräkning

        def rad(s, bonus, vinst):
            if s == "1":
                vinst += bet * 2**bonus
                print(Fore.WHITE + "VINST: " + Fore.GREEN + str(bet * 2**bonus))
                sleep(0.5)
            elif s == "2":
                vinst += bet * 3**bonus
                print(Fore.WHITE + "VINST: " + Fore.GREEN + str(bet * 3**bonus))
                sleep(0.5)
            elif s == "3":
                vinst += bet * 5**bonus
                print(Fore.WHITE + "VINST: " + Fore.GREEN + str(bet * 5**bonus))
                sleep(0.5)
            elif s == "4":
                vinst += bet * 7**bonus
                print(Fore.WHITE + "VINST: " + Fore.GREEN + str(bet * 7**bonus))
                sleep(0.5)
            elif s == "5":
                vinst += bet * 10**bonus
                print(Fore.WHITE + "VINST: " + Fore.GREEN + str(bet * 10*bonus))
                sleep(0.5)
            elif s == "6":
                vinst += bet * 15**bonus
                print(Fore.WHITE + "VINST: " + Fore.GREEN + str(bet * 15**bonus))
                sleep(0.5)
            elif s == "7":
                vinst += bet * 20**bonus
                print(Fore.WHITE + "VINST: " + Fore.GREEN + str(bet * 20**bonus))
                sleep(0.5)
            elif s == "8":
                vinst += bet * 25**bonus
                print(Fore.WHITE + "VINST: " + Fore.GREEN + str(bet * 25**bonus))
                sleep(0.5)
            elif s == "9":
                vinst += bet * 40**bonus
                print(Fore.WHITE + "VINST: " + Fore.GREEN + str(bet * 40**bonus))
                sleep(0.5)
            elif s == "W":
                vinst += bet * 100**bonus
                print(Fore.WHITE + "VINST: " + Fore.GREEN + str(bet * 100**bonus))
                sleep(0.5)
            return vinst


        if s1 == s2 and s1 == s3:
            vinst += rad(s1, 1, vinst)
            rad1 = True
        if s4 == s5 and s4 == s6:
            vinst += rad(s4, 1, vinst)
            rad2 = True
        if s7 == s8 and s7 == s9:
            vinst += rad(s7, 1, vinst)
            rad3 = True

        print()

        if rad1 == True and rad2 == True:
            if s1 == s4:
                vinst += rad(s1, 2, vinst)
        if rad1 == True and rad3 == True:
            if s1 == s7:
                vinst += rad(s1, 2, vinst)
        if rad2 == True and rad3 == True:
            if s4 == s7:
                vinst += rad(s1, 2, vinst)
        
        print()

        if rad1 == True and rad2 == True and rad3 == True:
            if s1 == s4 and s1 == s7:
                vinst += rad(s1, 3, vinst)
        
        print()
        
        print(Fore.WHITE + "TOTAL VINST:  " + Fore.GREEN + str(vinst))

        pengar += vinst

        auto_spins -= 1
        




from random import randint
from time import sleep
from colorama import Fore

pengar = 1000
o_jämn_bonus = False
femtedels_bonus = False
jackpot = False
en_ifrån_bonus = False


while True:
    sleep(1)
    print()
    if pengar < 1000000:
        print(Fore.WHITE + f"Du har {pengar} kronor.")
    elif pengar > 1000000 and pengar < 1000000000:
        print(Fore.WHITE + f"Du har {pengar/1000000}Mn kronor.")
    elif pengar > 1000000000 and pengar < 1000000000000:
        print(Fore.WHITE + f"Du har {pengar/1000000000}Md kronor.")
    elif pengar > 1000000000000 and pengar < 1000000000000000:
        print(Fore.WHITE + f"Du har {pengar/1000000000000}B kronor.")
    else:
        print(Fore.WHITE + f"Du har {pengar/1000000000000000}Bd kronor")
    if pengar <= 0:
        print("Du har tyvärr inga pengar kvar.")
        print("Här får du 500 kronor tillbaks.")
        pengar = 500
    print()
    sleep(1)
    bet_nummer = input("Vilken nummer (1-100) vill du betta på? ")
    if bet_nummer == "r" or bet_nummer == "R":
        bet_nummer = randint(1, 100)
        print("Du valde nummer: " + str(bet_nummer))
    else:
        if bet_nummer.isdigit() == False:
            print("Skriv ett giltligt nummer.")
            continue
        else:
            bet_nummer = int(bet_nummer)
            if bet_nummer <= 0 or bet_nummer > 100:
                print("Ogiltigt antal.")
                continue
            else:
                print("Du valde nummer: " + str(bet_nummer))
    sleep(1)
    print()
    bet = input("Hur mycket vill du betta? ")
    if bet == "h" or bet == "H":
        bet = int(pengar/2)
    else:
        if bet.isdigit() == False:
            print("Skriv ett giltligt nummer.")
            continue
        else:
            bet = int(bet)
            if bet <= 0:
                print("Skriv ett positivt tal.")
                continue
            elif bet > pengar:
                print("Du har inte tillräckligt med pengar för det där bettet.")
                continue
    if bet < 1000000:
        print(f"Du valde att betta {bet} kronor på nummer {bet_nummer}.")
    elif bet > 1000000 and bet < 1000000000:
        print(f"Du valde att betta {bet/1000000}Mn kronor på nummer {bet_nummer}.")
    elif bet > 1000000000 and bet < 1000000000000:
        print(f"Du valde att betta {bet/1000000000}Md kronor på nummer {bet_nummer}.")
    elif bet > 1000000000000 and bet < 1000000000000000:
        print(f"Du valde att betta {bet/1000000000000}Bn kronor på nummer {bet_nummer}.")
    else:
        print(f"Du valde att betta {bet/1000000000000000}Bd kronor på nummer {bet_nummer}.")
    pengar = pengar - bet
    vinnande_nummer = randint(1, 100)
    sleep(1)
    print()
    print("Det vinnande nummret är: " + Fore.BLUE + f"{vinnande_nummer}")
    #

    if vinnande_nummer % 2 == bet_nummer % 2:
        o_jämn_bonus = True
    else:
        o_jämn_bonus = False
    #
    femtedels_nummer = randint(1, 5)
    if femtedels_nummer == 5:
        femtedels_bonus = True
    else:
        femtedels_bonus = False
    #
    if vinnande_nummer == bet_nummer:
        jackpot = True
    else:
        jackpot = False
    #
    if vinnande_nummer - 1 == bet_nummer or vinnande_nummer + 1 == bet_nummer:
        en_ifrån_bonus = True
    else:
        en_ifrån_bonus = False
    #
    #
    if o_jämn_bonus == True or femtedels_bonus == True or jackpot == True or en_ifrån_bonus == True:
        multiplier = 1
        sleep(1)
        print()
        if o_jämn_bonus == True:
            multiplier = multiplier * 2
            sleep(1)
            print()
            print(Fore.GREEN + "Du fick (o)jämn bonusen "+ Fore.BLUE + "(1/2)")
            print(Fore.MAGENTA + "Multi x2")
        if femtedels_bonus == True:
            multiplier = multiplier * 5
            sleep(1)
            print()
            print(Fore.GREEN + "Du fick femtedels bonusen "+ Fore.BLUE + "(1/5)")
            print(Fore.MAGENTA + "Multi x5")
        if jackpot == True:
            multiplier = multiplier * 50
            sleep(1)
            print()
            print(Fore.GREEN + "DU FICK "+ Fore.LIGHTGREEN_EX + "JACKPOT! "+ Fore.BLUE + "(1/100)")
            print(Fore.MAGENTA + "Multi x50")
        if en_ifrån_bonus == True:
            multiplier = multiplier * 10
            sleep(1)
            print()
            print(Fore.GREEN + "Du var 1 ifrån jackpotten och fick därför en tröstbonus "+ Fore.BLUE + "(1/50)")
            print(Fore.MAGENTA + "Multi x10")
        vinst = bet * multiplier
        print()
        sleep(1)
        if bet < 1000000:
            print(Fore.BLUE + f"Du bettade " + Fore.GREEN +f"{bet}"+ Fore.BLUE +" kronor och fick en multi på "+ Fore.MAGENTA + f"{multiplier}"+ Fore.BLUE +".")
            print("Du vann därför "+ Fore.GREEN + f"{vinst}"+ Fore.BLUE +" kronor!")
        elif bet > 1000000 and bet < 1000000000:
            print(Fore.BLUE + f"Du bettade " + Fore.GREEN +f"{bet/1000000}Mn"+ Fore.BLUE +" kronor och fick en multi på "+ Fore.MAGENTA + f"{multiplier}"+ Fore.BLUE +".")
            print("Du vann därför "+ Fore.GREEN + f"{vinst/1000000}Mn"+ Fore.BLUE +" kronor!")
        elif bet > 1000000000 and bet < 1000000000000:
            print(Fore.BLUE + f"Du bettade " + Fore.GREEN +f"{bet/1000000000}Md"+ Fore.BLUE +" kronor och fick en multi på "+ Fore.MAGENTA + f"{multiplier}"+ Fore.BLUE +".")
            print("Du vann därför "+ Fore.GREEN + f"{vinst/1000000000}Md"+ Fore.BLUE +" kronor!")
        elif bet > 1000000000000 and bet < 1000000000000000:
            print(Fore.BLUE + f"Du bettade " + Fore.GREEN +f"{bet/1000000000000}Bn"+ Fore.BLUE +" kronor och fick en multi på "+ Fore.MAGENTA + f"{multiplier}"+ Fore.BLUE +".")
            print("Du vann därför "+ Fore.GREEN + f"{vinst/1000000000000}Bn"+ Fore.BLUE +" kronor!")
        else:
            print(Fore.BLUE + f"Du bettade " + Fore.GREEN +f"{bet/1000000000000000}Bd"+ Fore.BLUE +" kronor och fick en multi på "+ Fore.MAGENTA + f"{multiplier}"+ Fore.BLUE +".")
            print("Du vann därför "+ Fore.GREEN + f"{vinst/1000000000000000}Bd"+ Fore.BLUE +" kronor!")
        pengar = pengar + vinst
        continue
    else:
        multiplier = 0
        print()
        sleep(1)
        print(Fore.RED + "Du vann tyvärr ingenting.")
        continue
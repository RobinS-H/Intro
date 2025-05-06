from colorama import Fore
from random import randint
from time import sleep

lista = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20", "21", "22", "23", "24", "25", "26", "27", "28", "29", "30", "31", "32", "33", "34", "35", "36"]
nummer_till_farg = {}
nummer_till_farg[lista[0]] = Fore.GREEN
red_numbers = ["1", "3", "5", "7", "9", "12", "14", "16", "18", "19", "21", "23", "25", "27", "30", "32", "34", "36"]
black_numbers = ["2", "4", "6", "8", "10", "11", "13", "15", "17", "20", "22", "24", "26", "28", "29", "31", "33", "35"]

for i in red_numbers:
    nummer_till_farg[lista[int(i)]] = Fore.RED
for i in black_numbers:
    nummer_till_farg[lista[int(i)]] = Fore.BLACK


pengar = 100

while True:
    print()
    print(Fore.WHITE + "Pengar: " + Fore.GREEN + f"{pengar}")
    print()

    # vad ska bettas på

    print(Fore.WHITE + "Vad vill du betta på?")
    print("Låg eller hög")
    print("Jämnt eller udda")
    print("Svart eller röd")
    print("Eller ett specifikt nummer.")
    print()
    val = input("")
    if val == "Låg" or val == "låg":
        bet_val = "låg"
    elif val == "Hög" or val == "hög":
        bet_val = "hög"
    elif val == "Jämnt" or val == "jämnt":
        bet_val = "jämnt"
    elif val == "Udda" or val == "udda":
        bet_val = "udda"
    elif val == "Svart" or val == "svart":
        bet_val = "svart"
    elif val == "Röd" or val == "röd":
        bet_val = "röd"
    elif val.isdigit() == True:
        val = int(val)
        if val < 0 or val > 36:
            print("Fel")
            continue
        else:
            bet_val = lista[val]
    elif val == "pengar":
        pengar += 1000
        continue
    else:
        print("Fel, gör ett riktigt val")
        continue

    # hur mycket ska bettas

    print()
    print(Fore.WHITE + "Hur mycket pengar vill du betta?")
    print()
    bet = input("")
    print()
    if bet.isdigit() == True:
        bet = int(bet)
        if bet > pengar or bet < 1:
            print("Skriv en riktig summa")
            continue
        else:
            pengar = pengar - bet
            print("Du har nu " + Fore.GREEN + f"{pengar}" + Fore.WHITE + " kr.")
            print()
    else:
        print("Skriv en riktigt summa.")
        continue

    # "snurrandet" av roulettehjulet

    result = str(randint(0, 36))

    for i in range(10):
        r = str(randint(0, 36))
        print(nummer_till_farg[r] + str(r))
        sleep(0.2)
    
    print()
    print(nummer_till_farg[(result)] + (result))
    sleep(1)

    
    # utbetalning
    

    if result in red_numbers and bet_val == "röd":
        pengar += 2*bet
        print(Fore.WHITE + "Du har nu " + Fore.GREEN + f"{pengar}" + Fore.WHITE + " kr.")
    elif result in black_numbers and bet_val == "svart":
        pengar += 2*bet
        print(Fore.WHITE + "Du har nu " + Fore.GREEN + f"{pengar}" + Fore.WHITE + " kr.")
    elif int(result) % 2 == 0 and int(result) != 0 and bet_val == "jämnt":
        pengar += 2*bet
        print(Fore.WHITE + "Du har nu " + Fore.GREEN + f"{pengar}" + Fore.WHITE + " kr.")
    elif int(result) % 2 != 0 and bet_val == "udda":
        pengar += 2*bet
        print(Fore.WHITE + "Du har nu " + Fore.GREEN + f"{pengar}" + Fore.WHITE + " kr.")
    elif int(result) >= 19 and int(result) <= 36 and bet_val == "hög":
        pengar += 2*bet
        print(Fore.WHITE + "Du har nu " + Fore.GREEN + f"{pengar}" + Fore.WHITE + " kr.")
    elif int(result) >= 1 and int(result) <= 18 and bet_val == "låg":
        pengar += 2*bet
        print(Fore.WHITE + "Du har nu " + Fore.GREEN + f"{pengar}" + Fore.WHITE + " kr.")
    elif result == bet_val:
        pengar += 36*bet
        print(Fore.WHITE + "Du har nu " + Fore.GREEN + f"{pengar}" + Fore.WHITE + " kr.")
    else:
        print()
        print(Fore.RED + "Du vann tyvär ingenting.")
        sleep(1)
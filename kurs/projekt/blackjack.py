from random import randint
from time import sleep
from colorama import Fore

pengar = 100

def värde(hand):

    hand_värde = 0
    A = 0

    for kort in hand:
        if kort.isdigit() == False:
            if kort != "A":
                hand_värde += 10
            else:
                # A -> 1/11
                A += 1
        else:
            hand_värde += int(kort)
    if A > 0:
        for a in range(A):
            if hand_värde < 11:
                hand_värde += 11
            else:
                hand_värde += 1

    return (hand_värde)

def vinna(bet, hand):
    uppdatera_dealer_hand()
    uppdatera_du_hand()

    multi = 0
    if len(hand) == 2 and värde(hand) == 21:
        print()
        print(Fore.YELLOW + "blackjack")
        # blackjack
        multi = 1.5
    else:
        multi = 1
    vinst = int(bet*multi)
    print()
    sleep(1)
    print(Fore.WHITE + "du vann " + Fore.GREEN + f"{vinst}")
    sleep(2)
    return vinst


def förlora():
    uppdatera_dealer_hand()
    uppdatera_du_hand()
    sleep(1)
    print(Fore.WHITE + "du förlorade " + Fore.RED + f"{bet}")
    sleep(2)


def dealer_hit(hand):
    while värde(hand) < 17:
        dealer_kort.append(kort[randint(0, len(kort)-1)])
        
    

while True:
    kort = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]

    print(Fore.WHITE + "--------------------------")
    for i in range(31):
        print()


    print()
    print(Fore.WHITE + "pengar: " + Fore.GREEN + f"{pengar}")
    print()
    bet = input(Fore.WHITE + "hur mycket bettar du? ")
    print()
    if bet.isdigit() == True:
        bet = int(bet)
        if bet > pengar or bet < 1:
            print("skriv ett riktigt tal")
            continue
        else:
            pengar -= bet
    elif bet == "pengar":
        pengar += 100
        continue
    else:
        print("skriv ett riktigt tal")
        continue

    print("--------------------------")
    
    dealer_kort = []
    dealer_kort.append(kort[randint(0, len(kort)-1)])
    
    du_kort = []
    du_kort.append(kort[randint(0, len(kort)-1)])
    du_kort.append(kort[randint(0, len(kort)-1)])

    def uppdatera_dealer_hand():
            print(Fore.WHITE + "--------------------------")
            for i in range(12):
                print()
            print("pengar: " + Fore.GREEN + f"{pengar}")
            print(Fore.WHITE + "bet: " + Fore.GREEN +  f"{bet}")
            for i in range(3):
                print()
            print(Fore.WHITE + "ta -> " + Fore.CYAN + "q")
            print(Fore.WHITE + "stanna -> " + Fore.CYAN + "w")
            print(Fore.WHITE + "dubbla -> " + Fore.CYAN + "e")
            print(Fore.WHITE + "splitta -> " + Fore.CYAN + "r " + Fore.WHITE + "(funkar inte än)")
            for i in range(5):
                print()
            dealer_hand = Fore.WHITE + ""
            for kort in dealer_kort:
                dealer_hand += f"{str(kort)} "
            if len(dealer_kort) == 1:
                print(Fore.WHITE + f"dealer: {dealer_hand} X")
            else:
                print(Fore.WHITE + f"dealer: {dealer_hand}")
            print("värde: " + Fore.MAGENTA + f"{värde(dealer_kort)}")
            print()
    
    def uppdatera_du_hand():
            du_hand = ""
            for kort in du_kort:
                du_hand += f"{str(kort)} "
            print(Fore.WHITE + f"du: {du_hand}")
            print("värde: " + Fore.MAGENTA + f"{värde(du_kort)}")
            print()


    runda = True
    
    while runda == True:

        uppdatera_dealer_hand()
        uppdatera_du_hand()


        val = input(Fore.WHITE + "")
        
        # q -> hit
        # w -> stand
        # e -> double
        # r -> split

        if val == "q":
            # hit
            print()
            du_kort.append(kort[randint(0, len(kort)-1)])
            if värde(du_kort) == 21:
                pengar += bet + vinna(bet, du_kort)
                runda = False
            elif värde(du_kort) > 21:
                # bust
                förlora()
                runda = False
            else:
                continue

        elif val == "w":
            # stand
            print()
            dealer_hit(dealer_kort)
            if värde(dealer_kort) > 21:
                pengar += bet + vinna(bet, du_kort)
            elif värde(dealer_kort) < 22 and värde(dealer_kort) > värde(du_kort):
                förlora()
            elif värde(dealer_kort) < värde(du_kort):
                pengar += bet + vinna(bet, du_kort)
            elif värde(dealer_kort) == värde(du_kort):
                # push
                pengar += bet
                uppdatera_dealer_hand()
                uppdatera_du_hand()

                print(Fore.CYAN + "push")
                sleep(3)
            runda = False

        elif val == "e":
            # double
            print()
            if pengar >= bet:
                pengar -= bet
                bet += bet
                du_kort.append(kort[randint(0, len(kort)-1)])
                if värde(du_kort) == 21:
                    pengar += bet + vinna(bet, du_kort)
                    runda = False
                elif värde(du_kort) > 21:
                    # bust
                    förlora()
                    runda = False
                else:
                    continue
            else:
                print("inte tillräckligt med pengar")

        elif val == "r":
            # split
            print()
        else:
            print("gör ett riktigt beslut")
            continue


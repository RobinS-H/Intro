from random import randint
from random import uniform
from colorama import Fore


cash = 100
print(Fore.WHITE + "Cash = " + Fore.GREEN + f"{cash}")

while True:
    print()
    antal = input(Fore.WHITE + "How many cases do you want to open? ")
    print()
    if antal.isdigit() == True:
        antal = int(antal)
        if antal < 1 or antal > 100000:
            print("Type a number between 1 and 100 000.")
        else:
            gold = 0
            red = 0
            pink = 0
            purple = 0
            blue = 0
            for i in range(antal):
                number = randint(1, 10000)
                if number < 27:
                    print(Fore.LIGHTYELLOW_EX + "GOLD")
                    gold += 1
                    cash += randint(100, 500)
                elif number < 91 and number >= 27:
                    print(Fore.LIGHTRED_EX + "RED")
                    red += 1
                    cash += randint(10, 100)
                elif number < 411 and number >= 91:
                    print(Fore.LIGHTMAGENTA_EX + "PINK")
                    pink += 1
                    cash += randint(2, 10)
                elif number < 2008 and number >= 411:
                    print(Fore.MAGENTA + "PURPLE")
                    purple += 1
                    cash += uniform(0.5, 2)
                else:
                    print(Fore.BLUE + "BLUE")
                    blue += 1
                    cash += uniform(0, 0.5)
            cash = cash - 2*antal
            print()
            print(Fore.WHITE + "Total cases opened: " + Fore.GREEN + f"{antal}")
            print()
            if cash > 0:
                print(Fore.WHITE + "Cash = " + Fore.GREEN + f"{int(cash)}")
            else:
                print(Fore.WHITE + "Cash = " + Fore.RED + f"{int(cash)}")
            print()
            print(Fore.WHITE + "Golds opened: " + Fore.LIGHTYELLOW_EX + f"{gold} ({int(10000*gold/antal)/100}%)")
            print(Fore.WHITE + "Reds opened: " + Fore.LIGHTRED_EX + f"{red} ({int(10000*red/antal)/100}%)")
            print(Fore.WHITE + "Pinks opened: " + Fore.LIGHTMAGENTA_EX + f"{pink} ({int(10000*pink/antal)/100}%)")
            print(Fore.WHITE + "Purples opened: " + Fore.MAGENTA + f"{purple} ({int(10000*purple/antal)/100}%)")
            print(Fore.WHITE + "Blues opened: " + Fore.BLUE + f"{blue} ({int(10000*blue/antal)/100}%)")
                
    else:
        print("Type a number.")
        continue
    
    

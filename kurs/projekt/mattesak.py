from random import randint


def loop(räknesätt):
    while True:
        tal1 = randint(1, 100)
        tal2 = randint(1, 100)
        if räknesätt == "multiplikation":
            print(f"Vad är {tal1} x {tal2}?")
            tal3 = tal1 * tal2
        elif räknesätt == "addition":
            tal3 = tal1 + tal2
            print(f"Vad är {tal1} + {tal2}?")
        else:
            tal3 = tal1 - tal2
            print(f"Vad är {tal1} - {tal2}?")
        svar = input("Svar: ")
        if svar.isdigit():
            svar = int(svar)
            if svar == tal3:
                print(f"Korrekt, svaret var {tal3}")
                print()
                continue
            else:
                print(f"Försök igen, rätt svar var {tal3}")
                continue
        else:
            if svar == "quit":
                print("Tack för att du har spelat")
                exit
            else:
                print(f"Försök igen, rätt svar var {tal3}.")
                print()
                continue

print("Vilket läge vill du ha?")
print("Skriv 1 för multiplikation")
print("Skriv 2 för addition")
print("Skriv 3 för subtraktion")
print()
val = input("Svar: ")
if val.isdigit():
    val = int(val)
    if val == 1 or val == 2 or val == 3:
        if val == 1:
            print()
            print("Du valde multiplikation")
            print()
            loop("multiplikation")
        elif val == 2:
            print()
            print("Du valde addition")
            print()
            loop("addition")
        else:
            print()
            print("Du valde subtraktion")
            print()
            loop("subtraktion")
    else:
        print("Skriv antingen 1, 2 eller 3")
        
else:
    print("Skriv antingen 1, 2 eller 3.")
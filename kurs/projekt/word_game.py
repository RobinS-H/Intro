
from random import randint
from colorama import Fore

print("PICK A LANGUAGE")
print("1 = ENGLISH")
print("2 = SWEDISH")
language = input("")

if language == "1":
    file = open("C:/Users/07rose04/OneDrive - Stenungsunds Kommun/Kurser/Programmering 1/Intro/kurs/projekt/dict.txt.txt", encoding="utf-8")
    ord_lista = file.read().split()
    file.close()
    print(Fore.WHITE + "HARD -> ALL LETTERS")
    print("EASY -> WITHOUT J, Q, X, Y, Z")
    print("1 FOR HARD")
    print("2 FOR EASY")
    val = input("")
elif language == "2":
    file = open("C:/Users/07rose04/OneDrive - Stenungsunds Kommun/Kurser/Programmering 1/Intro/kurs/projekt/swe_wordlist.txt", encoding="utf-8")
    ord_lista = file.read().split()
    file.close()
    print(Fore.WHITE + "SVÅR -> ALLA BOKSTÄVER")
    print("ENKEL -> UTAN J, Q, X, Y, Z")
    print("1 FÖR SVÅR")
    print("2 FÖR ENKEL")
    val = input("")
else:
    print("Pick either 1 or 2")


skrivna_ord = []
bokstäver = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
bokstäver2 = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "K", "L", "M", "N", "O", "P", "R", "S", "T", "U", "V", "W"]
combo = 0


if val == "1" or val == "2":
    while True:
        w = 0
        l = 0
        if val == "1":
            b1 = randint(0, 25)
            b2 = randint(0, 25)
            prompt = bokstäver[b1] + bokstäver[b2]
        elif val == "2":
            b1 = randint(0, 20)
            b2 = randint(0, 20)
            prompt = bokstäver2[b1] + bokstäver2[b2]
        else:
            print(Fore.RED + "Error")
        print(Fore.WHITE + prompt)
        ord = input(Fore.WHITE + "")
        for x in ord_lista:
            if x == ord or x.lower() == ord:
                if prompt in ord or prompt.lower() in ord:
                    for y in skrivna_ord:
                        if y == ord:
                            l = 1
                            print(Fore.RED + "Already used")
                            continue
                    if l == 0:
                        print(Fore.GREEN + "+ 1")
                        combo += 1
                        print(f"{combo}x")
                        skrivna_ord.append(ord)
                        w = 1
                        continue
                    else: 
                        continue
                else:
                    continue
        if w == 0:
            print(Fore.RED + "-")
            combo = 0
            continue
        else:
            continue
else:
    print("TYPE EITHER 1 OR 2")
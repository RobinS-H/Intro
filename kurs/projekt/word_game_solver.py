from colorama import Fore

print("1 för engelska")
print("2 för svenska")

val = input("")

if val == "1":
    file = open("C:/Users/07rose04/OneDrive - Stenungsunds Kommun/Kurser/Programmering 1/Intro/kurs/projekt/dict.txt.txt", encoding="utf-8")
    ord_lista = file.read().split()
    file.close()
elif val == "2":
    file = open("C:/Users/07rose04/OneDrive - Stenungsunds Kommun/Kurser/Programmering 1/Intro/kurs/projekt/swe_wordlist.txt", encoding="utf-8")
    ord_lista = file.read().split()
    file.close()
else:
    print("1 eller 2")


while True:
    valda_ord_lista = []
    print()
    print()
    prompt = input(Fore.WHITE + "")
    for ord in ord_lista:
        if prompt in ord or prompt.upper() in ord:
            valda_ord_lista.append(ord)
    max_längd = 0
    min_längd = 999
    for valda_ord in valda_ord_lista:
        if len(valda_ord) > max_längd:
            max_längd = len(valda_ord)
            längsta_ordet = valda_ord
        if len(valda_ord) < min_längd:
            min_längd = len(valda_ord)
            kortaste_ordet = valda_ord
    print()
    if max_längd == 0 and min_längd == 999:
        print(Fore.LIGHTRED_EX + "no word found.")
    else:
        print(Fore.LIGHTBLUE_EX + f"{längsta_ordet}")
        print()
        print(Fore.LIGHTMAGENTA_EX + f"{kortaste_ordet}")
        print()
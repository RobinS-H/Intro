file = open("C:/Users/07rose04/OneDrive - Stenungsunds Kommun/Kurser/Programmering 1/Intro/kurs/projekt/swe_wordlist.txt", encoding="utf-8")
ord_lista = file.read().split()
file.close()

while True:
    alfabet = ['E', 'A', 'N', 'R', 'T', 'S', 'I', 'L', 'D', 'O', 'M', 'K', 'G', 'V', 'H', 'F', 'U', 'P', 'Ä', 'B', 'C', 'Å', 'Ö', 'Y', 'J', 'X', 'W', 'Z', 'Q']
    for i in range(len(alfabet)):
        alfabet[i] = alfabet[i].lower()
    bokstäver = list(input())
    for bokstav in bokstäver:
        if bokstav.lower() in alfabet:
            alfabet.remove(bokstav)
    
    for ord in ord_lista:
        for bokstav in alfabet:
            if bokstav in ord.lower():
                ord_lista.remove(ord)
                break
                    

    for i in range(20):
        print(ord_lista[i])        

    print()

    print(bokstäver)

    print()

    max_längd = 0
    for ord in ord_lista:
        if len(ord) > max_längd:
            max_längd = len(ord)
            längsta_ord = ord

    print(längsta_ord)

            
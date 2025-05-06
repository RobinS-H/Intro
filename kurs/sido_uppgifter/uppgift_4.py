from random import randint

while True:
    svar = input("Skriv ja för att kasta: ")
    if svar == "ja" or svar == "JA" or svar == "Ja":
        nummer1 = randint(1, 6)
        nummer2 = randint(1, 6)
        nummer3 = randint(1, 6)
        if nummer1 == nummer2 and nummer1 == nummer3:
            print("Alla talen är samma: " + str(nummer1))
        else:
            print("Alla talen blev inte samma.")
            print("Tal 1: " + str(nummer1))
            print("Tal 2: " + str(nummer2))
            print("Tal 3: " + str(nummer3))
        print("Skriv ja för att försöka igen")
    else:
        exit
        

    


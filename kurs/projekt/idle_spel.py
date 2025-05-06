from time import sleep
import threading



def spel_loop():
    global spel
    pengar = 200
    ökning = 1
    mult = 1

    spel = 1
    while spel == 1:
        print("---------------------------------")
        for i in range(15):
            print()
        print(f"Pengar: {pengar}")
        pengar += ökning * mult
        print(f"(+ {ökning} * {mult})")
        for i in range(7):
            print()

        print("Tryck enter för att komma till uppgraderingarna.")

        for i in range(8):
            print()
        print("---------------------------------")
        sleep(1)
        if spel == 0:
            affär = 1
            while affär == 1:
                print("---------------------------------")
                for i in range (15):
                    print()
                print(f"Du har {pengar} kr.")
                print("Vad vill du uppgradera?")
                for i in range(2):
                    print()
                print("Uppgraderingar:")
                print()
                print(f"Ökning (+1), kostnad: {ökning * 100}")
                print(f"Mult (+1), kostnad: {mult * 200}")
                print()
                print("Skriv 1 för att uppgradera ökning och skriv 2 för att uppgradera mult.")
                for i in range(4):
                    print()
                print("Skriv exit för att gå tillbaks.")
                for i in range(3):
                    print()
                print("---------------------------------")
                affär_val = input("")
                if affär_val == "1":
                    if pengar >= (ökning * 100):
                        pengar -= (ökning * 100)
                        ökning += 1
                if affär_val == "2":
                    if pengar >= (mult * 200):
                        pengar -= (mult * 200)
                        mult += 1
                if affär_val == "exit" or affär_val == "Exit" or affär_val == "EXIT":
                    affär = 0
                    spel = 1



def lämna_loop():
    global spel
    while True:
        while spel == 1:
            input("")
            spel = 0
    


x = threading.Thread(target=spel_loop)
y = threading.Thread(target=lämna_loop)

x.start()
y.start()


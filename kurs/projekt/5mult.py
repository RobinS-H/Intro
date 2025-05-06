from time import sleep
import threading



def spel_loop():
    global spel
    pengar = 100
    mult1 = 1
    mult2 = 1
    mult3 = 1
    mult4 = 1
    mult5 = 1

    spel = 1
    while spel == 1:
        print("---------------------------------")
        for i in range(15):
            print()
        print(f"Pengar: {int(pengar)}")
        pengar += mult1*mult2*mult3*mult4*mult5
        print(f"(+ {mult1} * {mult2} * {mult3} * {mult4} * {mult5} (= {mult1*mult2*mult3*mult4*mult5}))")
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
                for i in range (12):
                    print()
                print(f"Du har {int(pengar)} kr.")
                print("Vad vill du uppgradera?")
                for i in range(2):
                    print()
                print("Uppgraderingar:")
                print()
                print(f"Mult1 (+0.5), kostnad: {int(mult1 * 100)}")
                print(f"Mult2 (+0.5), kostnad: {int(mult2 * 1000)}")
                print(f"Mult3 (+0.5), kostnad: {int(mult3 * 10000)}")
                print(f"Mult4 (+0.5), kostnad: {int(mult4 * 100000)}")
                print(f"Mult5 (+0.5), kostnad: {int(mult5 * 1000000)}")

                print()
                print("Skriv siffror för att uppgradera respektive mult.")
                for i in range(4):
                    print()
                print("Skriv exit för att gå tillbaks.")
                for i in range(3):
                    print()
                print("---------------------------------")
                affär_val = input("")
                if affär_val == "1":
                    if pengar >= (mult1 * 100):
                        pengar -= (mult1 * 100)
                        mult1 += 0.5
                if affär_val == "2":
                    if pengar >= (mult2 * 1000):
                        pengar -= (mult2 * 1000)
                        mult2 += 0.5
                if affär_val == "3":
                    if pengar >= (mult3 * 10000):
                        pengar -= (mult3 * 10000)
                        mult3 += 0.5
                if affär_val == "4":
                    if pengar >= (mult4 * 100000):
                        pengar -= (mult4 * 100000)
                        mult4 += 0.5
                if affär_val == "5":
                    if pengar >= (mult5 * 1000000):
                        pengar -= (mult5 * 1000000)
                        mult5 += 0.5
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
# (https://open.kattis.com/problems/3dprinter)

while True:
    print()
    printers = 1
    dagar = 0
    N = input("Hur många statyer? ")
    if N.isdigit() == True:
        N = int(N)
        if N >= 1 and N <= 10000:
            while N >= 2 * printers:
                # printa en ny printer
                printers += printers
                dagar += 1
            if N == printers:
                # lika många, gör statyer
                dagar += 1
                print(f"Det tog {dagar} dag(ar).")
                continue
            elif N > printers:
                # måste ta två dagar
                dagar += 2
                print(f"Det tog {dagar} dagar.")
                continue
            else:
                print("fel")
        else:
            print("Skriv ett nummer mellan 1 och 10 000.")
            continue
    else:
        print("Skriv ett nummer.")
        continue
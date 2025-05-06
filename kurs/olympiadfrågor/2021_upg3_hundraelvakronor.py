while True:
    sedlar = 0
    N = input("priset N? ")
    if N.isdigit() == True:
        N = int(N)
        if N >= 1 and N <= 1000000000:
            pris_kvar = N
            while pris_kvar > 0:
                if pris_kvar >= 111111111:
                    pris_kvar = pris_kvar - 111111111
                    sedlar = sedlar + 1
                    continue
                if pris_kvar >= 11111111:
                    pris_kvar = pris_kvar - 11111111
                    sedlar = sedlar + 1
                    continue
                if pris_kvar >= 1111111:
                    pris_kvar = pris_kvar - 1111111
                    sedlar = sedlar + 1
                    continue
                if pris_kvar >= 111111:
                    pris_kvar = pris_kvar - 111111
                    sedlar = sedlar + 1
                    continue
                if pris_kvar >= 11111:
                    pris_kvar = pris_kvar - 11111
                    sedlar = sedlar + 1
                    continue
                if pris_kvar >= 1111:
                    pris_kvar = pris_kvar - 1111
                    sedlar = sedlar + 1
                    continue
                if pris_kvar >= 111:
                    pris_kvar = pris_kvar - 111
                    sedlar = sedlar + 1
                    continue
                if pris_kvar >= 11:
                    pris_kvar = pris_kvar - 11
                    sedlar = sedlar + 1
                    continue
                if pris_kvar > 0:
                    pris_kvar = pris_kvar - 1
                    sedlar = sedlar + 1
                    continue
            print(f"Det tog {sedlar} sedlar.")
        else:
            print("Skriv ett nummer mellan 1 och 1 000 000 000")
            continue
    else:
        print("Skriv ett nummer.")
        continue
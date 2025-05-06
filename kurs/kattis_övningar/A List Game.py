while True:
    X = input("Välj ett nummer (1 000 - 1 000 000 000). ")
    if X.isdigit() == True:
        X = int(X)
        if X >= 1000 and X <= 1000000000:
            primtal = []
            while X % 2 == 0:
               primtal.append(2)
               X = X/2
            for i in range(3, int(X)):
                while X % i == 0:
                    primtal.append(i)
                    X = X/i
            print(primtal)
            print(len(primtal))
        else:
            print("Skriv ett nummer mellan 1 000 och 1 000 000 000.")
    else:
        print("Skriv ett nummer.")
        continue
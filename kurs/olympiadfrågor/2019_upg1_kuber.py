while True:
    N = input("Vad är talet N? ")
    if N.isdigit() == True:
        N = int(N)
        if N >= 2 and N <= 40:
            kuber = 0
            while N > 0:
                kuber = kuber + N**3
                N = N - 1
            print(kuber)
            print()
        else:
            print("Välj ett nummer mellan 2 och 40.")
    else:
        print("Skriv ett nummer.")
        continue
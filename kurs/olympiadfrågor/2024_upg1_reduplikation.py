while True:
    ord = str(input("Ordet: "))

    if len(ord) < 1 or len(ord) > 9:
        print("Skriv ett ord med som högst 9 bokstäver")
        continue

    upprepningar = input("Upprepningar: ")

    if upprepningar.isdigit() == True:
        upprepningar = int(upprepningar)
    else:
        print("Skriv ett positivt nummer under 9 istället.")
        continue

    if upprepningar > 0 and upprepningar <= 9:
        print(ord * upprepningar)
    else:
        print("Du kan bara upprepa ordet 1-9 gånger.")
        continue
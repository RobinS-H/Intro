while True:
    print("(Svara i gram/kvadratmeter)")
    kuvert_ytvikt = input("Vad är kuvertets ytvikt? ")

    if kuvert_ytvikt.isdigit() == True:
        kuvert_ytvikt = int(kuvert_ytvikt)
        if kuvert_ytvikt >= 50 and kuvert_ytvikt <= 200:
            print()
        else:
            print("Skriv ett nummer mellan 50 och 200.")
            continue
    else:
        print("Skriv ett nummer.")
        continue

    affisch_ytvikt = input("Vad är affischens ytvikt? ")

    if affisch_ytvikt.isdigit() == True:
        affisch_ytvikt = int(affisch_ytvikt)
        if affisch_ytvikt >= 50 and affisch_ytvikt <= 200:
            print()
        else:
            print("Skriv ett nummer mellan 50 och 200.")
            continue
    else:
        print("Skriv ett nummer.")
        continue

    blad_ytvikt = input("Vad är informationsbladets ytvikt? ")

    if blad_ytvikt.isdigit() == True:
        blad_ytvikt = int(blad_ytvikt)
        if blad_ytvikt >= 50 and blad_ytvikt <= 200:
            print()
        else:
            print("Skriv ett nummer mellan 50 och 200.")
            continue
    else:
        print("Skriv ett nummer.")
        continue

    kuvert_vikt = kuvert_ytvikt * 2 * 0.229 * 0.324
    affisch_vikt = affisch_ytvikt * 2 * 0.297 * 0.420
    blad_vikt = blad_ytvikt * 0.210 * 0.297

    print("Totala vikten blir i gram:")
    print(kuvert_vikt + affisch_vikt + blad_vikt)
    print()
    continue
bokstäver = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n" "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

while True:
    högst = 1

    sträng = input("Vad är strängen? ")

    if len(sträng) > 32 or len(sträng) < 1:
        print("Skriv en sträng med minst en bokstav och som längst 32.")
        continue

    if sträng.isalpha() != True:
        print("Skriv bara bokstäver mellan a-z")
        continue

    k = input("Vad är det maximala antalet bokstäver som kan klippas om gången? ")

    if k.isdigit() == True:
        k = int(k)
        if k < 1:
            print("Skriv inte ett nummer under 1.")
            continue
    else:
        print("Skriv ett nummer.")
        continue

    for i in range(25):
        antal_av_bokstav = sträng.count(bokstäver[i])
        if antal_av_bokstav > högst:
            högst = antal_av_bokstav
            sparad_index = i
    print(högst)
    print(bokstäver[sparad_index])

    # vet inte mer


while True:
    morötter = 40

    TorsTid = input("Hur lång tid tar det Tor att äta en morot? ")

    if TorsTid.isdigit() == True:
        TorsTid = int(TorsTid)
        if TorsTid < 1 or TorsTid > 100:
            print("Välj ett nummer mellan 1 och 100.")
            continue
    else:
        print("Skriv ett nummer mellan 1 och 100.")
        continue

    MorsTid = input("Hur lång tid tar det hans Mor att äta en morot? ")
    
    if MorsTid.isdigit() == True:
        MorsTid = int(MorsTid)
        if MorsTid < 1 or MorsTid > 100:
            print("Välj ett nummer mellan 1 och 100.")
            continue
    else:
        print("Skriv ett nummer mellan 1 och 100.")
        continue

    TorMorötter = 0
    MorMorötter = 0
    tid = 0

    while morötter > 0:
        if tid % TorsTid == 0 or morötter == 40:
            morötter = morötter - 1
            TorMorötter = TorMorötter + 1
        if tid % MorsTid == 0 or morötter == 39:
            morötter = morötter - 1
            MorMorötter = MorMorötter +1
        tid = tid + 1
        if morötter == -1:
            TorMorötter = TorMorötter -1
            MorMorötter = MorMorötter -1
    
    print(f"Tors morötter: {TorMorötter}")
    print(f"Tors Mors morötter: {MorMorötter}")
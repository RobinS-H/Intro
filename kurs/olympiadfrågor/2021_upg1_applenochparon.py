while True:

    äpplen_sålda = input("Hur många äpplen såldes? ")

    if äpplen_sålda.isdigit() == True:
        äpplen_sålda = int(äpplen_sålda)
    else:
        print("Skriv ett nummer.")
        continue

    päron_sålda = input("Hur många päron såldes? ")

    if päron_sålda.isdigit() == True:
        päron_sålda = int(päron_sålda)
    else:
        print("Skriv ett nummer.")
        continue
    
    Axel_känat = äpplen_sålda * 7
    Petra_känat = päron_sålda * 13

    if Axel_känat > Petra_känat:
        print("Axel känade mest.")
        print(f"Axel känade {Axel_känat}kr medan Petra känade {Petra_känat}kr.")
    elif Petra_känat > Axel_känat:
        print("Petra känade mest")
        print(f"Petra känade {Petra_känat}kr medan Axel känade {Axel_känat}kr.")
    else:
        print("Båda två känade lika mycket.")
        print(f"Axel sålde {äpplen_sålda} för 7kr/st medan Petra sålde {päron_sålda} för 13kr/st.")
        print(f"Båda känade altså {Axel_känat}kr.")
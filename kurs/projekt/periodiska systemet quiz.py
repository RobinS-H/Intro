import random as rand
from colorama import Fore
from time import sleep




elements_list = ['H', 'He', 'Li', 'Be', 'B', 'C', 'N', 'O', 'F', 'Ne', 'Na', \
                 'Mg', 'Al', 'Si', 'P', 'S', 'Cl', 'Ar', 'K', 'Ca', 'Sc', 'Ti', \
                 'V', 'Cr', 'Mn', 'Fe', 'Co', 'Ni', 'Cu', 'Zn', 'Ga', 'Ge', \
                 'As', 'Se', 'Br', 'Kr', 'Rb', 'Sr', 'Y', 'Zr', 'Nb', 'Mo', \
                 'Tc', 'Ru', 'Rh', 'Pd', 'Ag', 'Cd', 'In', 'Sn', 'Sb', 'Te', \
                 'I', 'Xe', 'Cs', 'Ba', 'La', 'Ce', 'Pr', 'Nd', 'Pm', 'Sm', \
                 'Eu', 'Gd', 'Tb', 'Dy', 'Ho', 'Er', 'Tm', 'Yb', 'Lu', 'Hf', \
                 'Ta', 'W', 'Re', 'Os', 'Ir', 'Pt', 'Au', 'Hg', 'Tl', 'Pb', \
                 'Bi', 'Po', 'At', 'Rn', 'Fr', 'Ra', 'Ac', 'Th', 'Pa', 'U', \
                 'Np', 'Pu', 'Am', 'Cm', 'Bb', 'Ct', 'Es', 'Fm', 'Md', 'No', \
                 'Lr', 'Rf', 'Db', 'Sg', 'Bh', 'Hs', 'Mt', 'Ds', 'Rg', 'Cn', \
                 'Nh', 'Fl', 'Mc', 'Lv', 'Ts', 'Og']

elements_name_list = ["Väte", "Helium", "Litium", "Beryllium", "Bor", "Kol", "Kväve", "Syre", "Fluor", "Neon", "Natrium", "Magnesium", "Aluminium", "Kisel", "Fosfor", "Svavel", "Klor", "Argon", "Kalium", "Kalcium", "Skandium", "Titan", "Vanadin", "Krom", "Mangan", "Järn", "Kobolt", "Nickel", "Koppar", "Zink", "Gallium", "Germanium", "Arsenik", "Selen", "Brom", "Krypton", "Rubidium", "Strontium", "Yttrium", "Zirkonium", "Niob", "Molybden", "Teknetium", "Rutenium", "Rodium", "Palladium", "Silver", "Kadmium", "Indium", "Tenn", "Antimon", "Tellur", "Jod", "Xenon", "Cesium", "Barium", "Lantan", "Cerium", "Praseodym", "Neodym", "Prometium", "Samarium", "Europium", "Gadolinium", "Terbium", "Dysprosium", "Holmium", "Erbium", "Tulium", "Ytterbium", "Lutetium", "Hafnium", "Tantal", "Volfram", "Rhenium", "Osmium", "Iridium", "Platina", "Guld", "Kvicksilver", "Tallium", "Bly", "Vismut", "Polonium", "Astat", "Radon", "Francium", "Radium", "Aktinium", "Torium", "Protaktinium", "Uran", "Neptunium", "Plutonium", "Americium", "Curium", "Berkelium", "Californium", "Einsteinium", "Fermium", "Mendelevium", "Nobelium", "Lawrencium", "Rutherfordium", "Dubnium", "Seaborgium", "Bohrium", "Hassium", "Meitnerium", "Darmstadtium", "Röntgenium", "Copernicium", "Nihonium", "Flerovium", "Moskovium", "Livermorium", "Tenness", "Oganesson"]

elements_name_lowercase_list = ["väte", "helium", "litium", "beryllium", "bor", "kol", "kväve", "syre", "fluor", "neon", "natrium", "magnesium", "aluminium", "kisel", "fosfor", "svavel", "klor", "argon", "kalium", "kalcium", "skandium", "titan", "vanadin", "krom", "mangan", "järn", "kobolt", "nickel", "koppar", "zink", "gallium", "germanium", "arsenik", "selen", "brom", "krypton", "rubidium", "strontium", "yttrium", "zirkonium", "niob", "molybden", "teknetium", "rutenium", "rodium", "palladium", "silver", "kadmium", "indium", "tenn", "antimon", "tellur", "jod", "xenon", "cesium", "barium", "lantan", "cerium", "praseodym", "neodym", "prometium", "samarium", "europium", "gadolinium", "terbium", "dysprosium", "holmium", "erbium", "tulium", "ytterbium", "lutetium", "hafnium", "tantal", "volfram", "rhenium", "osmium", "iridium", "platina", "guld", "kvicksilver", "tallium", "bly", "vismut", "polonium", "astat", "radon", "francium", "radium", "aktinium", "torium", "protaktinium", "uran", "neptunium", "plutonium", "americium", "curium", "berkelium", "californium", "einsteinium", "fermium", "mendelevium", "nobelium", "lawrencium", "rutherfordium", "dubnium", "seaborgium", "bohrium", "hassium", "meitnerium", "darmstadtium", "röntgenium", "copernicium", "nihonium", "flerovium", "moskovium", "livermorium", "tenness", "oganesson"]

menu_loop = 1


while menu_loop > 0:
    streak = 0
    loop1 = False
    loop2 = False
    loop3 = False
    loop4 = False
    loop5 = False
    loop6 = False
    print(Fore.LIGHTWHITE_EX + "Välj läge:")
    print()
    print("Tecken -> Nummer: 1")
    print("Nummer -> Tecken: 2")
    print("Namn -> Nummer: 3")
    print("Namn -> Tecken: 4")
    print("Nummer -> Namn: 5")
    print("Tecken -> Namn: 6")
    print()
    print("För att komma tillbaka till menyn, skriv quit närsomhelst")
    sleep(2)
    print()
    choice = input("Skriv siffran för att välja läge: ")
    if choice == "1":
        loop1 = True
    elif choice == "2":
        loop2 = True
    elif choice == "3":
        loop3 = True
    elif choice == "4":
        loop4 = True
    elif choice == "5":
        loop5 = True
    elif choice == "6":
        loop6 = True

    if loop1 == False and loop2 == False and loop3 == False and loop4 == False and loop5 == False and loop6 == False:
        print(Fore.RED + "Skriv en siffra mellan 1-6 för att välja speltyp.")
        sleep(2)


    while loop1 == True:
        number = rand.randint(0, 117)
        element = elements_list[number]
        print()
        answer = input(Fore.LIGHTWHITE_EX + f"Vilket atomnummer har {element}? ")
        if answer.isdigit() and int(answer) == number + 1:
            print(Fore.GREEN + "Korrekt!")
            streak += 1
            print(f"x{streak}")
        elif answer == "quit":
            menu_loop = 1
            loop1 = False
        else:
            print(Fore.RED + f"Fel, rätt svar var {number + 1}.")
            print(f"Du hade en streak på x{streak}")
            streak = 0
        print()

    while loop2 == True:
        number = rand.randint(0, 117)
        element = elements_list[number]
        print()
        answer = input(Fore.LIGHTWHITE_EX + f"Vilket tecken har atomnummret {number + 1}? ")
        if answer == element:
            print(Fore.GREEN + "Korrekt!")
            streak += 1
            print(f"x{streak}")
        elif answer == "quit":
            menu_loop = 1
            loop2 = False
        else:
            print(Fore.RED + f"Fel, rätt svar var {element}.")
            print(f"Du hade en streak på x{streak}")
            streak = 0
        print()

    while loop3 == True:
        number = rand.randint(0, 117)
        element = elements_name_list[number]
        print()
        answer = input(Fore.LIGHTWHITE_EX + f"Vilket atomnummer har grundämnet {element}? ")
        if answer.isdigit() and int(answer) == number + 1:
            print(Fore.GREEN + "Korrekt!")
            streak += 1
            print(f"x{streak}")
        elif answer == "quit":
            menu_loop = 1
            loop3 = False
        else:
            print(Fore.RED + f"Fel, rätt svar var {number + 1}.")
            print(f"Du hade en streak på x{streak}")
            streak = 0
        print()

    while loop4 == True:
        number = rand.randint(0, 117)
        element = elements_name_list[number]
        print()
        answer = input(Fore.LIGHTWHITE_EX + f"Vilket tecken har grundämnet {element}? ")
        if answer == elements_list[number]:
            print(Fore.GREEN + "Korrekt!")
            streak += 1
            print(f"x{streak}")
        elif answer == "quit":
            menu_loop = 1
            loop4 = False
        else:
            print(Fore.RED + f"Fel, rätt svar var {elements_list[number]}.")
            print(f"Du hade en streak på x{streak}")
            streak = 0
        print()

    while loop5 == True:
        number = rand.randint(0, 117)
        element = elements_name_list[number]
        element2 = elements_name_lowercase_list[number]
        print()
        answer = input(Fore.LIGHTWHITE_EX + f"Vilket grundämne har atomnumret {number + 1}? ")
        if answer == element or answer == element2:
            print(Fore.GREEN + "Korrekt!")
            streak += 1
            print(f"x{streak}")
        elif answer == "quit":
            menu_loop = 1
            loop5 = False
        else:
            print(Fore.RED + f"Fel, rätt svar var {element}.")
            print(f"Du hade en streak på x{streak}")
            streak = 0
        print()

    while loop6 == True:
        number = rand.randint(0, 117)
        element = elements_name_list[number]
        element2 = elements_name_lowercase_list[number]
        print()
        answer = input(Fore.LIGHTWHITE_EX + f"Vilket grundämne har tecknet {elements_list[number]}? ")
        if answer == element or answer == element2:
            print(Fore.GREEN + "Korrekt!")
            streak += 1
            print(f"x{streak}")
        elif answer == "quit":
            menu_loop = 1
            loop6 = False
        else:
            print(Fore.RED + f"Fel, rätt svar var {element}.")
            print(f"Du hade en streak på x{streak}")
            streak = 0
        print()

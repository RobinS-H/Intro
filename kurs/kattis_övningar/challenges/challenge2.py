while True:
    lista = [input("Taggar? ")]
    lista = lista[0].split()
    if lista[0].isdigit() == True and len(lista) > 1:
        lista[0] = int(lista[0])
    else:
        print("Skriv två nummer.")
        continue
    if lista[1].isdigit() == True:
        lista[1] = int(lista[1])
    else:
        print("Skriv två nummer.")
        continue
    if lista[0] == lista[1] and lista[0] != 0:
        print(f"Even {lista[0]*2}")
    elif lista[0] > lista[1]:
        print(f"Odd {lista[0]*2}")
    elif lista[1] > lista[0]:
        print(f"Odd {lista[1]*2}")
    else:
        print("Not a moose.")
# C > B > A

siffror_lista = [str((input("Siffror? ")))]
bokstäver_lista = [str(input("Bokstäver? "))]

bokstäver_lista = bokstäver_lista[0].split()

siffror_lista = siffror_lista[0].split()

siffror_lista[0] = int(siffror_lista[0])
siffror_lista[1] = int(siffror_lista[1])
siffror_lista[2] = int(siffror_lista[2])

siffror_lista = sorted(siffror_lista)

klar_lista = []

bokstäver = ['A', 'B', 'C']

svar = []

for i in range(3):
    bokstav = bokstäver_lista[i]
    #hitta siffran
    # index för bokstav i bokstäver
    index =  bokstäver.index(bokstav)

    svar.append( siffror_lista[index])
print(f"Svar :  {svar}")
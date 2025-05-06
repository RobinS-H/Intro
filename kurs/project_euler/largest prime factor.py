num = 2
max = 1
lista = []
tal = 600851475143
for i in range(tal):
    if tal % num == 0:
        tal = tal / num
        lista.append(num)
        print(num)
    num += 1
print(lista)
for i in lista:
    if i > max:
        max = i
print(f"största: {max}")


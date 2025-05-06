tal1 = 1
tal2 = 2
lista = [1, 2]
sum = 0

while True:
    tal3 = tal1 + tal2
    tal1 = tal2
    tal2 = tal3
    if tal3 > 4000000:
        break
    else:
        lista.append(tal2)
for num in lista:
    if num % 2 == 0:
        sum += num
print(lista)
print(sum)

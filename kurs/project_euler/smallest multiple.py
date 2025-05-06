
klar = False
nummer = 0

print("test")

while klar == False:
    nummer +=1
    a = 0
    for i in range(20):
        i += 1
        if nummer % i != 0:
            continue
        else:
            a += 1
    if a >= 17:
        print(nummer)
    if a == 20:
        print(nummer)
        klar = True
        print("klar")
n = 0
max_terms = 0
max_i = 0

for i in range(1000000):
    terms = 0
    i += 1
    n = i
    while n != 1:
        if n % 2 == 0:
            # even
            n = n/2
            terms += 1
            if terms > max_terms:
                max_terms = terms
                max_i = i
        else:
            # odd
            n = 3*n + 1
            terms += 1
            if terms > max_terms:
                max_terms = terms
                max_i = i
print(max_i)
print(max_terms)
print("klar")

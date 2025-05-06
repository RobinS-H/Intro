num = 0
sum = 0

for i in range(999):
    num += 1
    if num % 5 == 0 or num % 3 == 0:
        sum += num
print(sum)
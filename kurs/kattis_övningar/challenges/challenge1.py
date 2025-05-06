while True:
    n = int(input("Hur många pizza slices? "))
    m = int(input("Hur många personer? "))
    print(f"{int((n-(n%m))/m)} slices var.")
    print(f"{n%m} slices kvar.")
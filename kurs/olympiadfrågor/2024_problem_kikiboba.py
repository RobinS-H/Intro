while True:
    ord = input("ord? ")
    if ord.count("b") > ord.count("k"):
        print(f"{ord} är ett boba-ord")
    elif ord.count("k") > ord.count("b"):
        print(f"{ord} är ett kiki-ord")
    elif ord.count("k") == ord.count("b") and ord.count("k") > 0:
        print(f"{ord} är ett boki-ord")
    else:
        print(f"{ord} är ett none-ord")
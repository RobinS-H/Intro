bas = 0
print("Vilken figur vill du beräkna arean av?")
svar = input("Fyrkant eller triangel: ")
if svar == "fyrkant" or svar == "Fyrkant":
    print("Du valde fyrkant")
    bas = int(input("Vad är basen? "))
    höjd = int(input("Vad är höjden? "))
    area = bas * höjd
    print("Arean blir: " + str(area))
    
elif svar == "triangel" or svar == "Triangel":
    print("Du valde triangel")
    bas = int(input("Vad är basen? "))
    höjd = int(input("Vad är höjden? "))
    area = (bas * höjd)
    area = area/2
    print("Arean blir: " + str(area))
else:
    print("Skriv triangel eller fyrkant")
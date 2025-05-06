def betyg_till_poäng(betyg):
    if betyg == "A":
        betyg = 20
    elif betyg == "B":
        betyg = 17.5
    elif betyg == "C":
        betyg = 15
    elif betyg == "D":
        betyg = 12.5
    elif betyg == "E":
        betyg = 10
    elif betyg == "F":
        betyg = 0
    else:
        print("Skriv bara en stor bokstav A-F.")
    return betyg

ämnen = ["Kemi 1", "Biologi 1", "Språk 3", "Svenska 1", "Engelska 5", "Matematik 1c", "Matematik 2c", "Matematik 3c"]

while True:
    merit = 0
    print("Skriv betygen nedan.")
    for ämne in ämnen:
        merit += betyg_till_poäng(input(f"{ämne}? "))
    print()
    print(f"Din merit med bonus merit blir: {merit/len(ämnen) + 2.5}")

from random import randint
from colorama import Fore

while True:
    tal = randint(1, 100)
    svar = input(Fore.WHITE + f"Vad är tredjeroten ur {tal**3}? ")
    if svar.isdigit() != True:
        print("Skriv ett nummer istället.")
        continue
    else:
        svar = int(svar)
        if svar == tal:
            print(Fore.GREEN + f"{svar} var rätt.")
        else:
            print(Fore.RED + f"{svar} var fel. Rätt svar var {tal}")
    
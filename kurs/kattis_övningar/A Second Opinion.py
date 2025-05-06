tid = int(input("Sekunder? "))
if tid > 3600:
    timmar = int(tid/3600)
    tid = tid - timmar*3600
else:
    timmar = 0
if tid > 60:
    minuter = int(tid/60)
    tid = tid - minuter*60
else:
    minuter = 0
print(f"{timmar} : {minuter} : {tid}")
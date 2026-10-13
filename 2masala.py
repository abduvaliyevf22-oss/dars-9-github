parol = input("Parol: ")

if len(parol) >= 8 and any(i.isupper() for i in parol) and any(i.islower() for i in parol) and any(i.isdigit() for i in parol) and " " not in parol:
    print("Parol to'g'ri")
else:
    print("Parol noto'g'ri")
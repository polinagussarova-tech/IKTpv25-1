
#paber, k‰‰rid ja kivi m‰ng 
import random

valikud=["kivi", "paber", "k‰‰rid"]
mangijad=["Inimene", "Robot"]
random.shuffle(mangijad)
print(f"M‰ngijate j‰rjekord: {mangijad}")
punktid={"Inimene": 0, "Robot": 0}
vooru_valikud=[]
vooru_tulemused=[]

while True:
    while True:
        kasutaja_valik = input("Sisesta kivi, paber vıi k‰‰rid: ").lower()
        if kasutaja_valik in valikud:
            break
        else:
            print("Vale valik! Palun proovi uuesti.")

    arvuti_valik=random.choice(valikud)
    print(f"Robot valis: {arvuti_valik}")

    vooru_valikud.append((kasutaja_valik, arvuti_valik))

    if kasutaja_valik==arvuti_valik:
        tulemus="Viik"
        print("Viik!")
    elif (kasutaja_valik=="kivi" and arvuti_valik == "k‰‰rid") or \
         (kasutaja_valik=="paber" and arvuti_valik == "kivi") or \
         (kasutaja_valik=="k‰‰rid" and arvuti_valik == "paber"):
        tulemus="Inimene vıitis"
        punktid["Inimene"]+=1
        print("Sa vıitsid!")
    else:
        tulemus="Robot vıitis"
        punktid["Robot"]+=1
        print("Robot vıitis!")

    vooru_tulemused.append(tulemus)

    print("Punktid:")
    print(f"Inimene: {punktid['Inimene']}")
    print(f"Robot: {punktid['Robot']}")

    uuesti=input("Kas m‰ngida j‰rgmine voor? (jah/ei): ").lower()
    if uuesti!="jah":
        break

print("M‰ng lıppes")
print(f"Lıplik tabel: {punktid}")


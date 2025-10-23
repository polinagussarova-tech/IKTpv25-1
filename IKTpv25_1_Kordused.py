#2.3 töö moodlist
print("Tere! Olen sinu uus sober - Python")

nimi=input("Palun sisesta oma nimi: ").strip()
print(f"{nimi}, oi kui ilus nimi! ")

try:
    soov=int(input(f"{nimi}! Kas leian Sinu keha indeksi? 0-ei, 1-jah =>"))
    if soov==1:
        print("Indeksi leidmine")

        while True:
            try:
                pikkus=int(input("Mis on sinu pikkus (cm)? "))
                if 0 < pikkus <= 250:
                    break
                else:
                    print("Pikkus peab olema vahemikus 0 kuni 250 cm!")
            except:
                print("Vale pikkuse formaat! Palun sisesta taisarv.")

        while True:
            try:
                 mass=float(input("Mis on sinu kehakaal (kg)? "))
                 if 0 < pikkus <= 250:
                     break
                 else:
                     print("Kehakaal peab olema vahemikus 0 kuni 250 kg!")
            except:
                print("Vale kehakaalise formaat! Palun sisesta taisarv")

        if pikkus>0 and mass>0:
            indeks = round(mass/(0.01*pikkus)**2, 2)
            print(f"{nimi}! Sinu keha indeks on: {indeks}")

            if indeks<16:
                hinnang="Tervisele ohtlik alakaal"
            elif 16<=indeks<19:
                hinnang="Alakaal"
            elif 19<=indeks<25:
                hinnang="Normaalkaal"
            elif 25<=indeks<30:
                hinnang = "Ulekaal"
            elif 30<=indeks<35:
                hinnang="Rasvumine"
            elif 35<=indeks<40:
                hinnang="Tugev rasvumine"
            else:
                hinnang="Tervisele ohtlik rasvumine"
            print(f"Hinnang: {hinnang}")
        else:
            print("Pikkus ja mass peavad olema positiivsed arvud!")

    elif soov==0:
        print("Kahju! See on vaga kasulik info!")
    else:
        print("Vale valik. Saab valida ainult 1 voi 0")
except:
    print("Vale soov!")

print(f"Kohtumiseni, {nimi}! Igavesti sinu, Python!")

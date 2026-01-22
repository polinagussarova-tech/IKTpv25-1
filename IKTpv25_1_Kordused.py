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



from math import * # import oli valesti tehtud
import math # import oli valesti tehtud
print("Ruudu karakteristikud")
a=float(input('Sisesta ruudu külje pikkus => ')) # int käsk ei olnud
S=a**2
print("Ruudu pindala", round(S, 1))
P=4*a
print("Ruudu ümbermõõt", round(P, 1))
di=a*math.sqrt(2) # on vaja lisada sqrt ei sqr
print("Ruudu diagonaal", round(di,2))
print()
print("Ristküliku karakteristikud") # ei ole vaja teine sulg
b=float(input("Sisesta ristküliku 1. külje pikkus => ")) # on vaja panna float või int
c=float(input("Sisesta ristküliku 2. külje pikkus => ")) # on vaja panna float
S=b*c
print("Ristküliku pindala", round(S, 1)) # kaks ülemist koma ei ole kirjutatud
P=2*(b+c) # on vaja korrutada panna
print("Ristküliku ümbermõõt", round(P, 1))
di=math.sqrt(b**2+c**2) #ei pea korrutama
print("Ristküliku diagonaal", round(di, 2)) # pärast di peab panema koma ja kaks ja teine sulg
print()
print("Ringi karakteristikud")
r=int(input("Sisesta ringi raadiusi pikkus => "))
d=2*r #on vaja panna korrutada
print("Ringi läbimõõt", round(d, 1))  # koma on puudu ja round puudu
S=pi*r**2 # sulg ei ole vaja kirjutada ja korrutada
print("Ringi pindala", round(S, 1)) # S koma 1
C=2*pi*r # kutsuta sulgud ja korrutada
print("Ringjoone pikkus", round(C, 2)) # kaks sulgud ja kaks pärast C ja koma








  päev=input("Sisesta päeva nimetus: (näiteks esmaspäev): ")
#1. Kui on neljapäev, siis "Huraaa, Programmeerimine!
if päev.lower()=="neljapäev":
    print("Huraaa, Programmeerimine!")

#2. Kui on neljapäev, siis "Huraaa, Programmeerimine!, kui on reede, siis "Igatsen programmeerida tahaks!"
if päev.lower()=="neljapäev":
    print("Huraaa, Programmeerimine!")
else:
    print("Igatsen, programmerida tahaks!")
#3. Tööpäevad ja nädalavahetus
if päev.lower()=="laupäev" or päev.lower()=="pühapäev":
    print("lõpuks ometi nädalavahetus!")
else:
    print("tööpäev, pean tööl käima!")


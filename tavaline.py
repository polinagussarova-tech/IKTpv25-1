
from Moodulifail import *

#5
summa=float(input("Sisesta hoiuse summa: "))
aastad=int(input("Sisesta aastate arv: "))
lõpp_summa=bank(summa, aastad)
print(f"Lõppsumma {aastad} aasta pärast on {lõpp_summa:.2f} eurot")

#4
kuu=season(input("Sisesta kuu number (1-12): "))
print(f"Aastaaja on: {kuu}")


#3
print("Arvutame ruudu pindala ja ümbermõõtu!")
külg=float_kontroll(input("Sisesta ruudu külje pikkus: "))
ümbermõõt,pindala,diagonaal=square(külg)
print(f"Ruudu külg: {külg}")
print(f"Ruudu ümbermõõt: {ümbermõõt}")
print(f"Ruudu pindala: {pindala}")
print(f"Ruudu diagonaal: {diagonaal}")



#2
for i in range(3):
    aasta=int_kontroll(input("Sisesta aasta: "))
    if is_year_leap(aasta):
        print(f"{aasta} on liigaasta")
    else:
        print(f"{aasta} on tavaline aasta")



  #1
print("Lahendame/testimine mitu arvutehet!")
for i in range(5):

    arv1=float_kontroll(input("Sisesta esimene arv: "))
    arv2=float_kontroll(input("Sisesta teine arv: "))

    t=input("Sisesta tehe (+,-,*,/): ")
    tulemus=arithmetic(arv1,arv2,t)
    print(f"{arv1}{t}{arv2} = {tulemus}")


#6
n = int(input("Sisesta arv (0–1000): "))

if is_prime(n):
    print(f"{n} on algarv!")
else:
    print(f"{n} ei ole algarv.")

#7
paev = int(input("Sisesta päev: "))
kuu = int(input("Sisesta kuu: "))
aasta = int(input("Sisesta aasta: "))

if date(paev, kuu, aasta):
    print("Kuupäev on õige!")
else:
    print("Kuupäev ei ole õige!")

#8
text = input("Sisesta tekst: ")
key = int(input("Sisesta võti (arv): "))

encrypted = XOR_cipher(text, key)
print(f"Krüpteeritud tekst {encrypted}")

decrypted = XOR_uncipher(encrypted, key)
print(f"Dekrüpteeritud tekst {decrypted}")

#9
text = input("Sisesta arvud komadega (näiteks 1,2,3,4): ")

if text.strip() == "":
    numbers = []
else:
    numbers = [float(x) for x in text.split(",")]

result = average(numbers)

if result is None:
    print("Järjend on tühi, keskmist ei ole.")
else:
    print(f"Aritmeetiline keskmine on {result}")

#10

text = input("Sisesta arvud komadega (näiteks 1,2,3,4): ")

if text.strip() == "":
    numbers = []
else:
    numbers = [float(x) for x in text.split(",")]

result = min_max(numbers)

if result is None:
    print("Järjend on tühi, tulemusi ei ole.")
else:
    print("Väikseim arv:", result[0])
    print("Suurim arv:", result[1])

#11

text = input("Sisesta elemendid komadega (näiteks: a,b,a,c,b): ")

if text.strip() == "":
    lst = []
else:
    lst = [x.strip() for x in text.split(",")]

result = unique_elements(lst)

print(f"Ainulaadsed elemendid {result}")



#TÖÖ 7.3


from kusimutlik__module import *
import random

N=3
M=2

koik=[]
oiged=[]
valed=[]

juba_testitud=["Mari", "Paul", "Johan"]

kus_vas={}

while True:
    valik=input("Vali 1- Alusta küsimustlikku, 2- lisa uus küsimus, 3- välju: ")
    
    #2 Küsimustiku läbiviimine ja Vastajate hulk
    if valik=="1":
        kus_vas=andmete_lugemine_failidest(kus_vas)
        for i in range(M):
            while True:
                nimi=input("Sisesta oma nimi: ")
                
                if nimi in juba_testitud:
                    print("See kasutaja on juba testitud! Sisesta teist nime.")
                else:
                    print(f"Tere, {nimi}! Alustame test.")
                    juba_testitud.append(nimi)
                    break
    #3 testimine
            punktid, sobis=testimine(kus_vas, N, nimi)
            email=nimi.replace(" ", ".")+"@example.com"
                    
            vastaja={"nimi":nimi, "punktid":punktid, "email":email, "sobis":sobis}
            koik.append(vastaja)
            
            if sobis:
                oiged.append(vastaja)
            else:
                valed.append(vastaja)
            
    #4 Failide salvestamine
            andmete_salvestamine_failidesse(koik, oiged, valed)
            print("Failid õiged.txt, valed.txt ja kõik.txt on salvestatud.")
        
    #5 E-kirjade saatmine
            emaili_saatmine(nimi, punktid, sobis)
            print("Emaili tulemused on saadetud.")
            
            raport_tooandjale(koik)
            
        
    #6 Võimalus lisada küsimusi programmi kaudu
    elif valik=="2":
            kusimus=input("Sisesta uus küsimus: ")
            vastus=input("Sisesta õige vastus: ")
        
            küsimuste_lisamine(kusimus, vastus)
            print("Uus küsimus on lisatud faili.")
            
    #7 Ekraaniväljund töö lõpus
            print("Edukalt vastanud:")
            for vastaja in oiged:
                print(vastaja["nimi"], "-", vastaja["punktid"], "õigesti")
        
            print("Tulemused saadetud e-posti aadressidele.")
            
    #8 välju kui valik on 3
    elif valik=="3":
            print("Head aega!")
            break
    else:
        print("Sisesta ainult 1, 2 või 3!")


#1.
#Kirjuta enda esimene programm, mis väljastab käsureale teksti: “Tere, maailm!”. 
#Küsi kasutaja nimi ja muuda tekst, et ta näeks välja nii: “Tere, maailm! Tervitan sind Mati”, kui kasutaja nimi on Mati.
#Küsi kasutajalt sisend tema vanuse kohta ning väljasta see ekraanile:
#“Tere, maailm! Tervitan sind Mati! Sa oled N aastat vana.”

print("Tere maailm!")
nimi=input("Sisesta oma nimi: ")
print(f"Tere maailm! Tervitan sind {nimi}") 
vanus=int(input("Sisesta oma vanus: "))
print(f"Tere maailm! Tervitan sind {nimi}. Sa olev {vanus} aastat vana")

#2
#Mis tüüpi on järgnevad muutujad:
# a) vanus = 18
# b) eesnimi = "Jaak"
# c) pikkus = 1.65
# d) kas_käib_koolis = True
# Mis võimalus veel peale True oleks viimast muutujat väärtustada? Kuidas võiks nende muutujate väärtusi koodis kontrollida?
# kood tüüpide kontrollimiseks.

vanus = 18 #int
eesnimi = "Jaak" #str
pikkus = 1.65 #float
kas_käib_koolis = True #bool

print(f"vanus {vanus} on: {type(vanus)}")
print(f"eesnimi {eesnimi} on: {type(eesnimi)}")
print(f"pikkus {pikkus} on: {type(pikkus)}")
print(f"kas_käib_koolis {kas_käib_koolis} on: {type(kas_käib_koolis)}")

#3
#Kirjuta enda koodis laual olevate kommide arv muutujasse(kommide arv on juhuslik). Seejärel kuva muutujas olev kommide arv ekraanile kasutades print() käsku.
#Küsi kasutajalt sisendit, mitu kommi ta soovib laualt ära võtta. Eemalda soovitud kommide arv laual olevate kommide arvust ja kuva ekraanile, kui palju komme laual nüüd on. 
from enum import member
from random import *
from types import MemberDescriptorType
laua_peal=randint(10,50)#juhuslik arv 10-50
print(f"laual on {laua_peal} kommi")
võtab=int(input("mitu kommi soovid võtta? "))#sisend võtab teisendab stringi täisarvuks
laua_peal-=võtab #laua_peal=laua_peal-võtab, võtab kommid maha
print(f"laual on nüüd {laua_peal} kommi")

# 4
# Puu läbimõõdu arvutamine
# Kirjuta programm, mis küsib kasutaja käest puu ümbermõõdu ning teatab selle peale puu läbimõõdu.
from math import*
ümbermõõt=int(input("sisesta puu ümbermõõt meetrites: ")) #int teisendab stringi täisarvuks

läbimõõt=ümbermõõt/3.14 #läbimõõt=ümbermõõt/π
print(f"puu läbimõõt on {läbimõõt:.2f} meetrit") #:.2f tähendab 2 kohta pärast koma

läbimõõt=ümbermõõt/pi #voib kasutada ka math raamatukogu
print(f"puu läbimõõt on {läbimõõt:.2f} meetrit") #.2f tähendab 2 kohta pärast koma

# 5.
# Arvutage Pythoni käsureal, kui pikk on ristkülikukujulise maatüki diagonaal, mille mõõtmed on Nm x Mm. N ja M küsi kasutajalt.
# from math import*
# N=int(input("sisesta maatüki N külje pikkus meetrites: "))
# M=int(input("sisesta maatüki M külje pikkus meetrites: "))
# diagonaal=sqrt(N**2+M**2) #Pythagorase teoreem
#     t(f"maatüki diagonaal on {diagonaal:.2f} meetrit")
# diagonaal=sqrt(N**2+M**2) #Pythagorase teoreem
#     t(f"maatüki diagonaal on {diagonaal:.2f} meetrit")
aeg = float(input("Mitu tundi kulus sõiduks? "))
teepikkus = float(input("Mitu kilomeetrit sõitsid? "))
kiirus = teepikkus / aeg

print("Sinu kiirus oli " + str(kiirus) + " km/h")
#6 Kood vastavalt esitatud plokkidele (ilma puhtuse ja vigade kontrollita)
print("Sisesta palun viis täisarvu:")
a1 = int(input("Arv 1: "))
a2 = int(input("Arv 2: "))
a3 = int(input("Arv 3: "))
a4 = int(input("Arv 4: "))
a5 = int(input("Arv 5: "))

s = a1 + a2 + a3 + a4 + a5
avg = s / 5

print(f"\nViie sisestatud arvu summa on: {s}")
print(f"Viie sisestatud arvu aritmeetiline keskmine on: {avg}")

#7 Võimalik viga: kui jagamisarv on 0, tekib ZeroDivisionError
d = int(input("\nSisesta üks täisarv, millega soovid summat jagada: "))

tosa = s // d
jaak = s % d

print(f"Summa ({s}) jagatuna arvuga ({d}):")
print(f"  Täisarvuline osa (kvoot): {tosa}")
print(f"  Jääk: {jaak}")

print("  @..@")
print("  (----)")
print(" ( \__/ )")
print("^^ \"\" ^^")

#8 Kolmnurk, korduv plokk
x = 5
y = 7
z = 9
P = x + y + z
print(f"Kolmnurga küljed on a={x}, b={y}, c={z}.")
print(f"Kolmnurga ümbermõõt P = a + b + c on: {P}")

#9 Pitsa
h = 12.90
jp = 0.10

try:
    p = int(input("Mitu inimest (P) pitsa eest maksab? "))
except ValueError:
    exit() # Jätab veateate väljastamata

if p <= 0:
    exit() # Jätab teate väljastamata

j = h * jp
k = h + j
m = k / p

print(f"\n--- Arvutuse tulemused ---")
print(f"Pitsa hind: {h:.2f} €")
print(f"Jootraha (10%): {j:.2f} €")
print(f"Kogu maksumus (koos jootrahaga): {k:.2f} €")
print(f"Inimesi (P): {p}")
print(f"Igaüks peab maksma: {m:.2f} €")



#veel töö
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

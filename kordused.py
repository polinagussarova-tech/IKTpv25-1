
#Variant 4

#1️ Kirjuta programm, mis antud arvu n (1–9) põhjal kuvab ekraanile n loomakest.
#Kahe loomakese vahel on tühikurida (tühikute veerg).
#Lubatud on tühik pärast viimast loomakest.
 # ^---^
# ( o o )
#  ! = !/)

while True:
    try:
        n=int(input("Sisesta arv (1-9): "))
        if 1<=n<=9:
            loom1="  ^---^"
            loom2=" ( o o )"
            loom3=" ! = !/)"
            
            print((loom1+" ")*n)
            print((loom2+" ")*n)
            print((loom3+" ")*n)
            break
        else:
            print("Arv peab olema 1 kuni 9!")
    except ValueError:
        print("Sisesta ainult täisarv!")

#2️ Väljasta naturaalarvude astmed, mis ei ületa arvu n×100.
#Kasutaja määrab astme näitaja ja arvu n.


while True:
    try:
        n=int(input("Sisesta arv n: "))
        if n>0:
            break
        else:
            print("Palun sisesta positiivne arv.")
    except ValueError:
        print("Palun sisesta korrektne täisarv.")
while True:
    try:
        k=int(input("Sisesta astme näitaja k: "))
        if k>0:
            break
        else:
            print("Palun sisesta positiivne astme näitaja.")
    except ValueError:
        print("Palun sisesta korrektne täisarv.")

limit=n*100
arv=1
while arv ** k <= limit:
    print(arv**k)
    arv+= 1

#3️ Antud on klassi õpilaste füüsika hinded.
#Leia minimaalne ja maksimaalne hinne (hinded ja õpilaste arv genereeritakse juhuslikult).

import random

opilaste_arv = random.randint(1,28)
print(f"Õpilaste arv on: {opilaste_arv}")
min_hinne = 5
max_hinne = 1

for i in range(opilaste_arv):
    hinne = random.randint(1, 5)
    print(f"Õpilane {i+1} hinne: {hinne}")
    if hinne < min_hinne:
        min_hinne = hinne
    if hinne > max_hinne:
        max_hinne = hinne

print(f"Miinimaalne hinne: {min_hinne}")
print(f"Maksimaalne hinne: {max_hinne}")

#4️ Üherakuline amööb jaguneb iga 3 tunni järel kaheks rakuks.
#Määra, mitu rakku on 3, 6, 9, ..., 24 tunni pärast, kui alguses oli üks rakk.

rakk=1

for tund in range(3, 25, 3):
    rakk=rakk*2
    print(f"tunni parast on {tund} rakku {rakk}")

#5️ Käsna-Kalle praeb kotlette 
#Tal on K kotletti ja ühele pannile mahub M kotletti.
#Arvuta, mitu täis pannitäit tuleb praadida ja mitu kotletti jääb viimasele pannile.
#Kasuta ainult tsüklit ja lahutamist.

while True:
    try:
        K=int(input("Sisesta kotlettide arv K: "))
        break
    except ValueError:
        print("Palun sisesta täisarv!")
while True:
    try:
        M=int(input("Sisesta pannile mahtuv kotlettide arv M: "))
        if M<=0:
            print("Pannile mahtuv kotlettide arv peab olema positiivne!")
        else:
            break
    except ValueError:
        print("Palun sisesta täisarv!")

pannid=0
while K>=M:
    K=K-M
    pannid=pannid+1
if K==0:
    print("Viimasele pannile ei jää midagi.")
else:
    print(f"Viimasele pannile jääb {K} kotletti")


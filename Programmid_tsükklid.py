#töö 3.1

#1 Sisestatakse 15 arvu.
#Määrata, mitu neist on täisarvud.

#k=0 #looendur
#for i in range(15):
  #  arv=float(input(f"Sisesta {i+1}. arv: "))
  #  if int(arv)==arv:
   #     print(f"{arv} on taisarv")
   #     k+=1
#print(f"Taisarve oli kokku {k} tk")

#2 Küsi kasutajalt arv A ja leia kõigi naturaalarvude summa vahemikus 1 kuni A.
#s=0 #summa
#while True:
  #  try:
  #      A=int(input(f"Sisesta A: "))
  #      break
  #  except:
  #      print("Vale andmetuup!")
#for i in range(1, A+1):
 #   s=s+i
#print(f"Summa vahwmikus 1 kuni {A} vordub {s}")


#3 Sisestatakse 8 arvu.
#Leida nende korrutis (ainult positiivsete arvude puhul).

#korrutis=1
#positiivsete=False
#for i in range(8):
   # arv=float(input(f"Sisesta {i+1}. arv: "))
   # if arv>0:
   #     korrutis*=arv
   #     positiivsete=True
#if positiivsete:
 #   print(f"Positiivsete arvude korrutis on {korrutis}")
#else:
 #   print("Korrutist ei saa, sest et ei olnud positiivsete arvude.")

#4  Koosta programm, mis väljastab ekraanile arvude ruudud vahemikus 10 kuni 20.

#for i in range(10,21):
    #print(f"Arv {i} ruut on {i**2}")

#5 Koosta programm, mis arvutab ainult negatiivsete arvude summa N sisestatud arvu seast.
#N väärtus sisestatakse klaviatuurilt.

#N = int(input("Kui palju arvu sa tahad sisestada? "))
#summa = 0
#for i in range(1, N + 1):
#    arv = float(input(f"Sisesta arv {i}: "))
#    if arv < 0:
#        summa += arv
#print(f"Negatiivsete arvude summa on: {summa}")

#6 Klaviatuurilt sisestatakse N arvu.
#Koosta programm, mis määrab sisestatud arvude seast:
#negatiivsete arvude arvu,
#positiivsete arvude arvu,
#nullide arvu.
#(N väärtus sisestatakse klaviatuurilt.)

#negatiivsed=0
#positiivsed=0
#nullid=0
#N=int(input("Kui palju arvu tahad sisestada? "))

#for i in range(1,N+1):
 #   arv=float(input(f"Sisesta arv {i}: "))
 #   if arv<0:
 #       negatiivsed+=1
 #   elif arv>0:
 #       positiivsed+=1
 #   else:
  #      nullid+=1
#print(f"Negatiivseid arve {negatiivsed}: ")
#print(f"Positiivseid arve {positiivsed}: ")
#print(f"Nulle {nullid}: ")

#7 Väljastada ekraanile arvud, mis on K-ga jaguvad vahemikust [A, B].

#A = int(input("Sisesta algus (A): "))
#B = int(input("Sisesta lopp (B): "))
#K = int(input("Sisesta jagaja (K): "))

#print(f"Kontrollime {A} kuni {B} jaguvad arvuga {K}: ")

#for arv in range(A, B + 1):
#    if arv % K == 0:
#        print(f"{arv} jagub arvuga {K}")
#    else:
#        print(f"{arv} ei jagu arvuga {K}")
#print(f"arvud vahemikus {A},{B} mis jaguvad arvuga {K}:")


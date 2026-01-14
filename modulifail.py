
#1️ Sõna või lause analüüs
#Sisesta sõna või lause.
#Loenda:
#mitu täishäälikut 
#mitu kaashäälikut 
#kui sisestati lause – loenda ka tühikud ja kirjavahemärgid
#import string

#t=[ 'a', 'e', 'i', 'o', 'u', 'ü', 'ä', 'ö', 'õ']
#k=['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 'š', 'z', 'ž', 't', 'v', 'w', 'x', 'y']
#m=string.punctuation + string.whitespace
#sõna_lause=input("Sisesta sõna või lause: ").lower()
#täishäälikud=0
#kaashäälikud=0
#märgid=0
#for täht in sõna_lause:
#    if täht in t:
 #       täishäälikud+=1
#    elif täht in k:
#        kaashäälikud+=1
#    elif täht in m:
#        märgid+=1
#print(f"Sõnas/lausees on {täishäälikud}täishäälikut, {kaashäälikud} kaashäälikut ja {märgid} märki.")


#2️ Loendid
#2.1 Nimed 👥
#Küsi kasutajalt viis nime.
#Salvesta nimed loendisse ja kuva need tähestikulises järjekorras.
#Kuva viimane lisatud nimi.
#Lisa võimalus nimekirjas olevaid nimesid muuta ✍️
#nimed=[]

#for i in range(5):
  #  küsimus=input("Sisesta palun 5 nime: ")
  #  nimed.append(küsimus)

#print(nimed)
#viimane_nimi=nimed[-1]
#nimed.sort()
#print(nimed)
#print(viimane_nimi)

#muuda=input("Kas sa tahad muuta nimi? ")
#if muuda=="jah":
 #   vana_nimi=input("Mis nimi muutame?")
  #  uus_nimi=input("Mis uus nimi?")
  #  find=nimed.index(vana_nimi)
 #   nimed[find]=uus_nimi
  #  print(nimed)
#else:
    #print(nimed)



#2.2 Kordustega nimed
#Antud on loend kordustega.
#Koosta programm, mis väljastab nimed ilma kordusteta.
#nimed=["Mari", "Jüri", "Kati", "Mari", "Peeter", "Jüri", "Anna"]
#ilma_kordusteta=list(set(nimed))
#print(ilma_kordusteta)

#2.3 Vanused
#Koosta vanuste loend ja leia:
#suurim
#väikseim
#kogusumma
#keskmine

#vanused=[12, 45, 23, 67, 34, 89, 10]
#suurim=max(vanused)
#väikseim=min(vanused)
#kogusumma=sum(vanused)
#keskmine=kogusumma/len(vanused)
#print(f"Suurim vanus on {suurim}")
#print(f"väikseim vanus on {väikseim}")
#print(f"kogusumma on {kogusumma}, keskmine on {keskmine:.2f}")

#3️ Tärnide lintdiagramm ⭐
#Kasuta loendis olevaid arve ja joonista tärnidega diagramm.
#******************
#*******************
#********************************
#*****************************************
#****************************************************
#************

#arvud=[18, 19, 32, 41, 52, 12]
#for arv in arvud:
#    print("*" * arv)

#4 Postiindeks
#Eestis koosnevad postiindeksid 5 numbrist, millest esimene number tähistab maakonda:
#1 – Tallinn 
#2 – Narva, Narva-Jõesuu 
#3 – Kohtla-Järve 
#4 – Ida-Virumaa, Lääne-Virumaa, Jõgevamaa 
#5 – Tartu linn 
#6 – Tartumaa, Põlvamaa, Võrumaa, Valgamaa 
#7 – Viljandimaa, Järvamaa, Harjumaa, Raplamaa 
#8 – Pärnumaa 
#9 – Läänemaa, Hiiumaa, Saaremaa
#Kontrolli kasutaja sisestatud postiindeksit.
#Näita, millisesse maakonda see kuulub.
#Erireegel:
#Tallinn, Narva, Kohtla-Järve → „Mine merre!”
#Teised → „Mine metsa!”

#index={"Tallinn", "Narva, Narva-Jõesuu", "Kohtla-Järve", "Ida-Virumaa, Lääne-Virumaa, Jõgevamaa", "Tartu", "Tartumaa, Põlvamaa, Võrumaa, Valgamaa", "Viljandimaa, Järvamaa, Harjumaa, Raplamaa", "Pärnumaa", "Läänemaa, Hiiumaa, Saaremaa"}
#while True:
  #  try:
  #      index=int(input("Sisesta oma postiindeks (5-kohaline arv):"))
  #      if 10000<=index<=99999:
   #         break
   #     else:
   #         print("Postiindeks peab olema 5-kohaline arv")
  #  except:
  #      print("Vigane andmetüüp")
#index_list=list(str(index))
#n1=int(index_list[0])
#print(f"Sinu postiindeks {index} kuulub piirkonda: {index_list[n1-1]}")
#if n1 in [0,1, 2, 7]:
  #  print("Mine merre!")
#else:
  #  print("Mine metsa!")


#5️ Vahetus 
#Vaheta loendis esimene ja viimane element, teine ja eelviimane jne.
#Küsi kasutajalt, mitu paari vahetada. loendis on min 2 elem.

#from random import *
#loend_arvud=[]
#loend_tähed=[]
#k=['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 'š', 'z', 'ž', 't', 'v', 'w', 'x', 'y']
#loend_kaashäälikud=[]
#mitu=randint(2,20)
#for i in range(mitu):
 #   elem=randint(0,100)
 #   loend_arvud.append(elem)
 #   elem=chr(randint(65,90))
 #   loend_tähed.append(elem)
 #   elem=choice(k)
 #   loend_kaashäälikud.append(elem)
#print(f"Kokku on {mitu} elemente loendis")
#while True:
   # try:
    #    paaride_arv=int(input(f"Sisesta mitu paari soovid vahetada? "))
   #     if 1<paaride_arv<=mitu//2:
    #        break
   #     else:
   #         print(f"arv peab olema vahemikus 1 kuni {mitu//2}")
  #  except:
   #     print("Vigane andmetüüp, proovi uuesti")

#6️„Arvud“
#Leia loendi suurim arv, jaga see loendi pikkusega ja asenda see tulemusena.


#from random import *
#loend_arvud=[]
#mitu=randint(2,20)
#for i in range(mitu):
#    elem=randint(0,100)
#    loend_arvud.append(elem)
#print(f"alguses loend: {loend_arvud}")
#suurim=max(loend_arvud)
#kus_asub=loend_arvud.index(suurim)
#suurim_muudatud=suurim/mitu
#loend_arvud[kus_asub]=round(suurim_muudatud,2)
#print(f"Muutumise järel: {loend_arvud}")


#7️ Sorteerimine 📊
#Sorteeri nimekiri numbreid absoluutväärtuse järgi
#kasvavalt ⬆️
#või kahanevalt ⬇️

#arvud = [-10, 3, -2, 15, -20, 5]
#print(f"Algne loend {arvud}")
#arvud.sort(key=abs)
#print(f"Kasvavalt (abs)  {arvud}")

#8️⃣ Võrdse pikkusega sõned 🧱
#Muuda kõik sõned loendis sama pikkusega, täites lühemad alakriipsudega _.
#Järjekorda ei tohi muuta.
#On antud:
#['tamm', 'taevas', 'elevant'] 
#['a', 'aa', 'aaa', 'aaaa', 'aaaaa'] 
#['qweasdqweas', 'q', 'rteww', 'ewqqqqq']
#Tulemus:
#['tamm___', 'taevas_', 'elevant'] 
#['a____', 'aa___', 'aaa__', 'aaaa_', 'aaaaa'] 
#['qweasdqweas', 'q__________', 'rteww______', 'ewqqqqq____']

#def võrdsusta_sõned(loend):
   # max_pikkus = max(len(s) for s in loend)
   # return [s + "_" * (max_pikkus - len(s)) for s in loend]
#
#loend1 = ['tamm', 'taevas', 'elevant']
#loend2 = ['a', 'aa', 'aaa', 'aaaa', 'aaaaa']
#loend3 = ['qweasdqweas', 'q', 'rteww', 'ewqqqqq']

#print(võrdsusta_sõned(loend1))
#print(võrdsusta_sõned(loend2))
#print(võrdsusta_sõned(loend3))

#9️⃣ Nime kontroll 👤
#Programm peab :
#kontrollima, et nimi sisaldab ainult tähti ✔️
#kuvama nimega tervituse (suur algustäht) 😊
#loendama tähti, täishäälikuid ja kaashäälikuid
#kuvama nime tähed tähestiku järjekorras (ilma kordusteta) 🔤

#nimi = input("Sisesta nimi: ")

#if not nimi.isalpha():
 #   print("Nimi peab sisaldama ainult tähti!")
#else:
 #   nimi_korras = nimi.capitalize()
 #   print(f"Tere, {nimi_korras}!")

 #   täishäälikud = "aeiouõäöüAEIOUÕÄÖÜ"
 #   kaashäälikud = "bcdfghjklmnpqrsšzžtvwxyBCDFGHJKLMNPQRSŠZŽTVWXY"

 #   tähti = len(nimi)
 #   vokaalid = sum(1 for t in nimi if t in täishäälikud)
 #   konsonandid = sum(1 for t in nimi if t in kaashäälikud)

 #   print(f"Tähti kokku: {tähti}")
    #print(f"Täishäälikuid: {vokaalid}")
  #  print(f"Kaashäälikuid: {konsonandid}")

  #  unikaalsed = sorted(set(nimi.lower()))
 #   print("Tähed tähestiku järjekorras:", "".join(unikaalsed))




#🔟 Töötajate andmed 💼
#Leia antud andmete põhjal:
#suurima palgaga töötaja
#keskmine palk
#mitu teenib üle keskmise
#keskmine vanus gruppidel: ≤ keskmine ja > keskmine

#tootajad = ["Mari", 25, 1500, "Jüri", 40, 2100, "Kati", 29, 1800, "Peeter", 50, 2500, "Anna", 35, 1900]

#suurim_palk = 0
#suurim_nimi = ""

#for i in range(0, len(tootajad), 3):
 #   nimi = tootajad[i]
 #   palk = tootajad[i+2]
 #   if palk > suurim_palk:
  #      suurim_palk = palk
  #      suurim_nimi = nimi

#print(f"Suurim palk: {suurim_nimi}, {suurim_palk}")

#palgad = []
#for i in range(2, len(tootajad), 3):
   # palgad.append(tootajad[i])

#keskmine = sum(palgad) / len(palgad)
#print(f"Keskmine palk: {round(keskmine, 2)}")

#ule = 0
#for palk in palgad:
 #   if palk > keskmine:
 #       ule += 1

#print(f"Üle keskmise palga: {ule}")

#vanus_väike = []
#vanus_suur = []

#for i in range(0, len(tootajad), 3):
 #   vanus = tootajad[i+1]
  #  palk = tootajad[i+2]
  #  if palk <= keskmine:
  #      vanus_väike.append(vanus)
 #   else:
  #      vanus_suur.append(vanus)

#print(f"Vanuse keskmine (palk ≤ keskmine): {round(sum(vanus_väike)/len(vanus_väike), 1)}")
#print(f"Vanuse keskmine (palk > keskmine): {round(sum(vanus_suur)/len(vanus_suur), 1)}")



#1️⃣1️⃣ Inglise tähestik 🔡
#Koosta:
#loend tähtedest ‘a’, ‘b’, ‘c’ ...
#loend: ‘a’, ‘bb’, ‘ccc’, ‘dddd’ ...

#tahed = []
#for t in "abcdefghijklmnopqrstuvwxyz":
#    tahed.append(t)
#print(tahed)

#tahed2 = []
#k = 1
#for t in "abcdefghijklmnopqrstuvwxyz":
 #   tahed2.append(t * k)
 #   k += 1
#print(tahed2)



#1️⃣2️⃣ Min ja max vahetamine 🔄
#Genereeri 10 juhuslikku arvu ja vaheta loendis väikseim ja suurim omavahel.


#import random

#numbrid = []
#for i in range(10):
#    numbrid.append(random.randint(1, 100))

#print(f"Algne {numbrid}")

#min_val = min(numbrid)
#max_val = max(numbrid)

#i_min = numbrid.index(min_val)
#i_max = numbrid.index(max_val)

#numbrid[i_min], numbrid[i_max] = numbrid[i_max], numbrid[i_min]

#print(f"Tulemus {numbrid}")



#1️⃣3️⃣ Arva sõna ära 🎯
#Programm:
#valib juhusliku sõna
#näitab seda alakriipsudena
#küsib tähti
#täidab õiged kohad
#lisab valed tähed eraldi loendisse
#näitab katsete arvu, kui sõna on ära arvatud


#import random

#sõnad = ["auto", "kala", "maja", "puu", "arvuti"]
#sõna = random.choice(sõnad)

#varjatud = list("_" * len(sõna))
#valed = []
#katsed = 0

#print(f"Arva sõna {varjatud}")

#while "_" in varjatud:
  #  t = input("Täht: ").lower()
 #   katsed += 1

 #   if t in sõna:
 ##       for i in range(len(sõna)):
  #          if sõna[i] == t:
  #              varjatud[i] = t
  #  else:
   #     valed.append(t)
   #     print(f"Valed {valed}")

#print(f"Arvasid ära! Katsed {katsed}")




#1️⃣4️⃣ Euroopa pealinnad 🌍
#Loo vähemalt 10 pealinnaga loend.
#Programm peab:
#kuvama iga linna eraldi
#sortima tähestikuliselt
#lisama kasutaja sisestatud 2 uut pealinna
#sortima uuesti
#lisama järjekorranumbrid
#kuvama kokkuvõtte: „Meie loendis on X Euroopa pealinna.”
#kuva neid veeruna

#pealinnad = ["Tallinn", "Riga", "Vilnius", "Helsinki", "Stockholm", "Oslo", "Copenhagen", "Berlin", "Warsaw", "Paris"]

#for linn in pealinnad:
#    print(linn)
#pealinnad.sort()

#uus_pealinn = input("Lisa pealinn: ")
#uus_pealinn2 = input("Lisa veel üks: ")

#pealinnad.append(uus_pealinn)
#pealinnad.append(uus_pealinn2)

#pealinnad.sort()

#for i in range(len(pealinnad)):
 #   print(i + 1, pealinnad[i])
#print("Meie loendis on", len(pealinnad), "Euroopa pealinna.")



#1️⃣5️⃣ Lihtne sõnaraamat 📚
#Koosta 4 loendit (arv, eesti, inglise, itaalia).
#Kuva tabelina:
#1 – üks – one – uno
#Lisaks:
#lisa kaks uut elementi
#kontrolli, kas sõna „tre” on olemas
#kuva kõik loendid tähestikulises järjekorras

#import random

#arv = [1, 2, 3, 4]
#eesti = ["üks", "kaks", "kolm", "neli"]
#inglise = ["one", "two", "three", "four"]
#itaalia = ["uno", "due", "tre", "quattro"]

#for i in range(len(arv)):
 #   print(arv[i], "-", eesti[i], "-", inglise[i], "-", itaalia[i])

#arv.append(5)
#eesti.append("viis")
#inglise.append("five")
#itaalia.append("cinque")

#arv.append(6)
#eesti.append("kuus")
#inglise.append("six")
#itaalia.append("sei")

#if "tre" in itaalia:
 #   print("Sõna 'tre' on olemas!")
#else:
 #   print("Sõna 'tre' puudub.")

#print(f"Eesti: {sorted(eesti)}")
#print(f"Inglise: {sorted(inglise)}")
#print(f"Itaalia: {sorted(itaalia)}")

#vastused = ["Jah, kindlasti!", "Jah!", "Võib-olla!", "Ei!"]

#küsimus = input("Küsi midagi: ")
#print(random.choice(vastused))


#1-esmaspäev, 2-teisipäev, 3-kolmapäev, 4-neljapäev, 5-reede, 6-laupäev, 7-pühapäev
#paev_number=int(input("Sisesta paeva number (1-7): "))
#if paev_number==1:
    #print("Esmaspaev")
#elif paev_number==2:
    #print("Teisipaev")
#elif paev_number==3:
    #print("Kolmapaev")
#elif paev_number==4:
    #print("Neljapaev")
#elif paev_number==5:
    #print("Reede")
#elif paev_number==6:
    #print("Laupaev")
#elif paev_number==7:
   # print("Puhapaev")
#else:
   # print("Vale number! Palun sisesta number vahemikus 1-7.")






#1. Juku

#a Kui eesnimi on Juku siis lähme Jukuga kinno. Aga teeme seda nii, kui nimi oli kirjutatud suurtähtedega.

#b Lisa valiku, kus Juku vanuse alusel otsustate mis pilet talle vaja osta. (Tee kontroll, kas sisestatud arv on täisarv)

#<6 aastad  - tasuta
#6-14 - lastepilet
#15-65 - täispilet
#>65 - sooduspilet
#<0 ja >100 viga andmetega
#eesnimi=input("Sisesta eesnimi: ")
#if eesnimi=="JUKU":
    #print("Lahme Jukuga kinno!")
    #vanus=input("Sisesta Juku vanus: ")
    #if vanus.isdigit():
        #vanus=int(vanus)
        #if vanus<9 or vanus>100:
            #print("Viga andmetega!")
        #elif vanus<6:
            #print("Pilet on tasuta!")
        #elif vanus<=14:
            #print("Lastepilet")
        #elif vanus<=65:
            #print("Taispilet")
        #else:
            #print("Sooduspilet")
    #else:
        #print("Palun sisesta vanus taisarvuna!")

#2 Pinginaabrid

#Küsi kahe inimese nimed. Kui nimed koosnevad
#ainult tähedest siis  teavita kasutajat,
#kas nad on täna pinginaabrid või ei mitte.
#nimi1=input("Sisesta nimi => ").capitalize()
#nimi2=input("Sisesta nimi => ").capitalize()
#if nimi1.isalpha() and nimi2.isalpha():
    #if nimi1=="Polina" and nimi2=="Darja" or nimi1=="Darja" and nimi2=="Polina":
        #print(f"{nimi1} ja {nimi2} on tana pinginaabrid")
    #else:
        #print(f"{nimi1} ja {nimi2} ei ole pinginaabrid")
#else:
    #print("Palun sisesta ainult tahed")

#3 Remont

#Küsi ristkülikukujulise toa seinte pikkused ning arvuta põranda pindala. Küsi kasutajalt remondi tegemise soov, kui ta on positiivne, siis küsi kui palju maksab ruutmeeter ja leia põranda vahetamise hind
#Lisaküsimus: kas ta teeb remonti ise või teeb seda professionaali abiga? Kui tegemist on professionaaliga, siis palun arvutage välja, kui palju remont koos tööga maksab.

#pikkus = int(input("Sisestage pikkus: "))
#laius = int(input("Sisestage laius: "))
#if pikkus>0 and laius>0:

    #pindala = pikkus * laius
    #print(f"pindala suurus on {pindala}")
    #user = input("Kas soovite remondi teha? ").capitalize()
    #if user.isalpha() and user == "Jah":
        #hind = float(input("Ruutmeetri hind? "))
        #if hind>0:
            #remondi_hind = hind * pindala
            #print(f"remondi summa on {remondi_hind}€")
            #kes = input("Kes teeb remondi(ise/tootaja)? ").capitalize()
            #if kes.isalpha() and kes == "Ise":
                #print(f"Siis summa on {remondi_hind}€")
            #else:
                #print(f"Siis summa on {remondi_hind + 300}€")
        #else:
            #print("Hind ei saa olla negatiivne!")
    #else:
        #print("Head aega!")
#else:
    #print("Arvud peavad olema suurem kui 0")

#4 Allahindus

 #Leia 30% soodustusega hinna, kui alghind on suurem kui 700


#hind = input("Hind: ")

#if hind.isdigit():
    #hind = float(hind)
    #if hind > 700:
       # hind *=0.7
        #print(f"Soodus hind võrdub {hind}")
#else:
    #print("On vaja numbreid sisestada")


#5 Temperatuur

#Küsi temperatuur ning teata, kas see on üle 18 kraadi (soovitav toasoojus talvel)
#try:
    #temperatuur=float(input("Sisesta temperatuur: "))
    #if temperatuur>18:
        #print("Soovitatav toasoojus talvel")
    #else:
        #print("Võib olla jähe")
#except:
    #print("Palun sisesta temperatuur ujukomaarvuna!")

#6 Pikkus

#Küsi inimese pikkus ning teata, kas ta on lühike, keskmine või pikk (piirid pane ise paika)

#pikkus=float(input("Sisesta oma pikkus: "))
#if pikkus<150:
    #print("Sa oled lühike")
#elif pikkus <=190:
    #print("Sul on keskmine pikk")
#else:
    #print("Sa oled pikk")

#7 Pikkus ja sugu

#Küsi inimeselt pikkus ja sugu ning teata, kas ta on lühike, keskmine või pikk (mitu tingimusplokki võib olla üksteise sees).

#pikkus=float(input("Sisesta oma pikkus: "))
#sugu=input("Sisesta oma sugu: ").lower()

#if sugu== "mees":
    #if pikkus<170:
        #print("Sa oled lühike mees")
    #elif pikkus <=185:
        #print("Sa oled keskmise pikkusega mees")
    #else:
        #print("Sa oled pikk mees")

#elif sugu== "naine":
    #if pikkus<150:
        #print("Sa oled lühike naine")
    #elif pikkus <=170:
        #print("Sa oled keskmise pikkusega naine")
    #else:
        #print("Sa oled pikk naine")

#else:
    #print("Palun sisesta oma sugu!")

#8 Poes

#Küsi inimeselt poes eraldi kas ta soovib osta piima, saia, leiba jne. Loo juhuslikud hinnad ja küsi mitu tükki tahad osta, kui tahad. Teata, mis summa maksma läheb(Kuva ekraanil tšekk).

#import random

#def küsi_toode(nimi):
   # """Küsib, kas inimene soovib toodet ja kui jah, siis mitu tükki."""
   # soov = input(f"Kas soovid osta {nimi}? (jah/ei): ").strip().lower()

    #if not soov.isalpha():
     #   print("Palun sisesta ainult tähed (jah/ei)!")
      #  return 0, 0

  #  if soov == "jah":
    #    hind = round(random.uniform(0.5, 5.0), 2)
    #    kogus = input(f"Mitu {nimi} soovid osta? (sisesta arv): ").strip()

   #     if not kogus.isdigit():
    #        print("Palun sisesta ainult arv!")
       #     return 0, 0

      #  kogus = int(kogus)
     #   return hind, kogus
  #  else:
     #   return 0, 0


#def prindi_tsekk(ostud):
  #  """Kuvab tšeki ja kogusumma."""
  #  print("\n--- tsekk ---")
    #kokku = 0
   # for nimi, (hind, kogus) in ostud.items():
    #    if kogus > 0:
        #    summa = hind * kogus
         #   kokku += summa
         #   print(f"{nimi:<10} {kogus} tk x {hind:.2f}€ = {summa:.2f}€")
   # print("----------------")
   # print(f"Kokku: {kokku:.2f}€")
  #  print("Aitäh ostu eest!")

#tooted = ["piim", "sai", "leib", "juust", "või", "munad", "õun", "kohv"]

#ostud = {}
#for toode in tooted:
 #   hind, kogus = küsi_toode(toode)
  #  ostud[toode] = (hind, kogus)
#9 Ruut

#Kasutaja sisestab ruudu küljed ning programm tuvastab kas tegemist saab olla ruuduga.
#Koosta vastab plokkskeem ja salvesta see samasse kataloogi programmiga.
#küljed = []

#print("Sisesta 4 külje pikkused (ainult numbrid):")
#for i in range(1, 5):
 #   külg = input(f"Sisesta {i}. külg: ").strip()
  #  if külg.replace('.', '', 1).isdigit():
   #     külg = float(külg)
   #     if külg > 0:
     #       küljed.append(külg)
    #    else:
     #       print("Külg peab olema positiivne arv!")
   # else:
      #  print("Palun sisesta arv, mitte tähed!")

#if len(küljed) == 4 and küljed.count(küljed[0]) == 4:
   # print("See on ruut — kõik küljed on võrdsed!")
#else:
  #  print("See EI OLE ruut — külgede pikkused erinevad.")

#10 Matemaatika
#Kasutaja sisestab kaks arvu ning programm küsib kasutajalt, mis tehet ta soovib (+-*/) ning viib kasutaja valiku ellu.
#Koosta vastab plokkskeem ja salvesta see samasse kataloogi programmiga.

#arv1 = input("Sisesta esimene arv: ").strip()
#arv2 = input("Sisesta teine arv: ").strip()

#if arv1.replace('.', '', 1).isdigit() and arv2.replace('.', '', 1).isdigit():
  #  arv1 = float(arv1)
  #  arv2 = float(arv2)
#else:
  #  print("Palun sisesta ainult arvud!")

#tehe = input("Sisesta tehe (+, -, *, /): ").strip()

#if tehe == '+':
 #   tulemus = arv1 + arv2
 #   print(f"Tulemus: {arv1} + {arv2} = {tulemus}")
#elif tehe == '-':
  #  tulemus = arv1 - arv2
  #  print(f"Tulemus: {arv1} - {arv2} = {tulemus}")
#elif tehe == '*':
  #  tulemus = arv1 * arv2
 #   print(f"Tulemus: {arv1} * {arv2} = {tulemus}")
#elif tehe == '/':
 #   if arv2 == 0:
  #      print("Nulliga sa ei saa jagada !")
  #  else:
  #      tulemus = arv1 / arv2
 #       print(f"Tulemus: {arv1} / {arv2} = {tulemus}")
#else:
  #  print("Kasuta ainult + - * /")

#11 Juubel
#Kasutaja sisestab oma sünnipäeva ja sinu programm ütleb, kas tegemist on juubeliga.
#Plokkskeemi pole vaja!

#synniaasta = int(input("Sisesta oma sünniaasta: "))
#vanus = date.today().year - synniaasta
#if vanus % 5 == 0:
  #  print(f"Sul on juubel! Oled {vanus} aastat vana.")
#else:
    #print(f"Sul ei ole juubelit. Oled {vanus} aastat vana.")

#12 Müük
#Kasutaja sisestab toote hinna. Kui see on hinnaga kuni 10€, saab ta allahindlust 10%. Üle 10€ tooted saavad soodukat 20%.
#Kuva toote lõplik hind. Plokkskeemi pole vaja!

#hind = input("Sisesta toote hind (€): ").strip()

#if hind.replace('.', '', 1).isdigit():
  #  hind = float(hind)
 #   if hind > 0:
 #       if hind <= 10:
    #        soodustus = hind * 0.10
   #     else:
     #       soodustus = hind * 0.20
     #   lopphind = hind - soodustus
 #       print(f"Toote lõplik hind on {lopphind:.2f} €")
    #else:
  #      print("Hind peab olema positiivne arv!")
#else:
  #  print("Palun sisesta hind numbrina!")

#13 Jalgpalli meeskond
#Sa pead looma programmi, mis kontrollib kas kandideerija sobib antud meeskonda.
#Vanus peab jääma vahemikku 16-18 ning lubatud on ainult meessugu.
#Täienda programmi nii, et kui kandideerija on naissoost, siis vanust üldse ei küsita

#sugu = input("Sisesta sugu (mees/naine): ").strip().lower()
#if sugu == "naine":
   # print("Vabandust, ainult mees lubatud.")
#elif sugu == "mees":
  #  vanus = int(input("Sisesta vanus: "))
  #  if 16 <= vanus <= 18:
 #       print("Sobid meeskonda!")
 #   else:
 #       print("Ei sobi vanus.")
#else:
  #  print("Kõik on korrass!.")

#14 Busside logistika
#Olgu meil vaja transportida teatud arv inimesi bussidega, milles on teatud arv kohti. Mitu bussi on vaja selleks, et kõik inimesed kohale saaksid, ja mitu inimest on viimases bussis (eeldusel, et eelmised on kõik täiesti täis)? Kirjuta programm, mis küsib inimeste arvu ja busside suuruse ning lahendab seejärel selle ülesande.

#inimesed = input("Sisesta inimeste arv: ").strip()
#kohad = input("Sisesta ühe bussi kohtade arv: ").strip()

#if inimesed.isdigit() and kohad.isdigit():
 #   inimesed = int(inimesed)
 #   kohad = int(kohad)
 #   if inimesed > 0 and kohad > 0:
   #     bussid = inimesed // kohad
   #     viimases = inimesed % kohad
    #    if viimases > 0:
    #        bussid += 1
     #   else:
     #       viimases = kohad
     #   print(f"Inimesi kokku: {inimesed}")
   #    print(f"Bussikohti igas bussis: {kohad}")
    #    print(f"Vaja busse: {bussid}")
    #    print(f"Viimases bussis on {viimases} inimest.")
   # else:
    #    print("peab olema vähemalt 1 inimene ja koht!!")
#else:
  #  print("Palun sisesta ainult täisarvud!")

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


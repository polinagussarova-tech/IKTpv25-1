import glob
import os
from datetime import datetime

f=open('Kasutajad.txt', 'r')
print(dir(f))
f.close()

#1 funktsioon leia_projektifailid(laiend):
def leia_projektifailid(laiend):
    if not laiend.startswith("."):
        laiend="."+laiend
    return glob.glob(f"*{laiend}")

#2 funktsioon analuusi_faili_sisu(failitee): Loeb faili ridade kaupa.
def analuusi_faili_sisu(failitee):
    ridade_arv=0
    tuhjad_read=0
    marksõnad=0

    with open(failitee,'r',encoding='utf-8') as f:
        for rida in f:
            ridade_arv+=1
            marksõnad+=rida.count("TODO")
            marksõnad+=rida.count("FIXME")

            if rida.strip()=="":
                tuhjad_read+=1

    return [ridade_arv, tuhjad_read, marksõnad]

#3 funktsioon loo_raporti_kataloog(nimi="Analüüsi_Raportid"):
def loo_raporti_kataloog(nimi="Analüüsi_Raportid")->bool:
    if not os.path.exists(nimi):
        os.mkdir(nimi)
        return True
    return False

#4 funktsioon leia_failid_algustahega(taht):
def leia_failid_algustahega(taht):
    return glob.glob(f"{taht}*.*")

#5 funktsioon otsime faili mingid kaustas
def otsi_faili(faili_nimi, otsingu_tee="."):
    for juur, kaustad, failid in os.walk(otsingu_tee):
        if faili_nimi in failid:
            return os.path.join(juur, faili_nimi)
    return "faili ei leitud"

#Näide kasutamisest
otsitav_fail=input("Sisesta itsitava faili nimi (nt minu_fail.txt): ")
tulemus=otsi_faili(otsitav_fail)
print(tulemus)
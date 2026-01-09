import glob
import os
from datetime import datetime

f=open('Kasutajad.txt', 'r')
print(dir(f))
f.close()

#1 funktsioon
def leia_projektifailid(laiend):
    if not laiend.startswith("."):
        laiend="."+laiend
    return glob.glob(f"*{laiend}")

#2 funktsioon
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

#3 funktsioon
def loo_raporti_kataloog(nimi="Analüüsi_Raportid"):
    if not os.path.exists(nimi):
        os.mkdir(nimi)
    return nimi

#4 funktsioon
def leia_failid_algustahega(taht):
    muster=f"{taht}*.*"
    failid=glob.glob(muster)
    return failid
import os
import analuusator
from datetime import datetime

while True:

    valik=int(input("Sisesta number: (0-4)"))

    if valik==0:
        print=("Head aega!")
        break

    elif valik==1:
        print(f"praegune kaust: {os.getswd()}")
        faililaiend=input("Sisesta faililaiend (nt: .py, .txt, .java): ")
        failid=analuusator.leia_projektifailid(faililaiend)
        print(failid)

    elif valik==2:
        failid=analuusator.leia_projektifailid
        kaust=analuusator.loo_raporti_kataloog



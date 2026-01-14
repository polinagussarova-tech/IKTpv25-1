import os
import analuusator
from datetime import datetime

failid = []

while True:

    valik=int(input("Sisesta number: (0-4)"))

    if valik==0:
        print("Head aega!")
        break

    elif valik == 1:
        print("praegune kaust:", os.getcwd())
        faililaiend = input("Sisesta faililaiend (nt: .py, .txt, .java): ")
        failid = analuusator.leia_projektifailid(faililaiend)
        print(failid)

    elif valik==2:
        fail=input("Sisesta faili nimi: ")

        tulemus=analuusator.analuusi_faili_sisu(fail)
        print(f"Ridade arv: {tulemus[0]}")
        print(f"Tühjad read: {tulemus[1]}")
        print(f"TODO/FIXME: {tulemus[2]}")

    elif valik==3:
        küsimus=input("Kas te tahate kustuta faili? (Jah/Ei)")
        while True:
            if küsimus=='Jah':
                kaust="Analüüsi_Raportid"
                failid=os.listdir(kaust)

                for fail in failid:
                    os.remove(os.path.join(kaust, fail))
                print("Failid kustutatud.")
            elif küsimus=='Ei':
                print("Kustutamine katkestatud")
        else:
            print("Sisesta ainult Jah või Ei!")

      # if viimane_analuus is None:
      #           print("Kõigepealt tee analüüs (Valik 1)!")
      # else:
      #   kaust = analuusaator.loo_raporti_kataloog()
      #   aeg = datetime.now().strftime("%Y_%m_%d")
      #   failinimi = f"{kaust}/raport_{aeg}.txt"

      #   with open(failinimi, "w", encoding="utf-8") as f:
      #       f.write("Koodiprojekti analüüs\n")
      #       f.write(f"Failide arv: {len(viimane_analuus[0])}\n")
      #       f.write(f"Ridade koguarv: {viimane_analuus[1]}\n")
      #       f.write(f"Tühjade ridade arv: {viimane_analuus[2]}\n")
      #       f.write(f"TODO/FIXME arv: {viimane_analuus[3]}\n")

      #   print("Raport salvestatud:", failinimi)

      # else:
      #     print("Vale valik!")


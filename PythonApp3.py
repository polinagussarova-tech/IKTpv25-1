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



#TÖÖÖÖ on vajalikk

print("Tere maailm!")

#Lineaarsed programmid

Aritmeetilised põhioperatsioonid

Operatsioon	Sümbol	Näide	Tulemus
Astendamine	**	2 ** 3	     8
Korrutamine	*	4 * 5        	20 умножение
Jagamine	/	7 / 2       	3.5 деление 
Jagamise täisarvuline osa	//	7 // 2	    3 елочисленная часть деления
Jagamisjääk	%	7 % 2	     1 Остаток распределения
Liitmine	+	10 + 3	     13 плюс
Lahutamine	-	9 - 4	      5 минус

Tehted tekstidega

Tehe	Kirjeldus	Näide	Tulemus
+	tekstide liitmine	"Tere " + "maailm"	"Tere maailm"
*	teksti kordamine	"ha" * 3	"hahaha"

Võrdlusoperatsioonid

Operatsioon	Sümbol	Näide	Tulemus
Võrdne	==	  5 == 5	  True
Ei võrdu	!=	 4 != 2	   True
Väiksem	<	  3 < 5	    True
Suurem	>	  7 > 2	      True
Väiksem või võrdne	<=	 5 <= 5	     True
Suurem või võrdne	>=	 6 >= 8	      False

Loogilised operatsioonid

Operatsioon	    Kirjeldus	      Näide	       Tulemus
not	   eitab (muudab vastupidiseks)	   not True	     False
and	   tõene, kui mõlemad on tõesed	    True and False	     False
or	   tõene, kui vähemalt üks on tõene	     False or True	     True


Funktsioon	Kirjeldus	Näide	        Tulemus
type(x)	    näitab muutuja tüüpi	     type(5)	<class 'int'>
int(x)	    teisendab täisarvuks	     int(3.7) → 3	
float(x)	     teisendab ujukomaarvuks	    float("4.5") → 4.5	
str(x)	     teisendab tekstiks	    str(123) → "123"



модули
Mooduli importimine
Et moodulit kasutada, tuleb see importida:

import mooduli_nimi

Või ainult osa moodulist:

from mooduli_nimi import *
Näited:

import math
import random
from math import sqrt, pi



Командование	Описание
dir()	Отображает все используемые имена (переменные, функции и т. д.).
dir(objekt)	Отображает свойства и методы заданного объекта.
Пример:

import math
print(dir(math))

МАТЕМАТИКАЕЕ

Модуль mathсодержит функции и константы для математических вычислений.

Основные характеристики
Функция	Объяснение	Пример
math.ceil(x)	Округляет число в большую сторону.	math.ceil(3.1)→4
math.floor(x)	Округляет число в меньшую сторону.	math.floor(3.9)→3
math.trunc(x)	Удаляет дробные значения (только целые числа).	math.trunc(3.7)→3
math.fabs(x)	Возвращает абсолютное значение числа.	math.fabs(-5)→5.0
math.factorial(x)	Вычисляет факториал	math.factorial(5)→120
math.sqrt(x)	Вычисляет квадратные корни	math.sqrt(9)→3.0
math.pow(x, y)	Вычисляет xв степениy	math.pow(2, 3)→8.0
math.log(x, base)	Логарифм (натуральный логарифм по умолчанию)	math.log(8, 2)→3.0
math.log10(x)	Логарифм по основанию 10	math.log10(100)→2.0
math.exp(x)	Вычисляетeˣ	math.exp(1)→2.718...
math.modf(x)	Возвращает дробную и целую части.	math.modf(5.6)→(0.6, 5.0)
math.hypot(x, y)	Вычисление гипотенузы	math.hypot(3, 4)→5.0
math.degrees(x)	Преобразует радианы в градусы	math.degrees(math.pi)→180.0
math.radians(x)	Преобразует градусы в радианы.	math.radians(180)→3.1415...


🔸 Тригонометрические функции (в радианах!)
Функция	Описание	Пример
math.sin(x)	Синус	math.sin(math.pi/2)→1.0
math.cos(x)	Косинус	math.cos(0)→1.0
math.tan(x)	Касательная	math.tan(math.pi/4)→1.0
math.asin(x)	Арксине	math.asin(1)→1.57
math.acos(x)	Аркозин	math.acos(0)→1.57
math.atan(x)	Арктангент	math.atan(1)→0.785

Полезные константы
Постоянный	Значение	Ценить
math.pi	π (пи)	3.1415926...
math.e	Число Эйлера	2.718281...


🎲 Модуль генерации случайных чисел — генерирует случайные значения
Этот модуль randomпозволяет генерировать случайные числа , символы и элементы из списков .

Функция	Описание	Пример
random.randint(a, b)	Случайное целое число от aдоb	random.randint(1, 10)→ например7
random.random()	Случайное число от 0 до 1	random.random()→0.5342...
random.uniform(a, b)	Случайное число с плавающей запятой в диапазоне aот доb


VALIKUD

🧩 Põhistruktuurid
1️⃣ Lihtne if-lause
if tingimus:
    tegevus
Kui tingimus on True, täidetakse tegevus.
Kui tingimus on False, jätkatakse programmi ilma tegevust tegemata.

Näide:

x = 5
if x > 0:
    print("Positiivne arv")

2️⃣ If…else
if tingimus:
    tegevus_1
else:
    tegevus_2
Kui tingimus on True, täidetakse tegevus_1, vastasel juhul tegevus_2.

Näide:

x = int(input("Sisesta arv: "))
if x == 1:
    print("Õige")
else:
    print("Vale")
3️⃣ If…elif…else
if tingimus_1:
    tegevus_1
elif tingimus_2:
    tegevus_2
else:
    tegevus_3
Kontrollitakse järjest tingimusi.
Kui üks neist on True, täidetakse vastav tegevus ja ülejäänuid enam ei kontrollita.

Näide:

x = int(input("Sisesta arv -5 kuni 5: "))
if x < -5:
    print("Vähe")
elif -5 <= x <= 5:
    print("OK")
else:
    print("Palju")

Полезные встроенные функции
Функция	Описание
abs(x)	Возвращает абсолютное значение числа.
bool(x)	Делает значение логичным (Истинно/Неверно)
int(x)	Преобразует значение в целое число.
float(x)	Преобразует значение в число с плавающей запятой.
len(x)	Возвращает количество элементов в объекте (например, длину строки).
max(seq)	Наибольший элемент в последовательности
min(seq)	Наименьший элемент в последовательности
sum(seq)	Сумма элементов
range(start, stop, step)	Последовательность чисел с фиксированным шагом
print(obj)	Отображается на экране
input(prompt)	Запрашивает у пользователя ввод данных.


Цикл	Когда использовать	Пример
while	Если вы точно не знаете, сколько раз должен повториться цикл, но знаете условие завершения.	Вы запрашиваете у пользователя подтверждение, пока он не введёт правильный ответ.
while True+break	Когда условие завершения возникает внутри цикла.	Игра прерывается, когда игрок нажимает кнопку «Выход».
for	Если вы точно знаете, сколько раз повторяется цикл.

 5. Та же задача с циклом FOR
for i in range(1, 31, 2):   # 🔢 Algab 1-st, kuni 31-ni, samm 2
    print(i, end=" ")
💬 Результат:1 3 5 7 9 11 13 15 17 19 21 23 25 27 29


🌀 цикл while
Цикл выполняется до тех пор, пока условие истинно .

while tingimus:
    tegevus
📘 Пример:

x = 0
while x <= 10:
    print(x)
    x += 1
➡ Отображает числа от 0 до 10.



Бесконечный цикл
while True:
    print("Ctrl+C lõpetab!")
➡ Цикл выполняется бесконечно, пока его не прервут вручную (Ctrl + C).



🔢 Функцияrange()
Используется для создания числовых последовательностей.

Пример	Результат
range(10)	0–9
range(2, 12)	2–11
range(2, 12, 3)	2, 5, 8
range(12, 2, -2)	12, 10, 8, 6, 4


⏹️ Прерывание и продолжение цикла
Командование	Операция
break	полностью разрывает порочный круг
continue	продолжается со следующей итерацией цикла
pass	Ничего не делает, используется для временного заполнения пустого пространства.
📘 Примеры:

for i in range(5):
    if i == 3:
        continue
    print(i)
➡ Результат: 0, 1, 2, 4

for i in range(5):
    if i == 3:
        break
    print(i)
➡ Результат: 0, 1, 2


LISTID

⚙️ Наиболее распространенные методы
Метод	Описание	Пример
append(x)	Добавляет в конец элемента	loend.append(5)
extend(L)	Добавляет все элементы в конец второго списка.	loend.extend([6,7])
insert(i, x)	Добавляет элемент в определённую позицию.	loend.insert(1, 99)
remove(x)	Удаляет первый совпадающий элемент.	loend.remove(25)
pop(i)	Удаляет и возвращает элемент.	loend.pop()
index(x)	Возвращает индекс элемента.	loend.index(30)
count(x)	Подсчитывает, сколько раз встречается это значение.	loend.count(10)
sort()	Сортирует список	loend.sort()
reverse()	Меняет порядок на обратный	loend.reverse()
clear()	Очищает список	loend.clear()
📌 Внимание! Большинство из них изменяют список напрямую — нет необходимости создавать новую переменную.

Функции, работающие со списками, содержащими числа.
max()
Находит наибольшее число в списке.

numbrid = [3, 10, 1]
print(max(numbrid))  # 10
min()
Находит наименьшее число.

print(min(numbrid))  # 1
sum()
Вычисляет сумму всех чисел.

print(sum(numbrid))  # 14



РАБОТА В ДЛВУХ ФАЙЛАХ
 Общая структура функции
def funktsiooni_nimi(parameetrid):
    """Funktsiooni kirjeldus (docstring)"""
    tegevused
    return väärtus
🧩 Объяснение
def– ключевое слово, с которого начинается функция

funktsiooni_nimi– имя, под которым функцию можно будет вызвать позже.

(parameetrid)– значения, передаваемые в функцию (могут также быть пустыми скобками)

:– двоеточие в конце заголовка функции

Отступы – все команды функций должны быть с отступом.

return– завершает функцию и возвращает результат.

💡 Если returnв функции нет оператора, она автоматически возвращает значение None.


✍️ Простой пример
def tervita():
    print("Tere tulemast!")
Вызов функции :

tervita()


🧮 Функция, возвращающая значение
def summa(a, b):
    return a + b

tulemus = summa(2, 3)
print(tulemus)  # 5
📘 Функция может возвращать значение , которое можно сохранить в переменной или использовать немедленно.


🔤 Эта функция также работает с текстом.
def liida_tekst(a, b):
    return a + b

print(liida_tekst('Tere', ' maailm'))  # 'Tere maailm'



🔢 Функция, возвращающая несколько значений
def summa_ja_korrutis(a, b):
    s = a + b
    k = a * b
    return s, k

summa, korrutis = summa_ja_korrutis(5, 4)
print(summa)     # 9
print(korrutis)  # 20
💡 Возвращаемые значения могут быть «распакованы» в несколько переменных.




.

🧾 Вызов функции с использованием пользовательского ввода
def korruta(a, b):
    return a * b

x = int(input("Sisesta esimene arv: "))
y = int(input("Sisesta teine arv: "))

print("Korrutis on:", korruta(x, y))




📘 Документация по функциям
В начале функции может быть строка документации, или docstring
, которая объясняет, что делает эта функция. Она отображается, например, help()с помощью команды.

def korruta(a: int, b: int) -> int:
    """Tagastab kahe arvu korrutise."""
    return a * b



⚡ Анонимные функции ( lambda)
Лямбда-функция — это короткая, однострочная функция без имени.
Она работает так же, как и обычная defлямбда-функция, но более компактна и быстрее для простых вычислений.

Пример 1:
summa = lambda a, b: a + b
print(summa(3, 4))  # 7
Пример 2:
korruta = lambda x, y: x * y
print(korruta(2, 5))  # 10
Пример 3 (слияние текста):
ühenda = lambda a, b: a + b
print(ühenda('a', 'b'))  # 'ab'
💡 В функциях lambdaне используются никакие returnоператоры — результат возвращается автоматически.





✅ Краткое содержание
Определение	Объяснение
Функция	Многократно используемый блок кода для выполнения конкретной задачи.
деф	Ключевое слово для определения функции
возвращаться	Возвращает результат функции
Никто	Значение по умолчанию, если returnотсутствует .
Докстринг	Описание функции в тройных кавычках
лямбда	Сокращенная форма для однострочных функций
Аргументы	Значения, которые функция использует для работы.

на эстике

Mõiste	Selgitus
Funktsioon	Korduvkasutatav koodiplokk kindla ülesande täitmiseks
def	Märksõna funktsiooni määratlemiseks
return	Tagastab funktsiooni tulemuse
None	Vaikeväärtus, kui return puudub
Docstring	Funktsiooni kirjeldus kolmekordsete jutumärkide vahel
lambda	Lühivorm üherealiste funktsioonide jaoks
Argumendid	Väärtused, mida funktsioon kasutab tööks



💬 Näide terviklikust programmist
def tervita(nimi):
    """Tervitab kasutajat nime järgi."""
    return "Tere, " + nimi + "!"

nimi = input("Sisesta oma nimi: ")
print(tervita(nimi))



#
#
#
#Фигура	Что значит
print("Овал	 ovaal  Начало / Конец")
print("Прямоугольник    ristkülik	Действие")
print("Параллелограмм   rööpkülik	Ввод / вывод)
print("Ромб	  romb     Условие")

#(Овал)
 # ↓
#(Параллелограмм)
 # ↓
#(Прямоугольник)
 # ↓
#(Ромб)
#  ↓       ↓
#(Да)    (Нет)
#  ↓       ↓
#(Прямоугольник)
 # ↓
#(Овал)  

    #  Terminator (овал)
#
#➡ Начало или конец программы

#Пишут:
#
#Start

#End

#Начало

#Конец

#⬛ Process (прямоугольник)

#➡ Действие / вычисление
#
#Пишут:

#Считать файл

#Подсчитать баллы

#Добавить пользователя

#Отправить email

🟦 #Data (параллелограмм)

#➡ Ввод или вывод данных

#Пишут:

#Ввести имя

#Вывести результат

#Показать сообщение

#📌 Всё, где input() или print()
#🔷 Decision (ромб)

#➡ Условие / выбор (ДА / НЕТ)

#Пишут:
#
#Ответ правильный?
#
#Пользователь уже есть?

#Баллы > половины?

#📌 Из ромба всегда два выхода:

#Да / True

#Нет / False
#

#Predefined process (Предопределённый процесс)

#👉 Это вызов функции / подпрограммы

#Что туда пишут:

#testimine()
#
#emaili_saatmine()

#raport_tooandjale()

#andmete_lugemine_failidest()

#📌 То есть: здесь вызывается уже готовая функция, детали которой описаны отдельно.


#    Preparation (Подготовка)

#👉 Это подготовка данных / начальные настройки

#Что туда пишут:

#N = 3

#punktid = 0

#kus_vas = {}

#loendur = 0

#juba_testitud = []

#📌 Используется перед началом основного процесса.

#штуки важные

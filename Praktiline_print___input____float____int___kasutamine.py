#10------------
from math import *

import("Ajateisendus")

V=float(input("sisesta aja minutites: "))

t=int(v//60)

sec=int(v%60)

print(f"minutes {t}: sekundid {sec}")



#9-------------
from math import *

print("Rulluisutajad")

print("Rulluisutaja keskmine kiirus on 29, 9km/h")

m=24/60

t=m*29.9

t=round(t,2)

print(f"Vastus: {t}km")

print()



#8--------------
from math import *

print("k�tusekulu arvutamine")

l=float(input("kasutaja sisestab tangitud k�tuse liitrid: "))

km=float(input("kasutaja sisestab l�bitud kilomeetrid: "))

p=l/km*100

print (f"Vastus: {p}l/km")

print()



#7--------------
from math import *

print("Pitsa V�tsite 3 s�braga suure pitsa hinnaga 12,90� te j�tate teenindajal")

s=10*12.90/100

s=round(s)

d=(12.90+s)

p=d/3

p=raund(p,1)

print (f" Iga s�ber peab maksma: {p}�")

print()

#6--------------
from math import *
from random import *
a=randint (1,100)
b=randint (1,100)
c=randint (1,100)
print(f"k�lg a={a}/nK�lg b={b}/ nk�lg c={c}")
print(f"kolmnurga �mberm��t = {a+b+c}")
print()



#5---------------
print("   @..@")
print("  (----)")
print(" ( \__/ )")
print("  ^^ "" ^^ ")
print()



#4----------------
from math import *
from re import I
print("keskmine")
a=float(input("1 number =>"))
b=float(input("2 number =>"))
v=float(input("3 number =>"))
h=float(input("4 number =>"))
d=float(input("5 number =>"))
m=(a+b+v+h+d)/5
print(f"keskmine on {m}")



#3-----------------
print("harjutus")
aeg = float(input("mitu tundi kulus s�idub ? "))
teepikkus = float(input("Mitu kilomeetrit s�itsid? "))
kiirus = aeg / teepikkus
print()
print("sinu kirus oli " + str(round(kiirus,2)) + " km/h")



#2-----------------
from math import *
print("Ristk�likukujulise maatk�ki diagonaal")
N=float(input("Sisesta ristk�liku 1. k�lje pikkus => "))
M=float(input("Sisesta ristk�liku 2. k�lje pikkus => "))
d=sqrt(N**2+M**2)
print(f"Maat�ki diagonaal on {d} m**2")



#1-----------------
from math import *
print("Puu l�bim��du arvutamine")
C=float(input("puu �mberm��t: "))
r=C/(2*pi)
print()
print("Puu radius", round(r,2))
d=2*r
print("Puu diagonal", round(d,2))
print(f"Vastus:/nPuu l�bim��duga {C} �mberm��t v�rdub {d}")

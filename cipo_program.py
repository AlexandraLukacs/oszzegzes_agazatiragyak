from Cipo import Cipo


peldany1 = Cipo("Nike", 42)
peldany2 = Cipo("Adidas", 41)
peldany3 = Cipo("Adidas", 45)

cipo_lista = []
cipo_lista.append(peldany1)
cipo_lista.append(peldany2)
cipo_lista.append(peldany3)

for i in range(0, len(cipo_lista), 1):
    nev = cipo_lista[i].nev
    meret = cipo_lista[i].meret
    print(f"{nev}: ({meret})")

def meret_atlag():
    ossz: int= 0
    for i in range(0, len(cipo_lista), 1):
        ossz += cipo_lista[i].meret
    print(round(ossz / len(cipo_lista), 3))

meret_atlag()

def nagyobb42adidas():
    print("Van-e 42-esnél nagyobb Adidas: ", end="")
    van = False
    for i in range(0, len(cipo_lista), 1):
        if cipo_lista[i].nev =="Adidas" and cipo_lista[i].meret > 42:
            van = True
    if van == True:
        print("Van")
    else:
        print("Nincs")

# , end="" = nem lesz sortörés 

print("")
nagyobb42adidas()
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

#Összegzés tétel
# Egy sorozathoz egy értéket rendel
def meret_atlag():
    ossz: int= 0
    for i in range(0, len(cipo_lista), 1):
        ossz += cipo_lista[i].meret
    print(round(ossz / len(cipo_lista), 3))

meret_atlag()


#Maximum kiválasztás tétel
# Egy sorozathoz egy értéket rendel
def legnagyobb():
    #legnagyobb méretet nézi
    print("Milyen márkájú a legnagyobb méretű cipő: ", end="")
    max: int= 0
    for i in range(1, len(cipo_lista), 1):
        if cipo_lista[i].meret > max:
            max = cipo_lista[i].meret
    print(f"{cipo_lista[i].nev}")

def legnagyobb2():
    #legnagyobb helyet nézi
    print("Milyen márkájú a legnagyobb méretű cipő: ", end="")
    max: int= 0
    for i in range(1, len(cipo_lista), 1):
        if cipo_lista[i].meret > cipo_lista[max].meret:
            max = i
    print(f"{cipo_lista[i].nev}")

legnagyobb()
legnagyobb2()

#Megszámlálás
#Hány db adidas cipőnk van?
def db_adidas():
    print("Hány db adidas cipőnk van: ", end="")
    db: int= 0
    for i in range(0, len(cipo_lista), 1):
        if cipo_lista[i].nev == "Adidas":
            db += 1
    print(f"{db} db")

db_adidas()

    

#Eldöntés tétel
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
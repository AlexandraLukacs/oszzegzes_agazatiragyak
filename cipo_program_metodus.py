from Cipo import Cipo


def pldListaba():
    peldany1 = Cipo("Nike", 42)
    peldany2 = Cipo("Adidas", 41)
    peldany3 = Cipo("Adidas", 45)

    cipok = []
    cipok.append(peldany1)
    cipok.append(peldany2)
    cipok.append(peldany3)
    return cipok

def listaKiir(lista):
    for i in range(0, len(lista), 1):
        nev = lista[i].nev
        meret = lista[i].meret
        print(f"{nev}: ({meret})")


#rövid verzió:
"""listaKiir(pldListaba())"""

#hosszú verzió:
"""cipok_lista=pldListaba()
listaKiir(cipok_lista)"""


def osszegzes_tetele(cipok):
    ossz: int= 0
    for i in range(0, len(cipok), 1):
        ossz += cipok[i].meret
    atlag = ossz / len(cipok)
    print(round(atlag, 3))

"""osszegzes_tetele(cipok_lista)"""


def maximum_kiválasztás_tetele(cipok):
    #legnagyobb helyet nézi
    print("Milyen márkájú a legnagyobb méretű cipő: ", end="")
    max: int= 0
    for i in range(1, len(cipok), 1):
        if cipok[i].meret > cipok[max].meret:
            max = i
    print(f"{cipok[i].nev}")

"""maximum_kiválasztás_tetele(cipok_lista)"""


def megszamlalas_tetele(cipok):
    print("Hány db adidas cipőnk van: ", end="")
    db: int= 0
    for i in range(0, len(cipok), 1):
        if cipok[i].nev == "Adidas":
            db += 1
    print(f"{db} db")

"""megszamlalas_tetele(cipok_lista)"""


def eldontes_tetele(cipok):
    n: int= int(input(f"\nszám: "))
    prim = bool
    if n < 2:
        prim = False
    else:
        i = 2
        while i <= math.sqrt(n) and n % i != 0:
            i += 1
        prim = i > math.sqrt(n)
    if prim == False:
        print("Nem prím")
    else:
        print("Prím")

"""eldontes_tetele(cipok_lista)"""

#rövid verzió:
"""listaKiir(pldListaba())"""

#hosszú verzió:
cipok_lista=pldListaba()
listaKiir(cipok_lista)

osszegzes_tetele(cipok_lista)
maximum_kiválasztás_tetele(cipok_lista)
megszamlalas_tetele(cipok_lista)
eldontes_tetele(cipok_lista)
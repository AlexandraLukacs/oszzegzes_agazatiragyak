import math

def fel():
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

# bool = True vagy False
# % = maradékos osztás
# math.sqrt(n) = n szám gyöke
# && = és itt a programban and
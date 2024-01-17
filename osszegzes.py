def osszegzes_fel():
    n: int= 0
    i: int = 1
    ossz: int= 0
    while (n <= 0):
        n: int= int(input("N="))
    for i in range(0, n+1):
        ossz += i
    print(f"Az első {n} db természetes szám összege: {ossz}")

def szorzas_fel():
    n: int= 0
    i: int = 1
    ossz: int= 1
    while (n <= 0):
        n: int= int(input("N="))
    for i in range(0, n+1):
        ossz *= i
    print(f"Az első {n} db természetes szám összege: {ossz}")
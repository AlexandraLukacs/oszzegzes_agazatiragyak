def osszegzes_fel():
    ossz: int= 0
    i: int =1
    n: int= int(input("N="))
    while n < 0:
        for i in range(0, n, 1):
            if i > n:
                ossz += i
        i += 1
    print(f"Az első {n} db természetes szám összege: {ossz}")

        
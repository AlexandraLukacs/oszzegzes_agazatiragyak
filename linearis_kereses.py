def lin_ker():
    also: int= 42
    felso: int= 67
    i = also
    while i <= felso and not(i % 10 == 0):
        i += 1
    van = i <= felso
    if van:
        print("van 0-ra végződő szám: " + str(i))
    else:
        print("nincs 0-ra végződő szám")

lin_ker()
import math

def osztok(szam):
    osztoi = []
    for i in range(2, round(math.sqrt(szam)+1)): 
        if szam % i == 0:
            osztoi.append(i)
    return osztoi

print(osztok(10008))

def osztok2(szam):
    osztoi = []
    i = 2
    while i <= math.sqrt(szam):
        if szam % i == 0:
            osztoi.append(i)
        i += 1
    return osztoi
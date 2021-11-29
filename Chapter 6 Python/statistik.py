def sum(*angka):
    x=0
    for i in angka :
        x+=i
    return x

def average(*angka) :
    x=0
    y=0
    for i in angka :
        x+=i
        y+=1
    rata = x/y
    return rata

def maks (*angka):
    a = max(angka)
    return a

def mins(*angka) :
    a = min(angka)
    return a
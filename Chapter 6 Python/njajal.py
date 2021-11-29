def luassegitiga (a,t):
    luas = a * t / 2
    return luas 

alas = 10
tinggi = 20
alas1 = 15
tinggi1 = 45
print('Luas segitiga dg alas ',alas,'dan tinggi ',tinggi, 'adalah', luassegitiga(alas,tinggi))
print('Luas segitiga dg alas ',alas1,'dan tinggi ',tinggi1, 'adalah', luassegitiga(alas1,tinggi1))

total1 = luassegitiga(alas,tinggi)
total2 = luassegitiga(alas1,tinggi1)

print (total1 + total2)
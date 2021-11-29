def faktorial(n):
    y=1
    while(n>0) :
        y*=n
        n-=1
    return y

a = faktorial(5)
b = faktorial (3)
hasil = a/b
print('C(5,3) =', hasil)


a= faktorial(10)
b= faktorial(7)
hasil = a/b
print('P(10,7) =', hasil)
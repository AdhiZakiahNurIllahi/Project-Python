def isPythagoras (a,b,c):
    if (a**2 + b**2 == c**2) :
        print('a=',a, 'b=',b, 'c=',c, '-> True')
    else :
        print('a=',a, 'b=',b, 'c=',c, '-> False')

#a.	a = 3, b = 4, c = 5	-> True
isPythagoras (3,4,5)
#b.	a = 5, b = 9, c = 12 -> False
isPythagoras (5,9,12)
#c.	a = 8, b = 6, c = 10 -> True
isPythagoras(8,6,10)
#d.	a = 7, b = 8, c = 11 -> False
isPythagoras(7,8,11)

print ('-' * 30)
print ('  PROGRAM HITUNG RATA - RATA    ')
print ('-' * 30)

total = 0
pembagi = 0
while True :
    try :
        bil = int(input('Masukkan bilangan bulat : '))
        total += bil
        if total != 0 :
            pembagi += 1
        elif total == 0 :
            pembagi += 0
#perulangan
        ulang = input('lagi y/n :')
        if ulang == 'y' :
            continue
        elif ulang == 'n' :
            print('\nRata - ratanya adalah :',total/pembagi)
            break
        else :
            print ('input yang anda masukkan salah')
            break
    except ValueError :
        print ('Bukan bilangan bulat')
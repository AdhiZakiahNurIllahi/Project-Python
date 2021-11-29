data = input('Masukkan nama file : ')
while True : 
    try :
        file = open(data, 'r')
        file = open(data, 'a')
        write = input ('Data yang mau ditambahkan :')
        file.write(write)  
    except FileNotFoundError :
        print('Data tidak ditemukan')
        break
#Perulangan
    ulang = input('Mau lagi y/n :')
    if ulang == 'y' :
        print()
    elif ulang == 'n' :
        break
    else :
        print ('input yang anda masukkan salah')
        break





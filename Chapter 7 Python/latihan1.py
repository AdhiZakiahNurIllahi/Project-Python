data = input("Masukkan nama file : ")
try:
    file = open(data,'r')
    print('isi file :',data,file.read())
except:
    print('Input yang anda masukkan salah')
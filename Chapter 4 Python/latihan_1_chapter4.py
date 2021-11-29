
#tarif
tarifawal = 200000 #12jam
tarifberikutnya = 10000 #per 1 jam
tarifberikutnya1 = tarifberikutnya/60 #biaya permenit menitnya

#waktu
waktupeminjaman = 06.00
waktupengembalian = 23.50

lamarental = int(waktupengembalian-waktupeminjaman)

#menghitung waktu rental setelah 12 jam
lamarentalberikutnya = lamarental-12

#menghitung biaya yang dikeluarkan
tarifrentalsetelah12jam = lamarentalberikutnya*tarifberikutnya
totalbiaya = tarifawal+tarifrentalsetelah12jam+(tarifberikutnya1*50)
print (round(totalbiaya))

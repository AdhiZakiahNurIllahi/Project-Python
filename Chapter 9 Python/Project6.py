nilai = [{'nim' : 'A01', 'nama' : 'Agustina', 'mid' : 50, 'uas' : 80}, 
	 {'nim' : 'A02', 'nama' : 'Budi', 'mid' : 40, 'uas' : 90}, 
         {'nim' : 'A03', 'nama' : 'Chicha', 'mid' : 100, 'uas' : 50}, 
         {'nim' : 'A04', 'nama' : 'Donna', 'mid' : 20, 'uas' : 100}, 
	 {'nim' : 'A05', 'nama' : 'Fatimah', 'mid' : 70, 'uas' : 100}]

print('==========================================================')
print('NIM       NAMA         N.MID   N.UAS   N.AKHIR    STATUS')
print('----------------------------------------------------------')

for data in nilai:
    nakhir = (data['mid'] + (2 * data['uas']))/3
    status = "LULUS"
    if(nakhir < 60):
        status = "TIDAK LULUS"
    print(data['nim'].ljust(9),data["nama"].ljust(11),str(data["mid"]).rjust(6),str(data["uas"]).rjust(7),str(round(nakhir,2)).rjust(9),status.rjust(9))

print('----------------------------------------------------------')
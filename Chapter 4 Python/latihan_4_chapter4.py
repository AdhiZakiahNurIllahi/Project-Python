
#perjalanan pak amir
jarakAB = 125
rata1 = 62
jarakBC = 256
rata2 = 70
istirahat = 45
berangkat = 06.00

#waktu dari A ke B
waktuAB = jarakAB//rata1
menitAB = round((jarakAB%rata1)/rata1*60)

#waktu dari B ke C
waktuBC = jarakBC//rata2
menitBC = round((jarakBC%rata2)/rata2*60)

waktujamsampai   = (berangkat + waktuAB + waktuBC)
waktumenitsampai = (menitAB + menitBC + istirahat)
if (waktumenitsampai >= 60):
	waktujamsampai += 1
	waktumenitsampai -= 60

	
print("Waktu sampai yaitu jam %d.%d" % (waktujamsampai,waktumenitsampai))


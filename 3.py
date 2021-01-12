import datetime
kode = input("Masukkan Kode Member :")
if(kode == 'M02'):
    buka = open("data.txt", 'r')
    teks = buka.read()
    print(teks)
    buka.close()
tgl2 = datetime.date(2018,12,18)
tgl1 = datetime.date(2018,12,26)
selisih = tgl1-tgl2
print ('Terlambat               :',selisih)
print ('Denda                   :', 8*2000)


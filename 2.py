kode = input("Masukkan Kode Member :")
nama = input("Masukkan Nama Member :")
judul = input("Masukkan Judul Buku :")
# saat menulis y/n menggunakan huruf kecil yaa...
ulang = (input ("Ulangi lagi (y/n) : "))

if (ulang == 'y'):
    kode = input("Masukkan Kode Member :")
    nama = input("Masukkan Nama Member :")
    judul = input("Masukkan Judul Buku :")
    bukakode = open("dataPeminjam2.txt",'r')
    teks = bukakode.read()
    print(teks)
    bukakode.close()

elif (ulang == 'n'):
    bukakode = open("dataPeminjam.txt", 'r')
    teks = bukakode.read()
    print(teks)
    bukakode.close()


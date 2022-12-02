#BUNGA HARDIYANA PUTRI
#2210312035
#PRAKTIKUM GAME TEBAK ANGKA

import random
angka_tebakan = random.randint (1, 10)
print ("Selamat Datang di Game Tebak Angka")
print ("\n")
print ("Anda harus memilih angka antara", 1, "dan", 10)
kesempatan = 8

while kesempatan > 0 :
    mulai = int(input("Masukkan angka tebakan Anda!"))
    if mulai == angka_tebakan:
        print ("\n")
        print ("Anda Benar! Angka tebakannya adalah:", angka_tebakan)
    
    else:
        print ("\n")
        kesempatan -= 1
        print ("Coba lagi! Kesempatan Anda tersisa:", kesempatan)

    if kesempatan == 0 :
        print ("Maaf, Anda belum beruntung.")
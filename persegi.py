sisi = float(input("Masukkan sisi persegi: "))
pilihan = input("pilih luas/keliling: ")
Hasil = {
    "luas": sisi * sisi, 
    "keliling": 4 * sisi
    }
print(Hasil[pilihan])



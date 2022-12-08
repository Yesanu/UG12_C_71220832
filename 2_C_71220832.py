angka = input("Masukkan Angka: ")
hitung = input ("Masukkan Angka Yang Dihitung: ")
jumlah = 0

for i in range(len(angka)):
    if angka[i] == hitung:
        jumlah += 1

print("angka {} muncul sebanyak {} kali".format(hitung, jumlah))

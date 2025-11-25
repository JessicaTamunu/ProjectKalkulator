print("=== KALKULATOR SEDERHANA ===")
print("1. Tambah")
print("2. Kurang")
print("3. Kali")
print("4. Bagi")

pilihan = input("Pilih operasi (1-4): ")

angka1 = float(input("Masukkan angka pertama: "))
angka2 = float(input("Masukkan angka kedua: "))

if pilihan == "1":
    print("Hasil:", tambah(angka1, angka2))
elif pilihan == "2":
    print("Hasil:", kurang(angka1, angka2))
elif pilihan == "3":
    print("Hasil:", kali(angka1, angka2))
elif pilihan == "4":
    print("Hasil:", bagi(angka1, angka2))
else:
    print("Pilihan tidak valid.")

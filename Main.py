def main():
  print("=== KALKULATOR SEDERHANA ===")
  print("1. Tambah")
  print("2. Kurang")
  print("3. Kali")
  print("4. Bagi")

pilihan = input("Pilih operasi (1-4): ")

a = float(input("Masukkan angka pertama: "))
b = float(input("Masukkan angka kedua: "))

 if pilihan == "1":
        print("Hasil:", tambah(a, b))
 elif pilihan == "2":
        print("Hasil:", kurang(a, b))
 elif pilihan == "3":
        print("Hasil:", kali(a, b))
 elif pilihan == "4":
        print("Hasil:", bagi(a, b))
 else:
        print("Pilihan tidak valid.")

print("""
  SELAMAT DATANG DI KALKULATOR SEDERHANA
""")

awal = int(input("Pilih : 1) Pertambahan 2) Pengurangan 3) Perkalian 4) Pembagian : "))
angka1 = int(input("masukkan angka pertama : "))
angka2 = int(input("masukkan angka kedua : "))

if awal == 1:
  tambah = angka1 + angka2
  print(tambah)
elif awal == 2:
  kurang = angka1 - angka2
  print(kurang)
elif awal == 3:
  kali = angka1 * angka2
  print(kali)
elif awal == 4:
  bagi = angka1 / angka2
  print(bagi)
else:
  print("error")

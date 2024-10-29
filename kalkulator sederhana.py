def kalkulator():
  """Fungsi ini membuat kalkulator sederhana"""

  # Meminta input dari pengguna
  angka1 = float(input("Masukkan angka pertama: "))
  angka2 = float(input("Masukkan angka kedua: "))
  operator = input("Masukkan operator (+, -, *, /): ")

  # Melakukan operasi berdasarkan operator yang dipilih
  if operator == '+':
    hasil = angka1 + angka2
  elif operator == '-':
    hasil = angka1 - angka2
  elif operator == '*':
    hasil = angka1 * angka2
  elif operator == '/':
    if angka2 == 0:
      print("Tidak dapat membagi dengan nol")
    else:
      hasil = angka1 / angka2
  else:
    print("Operator tidak valid")

  # Menampilkan hasil
  if 'hasil' in locals():
    print("Hasil:", hasil)

kalkulator()
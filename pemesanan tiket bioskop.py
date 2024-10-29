def hitung_harga_tiket():
  """Fungsi untuk menghitung harga tiket bioskop"""

  # Harga dasar tiket
  harga_reguler = 50000
  harga_vip = 100000
  diskon_member = 0.2 

  # Meminta input dari pengguna
  tipe_tiket = input("Masukkan tipe tiket (reguler/vip): ").lower()
  status_member = input("Apakah Anda memiliki kartu member? (ya/tidak): ").lower()

  # Menghitung harga tiket berdasarkan tipe tiket dan status member
  if tipe_tiket == "reguler":
    harga_awal = harga_reguler
  elif tipe_tiket == "vip":
    harga_awal = harga_vip
  else:
    print("Tipe tiket tidak valid.")
    return

  # Menghitung diskon jika pengguna adalah member
  diskon = harga_awal * diskon_member if status_member == "ya" else 0
  harga_akhir = harga_awal - diskon

  # Menampilkan hasil
  print("Harga tiket yang harus dibayar:", harga_akhir)

hitung_harga_tiket()
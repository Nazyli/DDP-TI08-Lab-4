# DDP LAB-4
# Nama: Evry Nazyli Ciptanto
# NIM: 0110220045

# SOAL 1 - Mencetak nama
# Tuliskan program untuk Soal 1 di bawah ini
print("SOAL 1 - Mencetak nama")
nama = input("Masukkan nama: ") # mendapatkan input pengguna
i = 0 # set awalan variabel i ke 0
while i < len(nama):  # melakukan perulangan sebanyak panjang string
  i +=1 # Agar dimulai indeks ke 1
  print(nama[0:i]) # tampilkan teks sesuai index awal 0 dan index akhir sesuai nilai i


# SOAL 2 - Validasi teks
# Tuliskan program untuk Soal 2 di bawah ini
print("\nSOAL 2 - Validasi teks")
isTeks = True # set awalan variabel ke true
# melakukan perulangan selama kondisi benar
while(isTeks):
  # mendapatkan input pengguna
  b = input("Masukkan sebuah teks: ");
  # kondisi Panjang teks minimal 8
  if(len(b)<8):
    print("Teks",b,"tidak valid karena panjang teks kurang dari 8")
  # kondisi teks mengandung frasa nf 
  elif("nf" not in b.lower()):
    print("Teks",b,"tidak valid karena tidak mengandung frase NF")
  # kondisi teks terakhir yyy
  elif(not b.lower().endswith('yyy')):
    print("Teks",b,"tidak valid karena tidak diakhiri dengan 'YYY' atau 'yyy'")
  # kondisi teks mengandung angka -> catatan ada di bawah
  elif(b.isalpha()):
    print("Teks",b,"tidak valid karena tidak mengandung angka")
  # jika teks sudah tervalidasi, hentikan perulangan dengan mengatur variable isTeks ke false
  else:
    isTeks=False
  print()
print("Teks valid. Program berhenti.")


#  b.isalpha() -> Return true if all characters in the string are alphabetic and there is at least one character, false otherwise.
# https://docs.python.org/2/library/stdtypes.html#str.isalpha
# isdigit() -> Return true if all characters in the string are digits and there is at least one character, false otherwise.
# kata ="asfasfasfasf@#asnfyyy"
# print(any(char.isdigit() for char in kata))


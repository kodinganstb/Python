# PENGERTIAN VARIABLE
# Variable dapat di ibaratkan sebagai wadah, wadah dari suatu data.
# Contohnya variable NAMA berisi data string 'Asifa'

# ATURAN PENULISAN VARIABLE PADA PYTHON
# 1.Nama variable harus dimulai dengan huruf atau underskor(nama, _nama)
# 2.Nama variable tidak boleh dimulai dengan angka
# 3.Nama variable hanya bisa menggunakan gabungan dr huruf dengan angka dan underskor( A-z, 0-9, dan _ )
# 4.Nama variable sangat sensitif dengan huruf besar dan huruf kecil(case-sensitive), (contohnya nama, Nama, NaMa, NAMA adalah variable yang berbeda)

# CONTOH PENULISAN VARIABLE YANG *SALAH
    # nama-depan
    # nama$depan
    # nama@depan
    # 4namadepan

# CONTOH PENULISAN VARIABLE YANG *BENAR
    # nama_depan
    # nama_belakang
    # usia
    # kota
    # nama3
    # nama4

# Contoh Variable pada Python
nama_depan = 'Asifa'                        #type data string
nama_belakang = 'Ahmad'
usia = 19                                   #type data integer
kota = 'Banjarnegara'
skills = ['Programming', 'Design Graphic']  #type data list
info_pribadi = {
    'Nama Depan' : 'Asifa',
    'Nama Belakang' : 'Ahmad',              #type data dictionary
    'Usia' : '19 Tahun',
    'Kota' : 'Banjarnegara'
}

# Menampilkan isi variable menggunakan perintah print()
print(nama_depan)
print(nama_belakang)
print(usia)
print(kota)
print(skills)
print(info_pribadi)
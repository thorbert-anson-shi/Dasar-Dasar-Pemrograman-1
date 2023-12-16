asep = "Variabel Tipe Data Struktur String Integer Float Boolean Pengulangan Kondisi Fungsi Prosedur Array Pointer Pemrograman Berorientasi Objek Pengkodean Logika Kontrol Versi Algoritma Class Metode Operasi Input Output String Integer Float Boolean"
agus = "OOP Variabel DataType String Integer Float List Tuple Dictionary Rekursi Kondisi Fungsi Modul Class Metode Operasi Input Output Logika Komentar File Kode Sintaks Global Local Scope Return Rekursi List Tuple Dictionary"

asep = set(asep.split(" "))
agus = set(agus.split(" "))

print(len(asep & agus)/len(agus))

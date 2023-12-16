# Prints header of program
print("RPG Abal-Abal")

# Asks user for the biodata of the friend character
friend_name = input("Nama Teman: ")
friend_date_of_birth = input("Tanggal Lahir Teman: ")
major = input("Jurusan Teman: ")
friend_class_of = int(input("Angkatan Teman (4 digit): "))

# Prints a short text block
print(
    "Pada suatu hari, kamu lagi jalan-jalan di sivitas UI.\nTiba-tiba, entah dari mana ada seseorang yang menghampiri kamu..."
)

# Asks user for their own name
self_name = input('"Permisi, nama kamu siapa?"\n')
self_major = input('"Kalau boleh tahu, dari jurusan mana ya?"\n')
self_class_of = int(input('"Oooo, angkatan berapa nih?"\n'))

# Compares whether the self or the friend is younger, and responds appropriately
if friend_class_of == self_class_of:
    print('"Oh, berarti kita angkatannya sama dong!"')
elif self_class_of < friend_class_of:
    print(
        f'"Oh, berarti aku panggilnya ko/ci {self_name} dong! Tapi ga usah lah ya, biar ga aneh gitu ehe"'
    )
else:
    print(f'"Oh, berarti aku panggil kamu dek {self_name} dong!"')

# Prints values stored in variables referring to friends
print(
    f'"Halo {self_name.title()}! Namaku {friend_name}, lahir pada {friend_date_of_birth}, dari jurusan {major}"'
)

# Prints values stored in variables referring to the user
print(
    f'"Jadi aku rekap lagi nih, nama kamu {self_name} dari {self_major} angkatan {self_class_of} ya? Salam kenal!"'
)

# Prints closing text
print("Tanpa alasan jelas, kamu membuat teman baru pada hari itu...")

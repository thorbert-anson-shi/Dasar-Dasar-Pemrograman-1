# Meminta input pesan dan 2 angka untuk password
msg = input("Pesan dari kelompok Zog: ")
num1 = int(input("Angka 1: "))
num2 = int(input("Angka 2: "))

# Mengkonversikan variabel "msg" menjadi angka biner, lalu men-decode kode biner tersebut sesuai code ASCII.
# Setara dengan:
#      bytes_str = bytes.fromhex(msg)
#      ascii_str = bytes_str.decode("ASCII")
ascii_str = bytes.fromhex(msg).decode("ASCII")

# Meng-encode angka yang dimasukkan user menjadi password (masih dalam bentuk int agar dapat dikonversikan menjadi angka biner)
pword = num1 * num2 * 13

print("-----------------------------------------------")

# Formatting dan printing string sesuai dengan nilai variabel "ascii_str" dan "pword"
print(f"Hasil terjemahan pesan: {ascii_str}")

# Menggunakan function bin(x: int) -> str untuk mengkonversikan variabel "pword" menjadi string biner
print(f"Password: {bin(pword)}")
print(f'Pesan "{ascii_str}" telah diterima dengan password "{bin(pword)}"')

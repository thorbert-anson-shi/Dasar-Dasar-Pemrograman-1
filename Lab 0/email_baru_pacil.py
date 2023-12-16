# Prints out a header text to preface the program
print("Buat Email Baru Khusus Anak Pacil")

# Takes user input to use later in email creation
fname = input("Nama Depan: ")
nickname = input("Nama Panggilan: ")
date_of_birth = input("Tanggal Lahir: ")

# Prints out a welcome message, personalized with the "fname" variable
print("Halo " + fname + ", selamat datang di Fasilkom!")

# Prints out the user's email by concatenating the values from the "fname", "nickname", and "date_of_birth" variables
print("Email kamu adalah " + fname + nickname + date_of_birth + "@ui.ac.id")

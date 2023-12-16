# Initialize user balance outside main while loop
balance: float = 0
BOOKS_COST = {"X-Man": 7000, "Doraemoh": 5500, "Nartoh": 4000}

# Creates a list of the available books from the BOOKS_COST dictionary
catalogue = ""
for i in BOOKS_COST.items():
    catalogue += f"{i[0]} (Rp {i[1]:,}/hari)\n"

# Main program while loop
while True:
    print(
        """\
============================================
Selamat Datang di Toko Buku Place Anak Chill!
============================================
1. Pinjam Buku
2. Keluar
============================================
"""
    )
    # Amount the cost is multiplied by
    coefficient = 1

    # Ask for user action (borrow/exit)
    action = input("Apa yang ingin Anda lakukan: ")

    # If action is borrow, ask for membership status
    if action == "1":
        name = input("Masukkan nama Anda: ")

        balance = int(input("Saldo Anda sekarang (Rp): "))

        member = True if input("Apakah Anda member? [Y/N]: ") == "Y" else False

        if member:
            chances = 3
            # Asks for ID until user runs out of chances
            while chances > 0:
                id = input("Masukkan ID Membership Anda: ")
                # Check if ID is valid (length = 5 and sum of digits is 23)
                if len(id) == 5 and sum([int(num) for num in id]) == 23:
                    # Apply 20% discount (1 - 0.2 = 0.8)
                    coefficient = 0.8
                    print(
                        "Login member berhasil!\n==============================================\n"
                    )
                    break
                else:
                    chances -= 1
                    print("Member ID invalid!")
            else:
                print("Program akan kembali ke menu utama")
                continue
        # If not a member, continue program as usual
        else:
            print(
                "Login non-member berhasil!\n==============================================\n"
            )

        # Book borrowing subprogram
        while True:
            print(
                f"""\
============================================
Katalog Buku Place Anak Chill
============================================
{catalogue.strip()}
============================================
Exit
============================================\
"""
            )
            # Stores the user-chosen title
            # Converts user input into titlecase to make sure input is processed case-insensitively
            book_choice = input("Buku yang dipilih: ").title()

            # If user chooses from available books, ask for number of days book is to be borrowed for
            if book_choice in BOOKS_COST:
                days = int(input("Ingin melakukan peminjaman untuk berapa hari: "))
                # cost of borrowing = cost/day * no. of days * (1 - discount)
                cost = BOOKS_COST.get(book_choice) * days * coefficient
                # Check to see if balance is enough for purchase
                if balance >= cost:
                    balance -= cost
                    print(f"Berhasil meminjam buku {book_choice} selama {days} hari")
                    print(f"Saldo Anda saat ini: Rp{balance}\n")
                else:
                    # Prints out difference between book cost and user balance
                    print(
                        f"Tidak berhasil meminjam! Saldo anda kurang Rp{cost-balance}\n"
                    )
                    pass

            # If user exits, break out of book borrowing subprogram
            elif book_choice == "Exit":
                print()
                break

            # If book title is invalid, reprompt with book choice
            else:
                print(
                    "Komik tidak ditemukan. Masukkan kembali judul komik sesuai katalog!"
                )

    # If user chooses to exit program, break from while loop and print exit message
    elif action == "2":
        break
print("Terima kasih sudah berbelanja di Toko Buku Place Anak Chill!")

def main():
    """
    Declares database, then asks user for input and runs helper functions based on the chosen action
    """
    # Format of data = ["uname", [score1, score2, score3, etc.]]
    global db
    db = []
    while True:
        print(
            """Selamat datang di Database Nilai Dek Depe
1. Tambah data ke database
2. Baca data dari database
3. Update data di database
4. Hapus data dari database
5. Keluar"""
        )
        action = input("Masukkan kegiatan yang ingin dilakukan: ")
        if action == "1":
            add_score()
        elif action == "2":
            show_score()
        elif action == "3":
            update_score()
        elif action == "4":
            delete_score()
        elif action == "5":
            print("Terima kasih telah menggunakan database Dek Depe!")
            exit()


def add_score():
    """
    Add new user data to database in the specified format ([uname, [score1, score2, score3, etc.]])
    """
    uname = input("Masukkan nama: ")
    # Check if name is already in database
    for data in db:
        if uname.lower() == data[0].lower():
            print("Nama sudah di database!")
            return

    scores = []

    lab = 1
    while True:
        score = score_input(f"Masukkan nilai Lab {lab} (Ketik STOP untuk selesai): ")
        if score == "STOP":
            break
        else:
            scores.append(score)
        lab += 1
    db.append([uname, scores])
    print(f"Berhasil menambahkan {lab-1} nilai untuk {uname} ke database\n")


def show_score():
    """
    Show the specified score of the specified name
    """
    uname = input("Masukkan nama: ")
    # Check if entered name is already in database
    for i in range(len(db)):
        if db[i][0].lower() == uname.lower():
            # Locate the index of name in the database and the number of scores said name has
            uname_idx = i
            max = len(db[i][1])
            break
    else:
        print("Nama tidak ada dalam database!")
        return

    while True:
        try:
            lab_idx = int(input("Masukkan nilai Lab ke berapa yang ingin dilihat: "))
        except ValueError:
            print("Masukkan index lab dalam bentuk bilangan bulat!")
            continue
        # Validate the index of chosen score to be greater than 0 and to be smaller than the number of scores the name has
        if lab_idx <= max:
            score_at_idx = db[uname_idx][1][lab_idx - 1]
            # Check if the score at the particular index exists
            if score_at_idx == -1:
                print(f"Nilai untuk Lab {lab_idx} tidak ada!")
            else:
                print(
                    f"Nilai {db[uname_idx][0]} untuk Lab {lab_idx} adalah {score_at_idx}"
                )
        elif lab_idx < 0:
            print(f"Masukkan index Lab lebih dari atau sama dengan 1")
        else:
            print(f"Tidak terdapat nilai untuk Lab {lab_idx}")
        print()
        break


def update_score():
    """
    Change a specified name's score for a specified Lab assignment and reflect the change in db
    """
    uname = input("Masukkan nama: ")
    # Data existence check
    for i in range(len(db)):
        if db[i][0].lower() == uname.lower():
            uname_idx = i
            max = len(db[i][1])
            break
    else:
        print("Nama tidak ada dalam database!")
        return

    while True:
        try:
            lab_idx = int(input("Masukkan nilai Lab ke berapa yang ingin diubah: "))
        except ValueError:
            print("Masukkan index lab dalam bentuk bilangan bulat!")
            continue
        # Index validation
        if lab_idx <= max:
            new_score = score_input(f"Masukkan nilai baru untuk Lab {lab_idx}: ")
            old_score = db[uname_idx][1][lab_idx - 1]
            db[uname_idx][1][lab_idx - 1] = new_score
            print(
                f"Berhasil mengupdate nilai Lab {lab_idx} {db[uname_idx][0]} dari {old_score} ke {new_score}"
            )
        elif lab_idx < 0:
            print(f"Masukkan index Lab lebih dari atau sama dengan 1")
        else:
            print(f"Tidak terdapat nilai untuk Lab {lab_idx}")
        print()
        break


def delete_score():
    """
    Delete the specified name's specified score by changing the specified score to -1,
    as it is a special value that the user can't simply enter
    """
    uname = input("Masukkan nama: ")
    # Data existence check
    for i in range(len(db)):
        if db[i][0].lower() == uname.lower():
            uname_idx = i
            max = len(db[i][1])
            break
    else:
        print("Nama tidak ada dalam database!")
        return

    while True:
        try:
            lab_idx = int(input("Masukkan nilai Lab ke berapa yang ingin dihapus: "))
        except ValueError:
            print("Masukkan index lab dalam bentuk bilangan bulat!")
            continue
        # Index validation
        if lab_idx <= max:
            db[uname_idx][1][lab_idx - 1] = -1
            print(
                f"Berhasil menghapus nilai Lab {lab_idx} {db[uname_idx][0]} dari database"
            )
        elif lab_idx < 0:
            print(f"Masukkan index Lab lebih dari atau sama dengan 1")
        else:
            print(f"Tidak terdapat nilai untuk Lab {lab_idx}")
        print()
        break


def score_input(prompt):
    """
    Validate user input when entering scores (max and min values, type validation)
    """
    max = 100
    min = 0
    while True:
        # Special condition for add_score() function
        score = input(prompt)
        if score.upper() == "STOP":
            return "STOP"

        try:
            score = float(score)
        except ValueError:
            print("Masukkan nilai dalam bentuk bilangan riil!")
            continue
        if min <= score <= max:
            return score
        else:
            print("Nilai harus berada dalam range 0-100")


if __name__ == "__main__":
    main()

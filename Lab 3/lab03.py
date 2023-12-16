"""
The program relies heavily on the use of .find() to iterate
through all items in a string separated by commas. After each iteration,
an item separated by commas is yielded which can be used in expressions.
"""


def main():
    # Asks for input file and makes sure it exists
    print(
        "Selamat datang! Masukkan dua nama file yang berisi daftar makanan yang kamu miliki."
    )
    while True:
        try:
            my_file = open(input("Masukkan nama file input daftar makanan: "), "r")
            break
        except FileNotFoundError:
            print("Maaf, file input tidak ada")
            continue

    output_file_name = input("Masukkan nama file output: ")
    output_file = open(output_file_name, "a")  # Open output file for appending

    contents = (
        my_file.read()
    )  # Converts file into string; will print file metadata otherwise

    # Splits and stores the 2 lines in file into 2 separate strings
    newline_idx = contents.find("\n")
    line_1 = contents[contents.find(":") + 1 : newline_idx].strip().lower() + ","
    line_2 = contents[newline_idx + 1 :][contents.find(":") + 1 :].strip().lower() + ","

    while True:
        print(
            """Apa yang ingin kamu lakukan?
================================================
1. Tampilkan daftar makanan pertama
2. Tampilkan daftar makanan kedua
3. Tampilkan gabungan makanan dari dua daftar
4. Tampilkan makanan yang sama dari dua daftar
5. Keluar
================================================
"""
        )

        action = input("Masukkan aksi yang ingin dilakukan: ")
        print()
        if action == "1":
            print(f"Daftar makanan pertama:\n{show_list(line_1)}\n", file=output_file)
            print(f"Daftar makanan pertama:\n{show_list(line_1)}\n")
        elif action == "2":
            print(f"Daftar makanan kedua:\n{show_list(line_2)}\n", file=output_file)
            print(f"Daftar makanan kedua:\n{show_list(line_2)}\n")
        elif action == "3":
            print(
                f"Makanan yang sama dari dua daftar:\n{intersect(line_1, line_2)}\n",
                file=output_file,
            )
            print(f"Makanan yang sama dari dua daftar:\n{intersect(line_1, line_2)}\n")
        elif action == "4":
            print(
                f"Gabungan makanan dari kedua daftar:\n{union(line_1, line_2)}\n",
                file=output_file,
            )
            print(f"Gabungan makanan dari kedua daftar:\n{union(line_1, line_2)}\n")
        elif action == "5":
            output_file.close()
            print(
                f"Terima kasih sudah menggunakan program ini! Semua output akan dicatat pada {output_file_name}"
            )
            break
        else:
            print("Perintah tidak terdefinisi. Pilih angka dari 1-5")


def show_list(string):
    out_string = ""
    comma_idx = next_comma_idx = 0
    while next_comma_idx != -1:
        # From previous loop, set the previous loop's next comma index as the current loop's comma index
        comma_idx = next_comma_idx
        # Finds next comma index after first comma
        next_comma_idx = string.find(",", comma_idx + 1)
        # Slices string between commas, yielding the current chosen item
        chosen_item = string[comma_idx:next_comma_idx].strip(", ")
        # Make sure there are no duplicate items
        if chosen_item not in out_string:
            out_string += chosen_item + ","
    return out_string.strip(",")


def intersect(string1: str, string2: str):
    """
    Add items to output string if they exist in both string1 and string2
    """
    out_string = ""
    comma_idx = next_comma_idx = 0
    while next_comma_idx != -1:
        comma_idx = next_comma_idx
        next_comma_idx = string1.find(",", comma_idx + 1)
        chosen_item = string1[comma_idx:next_comma_idx].strip(", ")
        if next_comma_idx == -1:
            break
        # If an item in string1 is not in string2, there is no need to check the other way around
        if chosen_item in string2 and chosen_item not in out_string:
            out_string += chosen_item + ","
    return out_string.strip(",")


def union(string1: str, string2: str):
    """
    Add items to output_string as long as it is unique
    """
    out_string = ""
    comma_idx = next_comma_idx = 0
    while next_comma_idx != -1:
        comma_idx = next_comma_idx
        next_comma_idx = string1.find(",", comma_idx + 1)
        chosen_item = string1[comma_idx:next_comma_idx].strip(", ")
        if chosen_item in out_string:
            pass
        else:
            out_string += chosen_item + ","

    comma_idx = next_comma_idx = 0
    while next_comma_idx != -1:
        comma_idx = next_comma_idx
        next_comma_idx = string2.find(",", comma_idx + 1)
        chosen_item = string2[comma_idx:next_comma_idx].strip(", ")

        # Prevent duplicate items in output
        if chosen_item in out_string:
            pass
        else:
            out_string += chosen_item + ","

    return out_string.strip(",")


if __name__ == "__main__":
    main()

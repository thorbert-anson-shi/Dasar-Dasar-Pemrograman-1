import sys


def print_headers():
    print(
        "| {: <2} | {: <25} | {: <8} | {: <10} | {: <3}|".format(
            "No", "Smartphone", "Price", "Screensize", "RAM"
        )
    )
    print("================================================================")


def print_table(filename):
    """Prints out the entire file's contents, formatted into a table"""
    with open(filename, "r") as f:
        print_headers()
        rows = f.readlines()
        idx = 0
        # For each row of the table
        for i in range(len(rows)):
            idx += 1
            # Split each value and store it in an array
            data = rows[i].split("\t")
            # Strip any leading or trailing characters for each value
            for j in range(len(data)):
                data[j] = data[j].strip()
            # Print out a formatted string based on the contents of the list
            print(
                "| {: <2} | {: <25} | {: <8} | {: <10} | {: <3}|".format(
                    idx,
                    data[0],
                    data[1],
                    data[2],
                    data[3],
                )
            )


def search_phone(filename, keyword):
    """Searches for a specific substring in the data table"""
    with open(filename, "r") as f:
        print_headers()
        rows = f.readlines()
        # Keep track of how many matches we've found
        idx = 0
        for i in range(len(rows)):
            data = rows[i].split("\t")
            for j in range(len(data)):
                data[j] = data[j].strip()
            # Lowercase keyword and data to make sure program is case insensitive
            if keyword.lower() in data[0].lower():
                idx += 1
                print(
                    "| {: <2} | {: <25} | {: <8} | {: <10} | {: <3}|".format(
                        idx,
                        data[0],
                        data[1],
                        data[2],
                        data[3],
                    )
                )

    print(f"Ukuran data dari hasil pencarian: {idx} x 4")


def desc_stat(filename, col):
    """Retrieves data from a specific column in a file and prints out the min, max, and average values of said column"""
    with open(filename, "r") as file_obj:
        ds = []
        rows = file_obj.readlines()
        for i in range(len(rows)):
            data = rows[i].split("\t")
            try:
                ds.append(float(data[col]))
            except IndexError:  # Catches error if sys.argv[3] is out of range
                print("\nPencarian gagal! Index kolom harus dalam range 1-3!")
                exit()
            except ValueError:  # Catches error if sys.argv[3] is 0.
                print("\nPencarian gagal! Index kolom tidak bisa bernilai 0!")
                exit()

    print(f"Min data: {min(ds)}")
    print(f"Max data: {max(ds)}")
    print(f"Rata-rata: {sum(ds)/len(ds)}")


if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python script_name.py <file_path> <search_keyword> <column_num>")
        sys.exit(1)
    file_path = sys.argv[1]
    key = sys.argv[2]
    column_num = int(sys.argv[3])

    try:
        print_table(file_path)
        print()
        search_phone(file_path, key)
        desc_stat(file_path, column_num)
    except FileNotFoundError:  # Catch FNF errors from calling open() within functions
        print("Maaf, file input tidak ada")

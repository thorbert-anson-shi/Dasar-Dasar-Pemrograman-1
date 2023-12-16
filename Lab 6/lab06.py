def convert_to_dict(filename, encoding):
    """
    Converts file contents into a dict of subjects, whose values are dicts
    of names whose values are the keywords of each person for the specified subject
    """
    try:
        with open(filename, "r", encoding=encoding) as fileobj:
            lines = fileobj.readlines()  # Converts file contents a list of lines
    except FileNotFoundError:
        print("File tidak ditemukan!")
        exit(code=404)

    subj_to_person = {}  # Create a dictionary that maps a subject to people

    for line_idx in range(len(lines)):
        line_content = lines[line_idx]
        if line_content[0] == "=":
            # If a line whose first character is "=", we know that the line above and below
            # contain the biodata and the assignment content, respectively
            biodata_line = lines[line_idx - 1].strip(
                ""
            )  # Weird multibyte string detected?
            keywords_line = lines[line_idx + 1].strip()

            biodata: list = biodata_line.strip().split(";")
            keywords: list = keywords_line.split(" ")

            # Create a dict mapping each person's name and NPM to their assignment's content
            dict_entry: dict = {
                # Create two keys so both NPM and name can be used for searching
                biodata[0]: set(keywords),
                biodata[1]: set(keywords),
            }

            subject = biodata[2].strip()
            if subject in subj_to_person:
                subj_to_person[subject].update(dict_entry)
            else:
                subj_to_person[subject] = dict_entry

    return subj_to_person


def get_similarity(s1: set, s2: set):
    return len(s1 & s2) / len(s1)


def print_status(p1: str, p2: str, f: float):
    """
    Prints the assignment's plagiarism status based on the percentage similarity
    """
    if f >= 71:
        print(f"{p1} dan {p2} terindikasi plagiarisme.")
    elif f >= 31:
        print(f"{p1} dan {p2} terindikasi plagiarisme ringan.")
    else:
        print(f"{p1} dan {p2} tidak terindikasi plagiarisme.")
    print(f"\n{56 * '='}")


def main():
    """
    Converts file contents into a dict, searches for each person's keyword set
    based on their name, and then returns the percentage similarity of both sets
    """
    subj_to_person = convert_to_dict("Lab6.txt", "utf-8-sig")
    print("Selamat datang di program Plagiarism Checker!")
    print(f"{'=' * 56}")

    while True:
        subject = input("Masukkan nama mata kuliah yang ingin diperiksa: ")
        if subject in subj_to_person:
            person1 = input("Masukkan nama/NPM mahasiswa pertama: ")
            if person1 not in subj_to_person[subject]:
                print("Informasi mahasiswa tidak ditemukan.")
                print(f"\n{'=' * 56}")
                continue
            person2 = input("Masukkan nama/NPM mahasiswa kedua: ")
            if person2 not in subj_to_person[subject]:
                print("Informasi mahasiswa tidak ditemukan.")
                print(f"\n{'=' * 56}")
                continue

            # Gets dict of names and their keywords based on the chosen subject
            assignments = subj_to_person[subject]
            percentage = (
                get_similarity(assignments[person1], assignments[person2]) * 100
            )

            print(
                f"Tingkat kemiripan tugas {subject} {person1} dan {person2} adalah {percentage:.2f}%"
            )
            print_status(person1, person2, percentage)
        elif subject == "EXIT":
            print("Terima kasih telah menggunakan program Plagiarism Checker!")
            exit()
        else:
            print(f"{subject} tidak ditemukan!")
            print(f"\n{'=' * 56}")
            continue


if __name__ == "__main__":
    main()

import os, sys, time


SECTION_NAMES = [
    "kepala_putusan",
    "identitas",
    "riwayat_penahanan",
    "riwayat_perkara",
    "riwayat_tuntutan",
    "riwayat_dakwaan",
    "fakta",
    "fakta_hukum",
    "pertimbangan_hukum",
    "amar_putusan",
    "penutup",
]


path = "indo-law-main/dataset"


def main() -> int:
    """Runs the search algorithm and helper functions"""
    start = time.time()

    # There are only 2 possible valid command line argument lengths, so if-else is viable
    if len(sys.argv) == 3:
        keyphrase = sys.argv[2].lower()
    elif len(sys.argv) == 5:
        keyword1 = sys.argv[2].lower()
        operator = sys.argv[3].upper()  # Make input case insensitive
        keyword2 = sys.argv[4].lower()
        keyphrase = f"{keyword1} {operator} {keyword2}"
    else:
        print("Argumen program tidak benar")
        # Exit program without error message
        return -1

    sec = sys.argv[1].lower()

    if sec == "all":
        print(f"Searching all files for {keyphrase}...")
        section = "all"
    elif sec in SECTION_NAMES:
        print(f"Searching through <{sec}> for {keyphrase}...")
        section = sec
    else:
        print("Section tidak ditemukan! Pastikan pengejaan section benar!")
        [print(i) for i in SECTION_NAMES]
        # Exit program without error message
        return -1

    # Keep track of total file count
    count = 0

    # Initialize an empty array to keep names of all found files
    result = []

    # Create a list of all file names in folder to iterate through
    folder = os.listdir(path)
    file_count = len(folder)

    for file in folder:
        # Open each file and read its contents
        with open(f"{path}/{file}") as file_obj:
            # Replace \n with whitespace for cases of inconsistent file formatting
            content = file_obj.read().replace("\n", " ")
            content_cut = get_section(content, section)

            # Divide cases based on number of keywords
            if len(sys.argv) == 3:
                if keyphrase in content_cut:
                    a = get_case_info(content)
                    result.append(f"|{file}|{a}|")
                count += 1

            elif len(sys.argv) == 5:
                if operator == "AND":
                    if keyword1 in content_cut and keyword2 in content_cut:
                        a = get_case_info(content)
                        result.append(f"|{file}|{a}|")
                    count += 1

                elif operator == "OR":
                    if keyword1 in content_cut or keyword2 in content_cut:
                        a = get_case_info(content)
                        result.append(f"|{file}|{a}|")
                    count += 1

                elif operator == "ANDNOT":
                    if keyword1 in content_cut and keyword2 not in content_cut:
                        a = get_case_info(content)
                        result.append(f"|{file}|{a}|")
                    count += 1

                else:
                    print("Operator harus berupa AND, OR atau ANDNOT")
                    return -1
        # Simple progress indicator
        print(
            f"\rProgress : {count} files out of a total of {file_count} files", end=""
        )
    end = time.time()

    print(f"\n{str():=^122}")

    for _ in result:
        print(_)

    print(f"{str():=^122}\n")

    print(f"{len(result)} files found with the keywords: {keyphrase}")
    print(f"{count} files scanned in {end-start:.5f} seconds\n")

    return 0


def get_section(file: str, section_name: str) -> str:
    """This function returns the contents within a specified section of the file as a string"""
    if section_name == "all":
        return file
    else:
        try:
            section_start = file.index(f"<{section_name}>")
            section_end = file.index(f"</{section_name}>")
            # Uses string slicing to extract string between opening and closing tags
            return file[section_start : section_end + 1]
        except ValueError:
            return ""


def get_case_info(string: str) -> str:
    """This function looks inside the <putusan> tag and searches for values of the listed fields, then returns a formatted string of said values"""
    data = string[string.find("<putusan") : string.find(">")]

    field_string = ["provinsi", "klasifikasi", "sub_klasifikasi", "lembaga_peradilan"]

    out = []
    # Iterate through the list values and check for the values within the quotation marks ("")
    for val in field_string:
        start_index = data.find(f'{val}="') + len(f'{val}="')
        end_index = data.find('"', start_index)
        out.append(data[start_index:end_index])

    return f"{out[0]:>15.15s}|{out[1]:>15.15s}|{out[2]:>30.30s}|{out[3]:>20.20s}"


if __name__ == "__main__":
    main()

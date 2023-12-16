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

    if len(sys.argv) == 3:
        for file in folder:
            with open(f"{path}/{file}") as file_obj:
                # Replace newline characters with whitespace for consistency between files (Credit: Yudayana Arif)
                content = file_obj.read().replace("\n", " ")
                content_cut = get_section(content, section)
                if keyphrase in content_cut:
                    a = get_case_info(content)
                    result.append(f"|{file}|{a}")
                count += 1
                print(
                    f"\rProgress : {count} files out of a total of 22630 files", end=""
                )

    elif len(sys.argv) == 5:
        if operator == "AND":
            for file in folder:
                with open(f"{path}/{file}") as file_obj:
                    content = file_obj.read().replace("\n", " ")
                    content_cut = get_section(content, section)
                    if keyword1 in content_cut and keyword2 in content_cut:
                        a = get_case_info(content)
                        result.append(f"|{file}|{a}")
                    count += 1
                    print(
                        f"\rProgress : {count} files out of a total of 22630 files",
                        end="",
                    )

        elif operator == "OR":
            for file in folder:
                with open(f"{path}/{file}") as file_obj:
                    content = file_obj.read().replace("\n", " ")
                    content_cut = get_section(content, section)
                    if keyword1 in content_cut or keyword2 in content_cut:
                        a = get_case_info(content)
                        result.append(f"|{file}|{a}")
                    count += 1
                    print(
                        f"\rProgress : {count} files out of a total of 22630 files",
                        end="",
                    )

        elif operator == "ANDNOT":
            for file in folder:
                with open(f"{path}/{file}") as file_obj:
                    content = file_obj.read().replace("\n", " ")
                    content_cut = get_section(content, section)
                    if keyword1 in content_cut and keyword2 not in content_cut:
                        a = get_case_info(content)
                        result.append(f"|{file}|{a}")
                    count += 1
                    print(
                        f"\rProgress : {count} files out of a total of 22630 files",
                        end="",
                    )
        else:
            print("Operator harus berupa AND, OR atau ANDNOT")
            return -1

    print(f"\n{str():=^122}")

    end = time.time()

    for _ in result:
        print(_)
    print(f"{str():=^122}\n")

    print(f"{len(result)} files found with the keywords: {keyphrase}")
    print(f"{count} files scanned in {end-start:.5f} seconds\n")

    return 0


def get_section(file: str, section_name: str) -> str:
    if section_name == "all":
        return file
    else:
        try:
            section_start = file.rindex(f"<{section_name}>")
            section_end = file.index(f"</{section_name}>")
            return file[section_start : section_end + 1]
        except ValueError:
            return ""


def get_case_info(string: str) -> str:
    data = string[string.rfind("<putusan") : string.find(">")]
    fields_string = {
        1: "provinsi",
        2: "klasifikasi",
        3: "sub_klasifikasi",
        4: "lembaga_peradilan",
    }

    out = []
    for key in fields_string.keys():
        start_index = data.find(f'{fields_string[key]}="') + len(
            f'{fields_string[key]}="'
        )
        end_index = data.find('"', start_index)
        out.append(data[start_index:end_index])

    return f"{out[0]:>15.15s}|{out[1]:>15.15s}|{out[2]:>30.30s}|{out[3]:>20.20s}|"


if __name__ == "__main__":
    main()

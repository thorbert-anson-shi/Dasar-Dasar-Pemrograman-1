import os
import sys
import time


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

folder = os.listdir("indo-law-main/dataset")


def main():
    start = time.time()
    if len(sys.argv) == 3:
        keyword = sys.argv[2]
    elif len(sys.argv) == 5:
        keyword1 = sys.argv[2]
        operator = sys.argv[3]
        keyword2 = sys.argv[4]

    if sys.argv[1] == "all":
        print("sift through all files")
        section = "all"
    elif sys.argv[1] in SECTION_NAMES:
        print("sift through certain sections")
        section = sys.argv[1]
    else:
        print(section)
        exit()

    count = 0
    result = []
    for file in folder:
        file_obj = open(f"indo-law-main/dataset/{file}", "r")
        content = get_section(file_obj.read(), section)

        if len(sys.argv) == 3:
            if keyword in content:
                result.append(file)
            count += 1

        elif len(sys.argv) == 5:
            if operator == "AND":
                if keyword1 in content and keyword2 in content:
                    result.append(file)
            elif operator == "OR":
                if keyword1 in content or keyword2 in content:
                    result.append(file)
            elif operator == "ANDNOT":
                if keyword1 in content and keyword2 not in content:
                    result.append(file)
            count += 1

        file_obj.close()

        print(f"\rProgress : {count} files out of a total of 22630 files", end="")
    print()
    for _ in result:
        print(_)
    end = time.time()
    print(f"\r{count} files scanned in {end-start:.5f} seconds")


def get_section(file: str, section_name: str):
    if section_name == "all":
        return file
    else:
        try:
            section_start = file.rindex(f"<{section_name}>")
            section_end = file.index(f"</{section_name}>")
            return file[section_start : section_end + 1]
        except ValueError:
            return ""


if __name__ == "__main__":
    main()

import matplotlib.pyplot as plt

# Libraries for additional functions, can be discarded for core functionality
import numpy as np
from scipy.stats import gaussian_kde


def get_type(a_str: str) -> str:
    try:
        int(a_str)
        return "int"
    except:
        try:
            float(a_str)
            return "float"
        except:
            return "str"


def read_csv(file_name: str, delimiter: str = ",") -> tuple:
    """
    Dataframe adalah sebuah abstraksi tabel data siap
    proses yang dalam tugas kali ini direpresentasikan
    sebagai 3-tuple:

    (data, list nama kolom, list tipe data)

    'data' merupakan list of lists yang menyimpan
    nilai-nilai pada tabel dan mempunyai format:

    [[row_11, row_12, ..., row_1n],
    [row_21, row_22, ..., row_2n],
    ...
    [row_m1, row_m2, ..., row_mn]]

    Satu cell row_mn dapat bertipe string, integer,
    atau float. Jika semua cell pada kolom n berisi
    literal integer, maka ubah semuanya dalam tipe
    data integer; jika bukan integer, maka ada dua kemungkinan,
    yaitu float atau string; jika semua nilai pada
    kolom n berupa number dan ada satu yang float, maka
    jadikan semua tipe data pada kolom n tersebut sebagai
    float; jika cell-cell pada kolom n ada yang tidak
    bisa dikonversikan ke integer maupun float, maka
    tipe kolom n tersebut adalah string.

    Selain list of lists yang berisi tabel, informasi
    nama kolom juga disimpan dalam bentuk
    'list nama kolom':

    [nama_kolom_1, nama_kolom_2, ..., nama_kolom_n]

    Elemen ketiga pada 3-tuple adalah 'list tipe data'
    pada setiap kolom. Ada tiga jenis tipe data dalam
    tugas kali ini = "str", "int", dan "float". Sebuah
    kolom bertipe "int" jika semua elemen pada kolom
    tersebut adalah literal integer; "float" jika semua
    elemen pada kolom adalah literal float (dan bukan
    literal integer); "str" jika selain kedua di atas.

    Fungsi ini bertugas untuk membaca sebuah file comma
    separated value, melakukan parsing, dan mengembalikan
    dataframe yang berupa 3-tuple.

    ASUMSI file csv:
    1. selalu ada header (nama kolom) pada baris pertama
    2. nama kolom yang diberikan sudah dijamin unik

    Daftar Exceptions:
    1. jika ada baris dengan jumlah kolom berbeda dari
        sebelumnya

        raise Exception(f"Banyaknya kolom pada baris {x} tidak konsisten.")

        dengan x adalah nomor baris (1-based) yang kolomnya
        berlebih pertama kali.

    2. jika tabel kosong,

            raise Exception("Tabel tidak boleh kosong.")

    parameter:
    file_name (string): nama file comma separated value
    delimiter (string): karakter pemisah antar kolom pada
                        suatu baris.

    return (list, list, list): (data, list nama kolom, list tipe data)
    """
    try:
        with open(file_name, "r") as fileobj:
            file_contents = fileobj.readlines()
    except FileNotFoundError:
        print("File tidak ditemukan!")

    dlim = delimiter

    # Empty list to hold lists of data per row
    data = []

    # Appends data per row to data list
    for line in file_contents:
        data.append(line.strip("\n").split(dlim))

    # Assumes first row is header column, removes it from data list
    col_names = data.pop(0)

    col_num = len(col_names)

    # Check for inconsistent column number per row
    for row in data:
        if len(row) != col_num:
            raise Exception(
                f"Banyaknya kolom pada baris {data.index(row) + 1} tidak konsisten."
            )

    if data == []:
        raise Exception("Tabel tidak boleh kosong!")

    # Creates a col first, row second structure
    data_per_col = []

    # Instantiates an empty list for each column
    for _ in col_names:
        data_per_col.append([])

    # Appends data for each row for each column
    for col_idx in range(col_num):
        for row_idx in range(len(data)):
            data_per_col[col_idx].append(data[row_idx][col_idx])

    col_dtypes = []

    for col in data_per_col:
        col_idx = data_per_col.index(col)

        # If the conditionals don't detect str or float, the col must contain ints
        col_type = "int"

        for item in col:
            # Check data type of each item
            if get_type(item) == "str":
                curr_type = "str"
            elif get_type(item) == "float":
                curr_type = "float"
            elif get_type(item) == "int":
                curr_type = "int"

            # Runs based on priority hierarchy of str -> float -> int
            if curr_type == "str":
                col_type = "str"
                break
            if curr_type == "float" and col_type == "int":
                col_type = "float"
        
        # Converts each "cell" into their respective types
        # If str, don't have to change anything as raw data is str
        if col_type == "float":
            for row_idx in range(len(data)):
                data[row_idx][col_idx] = float(data[row_idx][col_idx])
        elif col_type == "int":
            for row_idx in range(len(data)):
                data[row_idx][col_idx] = int(data[row_idx][col_idx])
        
        col_dtypes.append(col_type)

    return data, col_names, col_dtypes


def to_list(dataframe: tuple) -> list:
    return dataframe[0]


def get_column_names(dataframe: tuple) -> list:
    return dataframe[1]


def get_column_types(dataframe: tuple) -> list:
    return dataframe[2]


def head(dataframe: tuple, top_n: int = 10) -> str:
    """

    -- DIBUKA KE PESERTA --

    top_n baris pertama pada tabel!

    Mengembalikan string yang merupakan representasi tabel
    (top_n baris pertama) dengan format:

     kolom_1|     kolom_2|     kolom_3|     ...
    -------------------------------------------
    value_11|    value_12|    value_13|     ...
    value_21|    value_22|    value_23|     ...
    ...         ...         ...

    Space setiap kolom dibatasi hanya 15 karakter dan right-justified.

    parameter:
    dataframe (list, list, list): sebuah dataframe
    top_n (int): n, untuk penampilan top-n baris saja

    return (string): representasi string dari penampilan tabel.

    Jangan pakai print()! tetapi return string!
    """
    cols = get_column_names(dataframe)
    out_str = ""
    out_str += "|".join([f"{str(col):>15.15s}" for col in cols]) + "\n"
    out_str += ("-" * (15 * len(cols) + (len(cols) - 1))) + "\n"
    for row in to_list(dataframe)[:top_n]:
        out_str += "|".join([f"{str(col):>15.15s}" for col in row]) + "\n"
    return out_str


def info(dataframe: tuple) -> str:
    """
    Mengembalikan string yang merupakan representasi informasi
    dataframe dalam format:

    Total Baris = xxxxx baris

    Kolom          Tipe
    ------------------------------
    kolom_1        tipe_1
    kolom_2        tipe_2
    ...

    Space untuk kolom dan tipe adalah 15 karakter, left-justified

    parameter:
    dataframe (list, list, list): sebuah dataframe

    return (string): representasi string dari info dataframe
    """
    out = f"Total baris = {len(to_list(dataframe))} baris\n\n"
    header = f"{'Kolom':<15.15s}{'Tipe':<15.15s}\n{'-' * 30}"
    out += header
    # Iterate through column names and types at the same time to print each line
    for col_name, col_dtype in zip(
        get_column_names(dataframe), get_column_types(dataframe)
    ):
        out += "\n" + f"{col_name:<15.15s}{col_dtype:<15.15s}"
    return out


def satisfy_cond(value1, condition, value2) -> bool:
    """
    -- DIBUKA KE PESERTA --

    parameter:
    value1 (tipe apapun yang comparable): nilai pertama
    condition (string): salah satu dari ["<", "<=", "==", ">", ">=", "!="]
    value2 (tipe apapun yang comparable): nilai kedua

    return (boolean): hasil perbandingan value1 dan value2

    """
    try:
        if condition == "<":
            return value1 < value2
        elif condition == "<=":
            return value1 <= value2
        elif condition == ">":
            return value1 > value2
        elif condition == ">=":
            return value1 >= value2
        elif condition == "!=":
            return value1 != value2
        elif condition == "==":
            return value1 == value2
        else:
            raise Exception(f"Operator {condition} tidak dikenal")
    # Catch cases where boolean operators do not work
    except TypeError:
        raise Exception(
            f"Perbandingan antara tipe data {type(value1)} dan {type(value2)} tidak dapat dilakukan"
        )


def select_rows(dataframe: tuple, col_name: str, condition: str, value: str) -> tuple:
    """
    Mengembalikan dataframe baru dimana baris-baris sudah
    dipilih hanya yang nilai col_name memenuhi 'condition'
    terkait 'value' tertentu.

    Gunakan/Call fungsi satisfy_cond(value1, condition, value2) yang
    sudah didefinisikan sebelumnya!

    contoh:
      select_rows(dataframe, "umur", "<=", 50) akan mengembalikan
      dataframe baru dengan setiap baris memenuhi syarat merupakan
      item dengan kolom umur <= 50 tahun.

    Exceptions:
      1. jika col_name tidak ditemukan,

          raise Exception(f"Kolom {col_name} tidak ditemukan.")

      2. jika condition bukan salah satu dari ["<", "<=", "==", ">", ">=", "!="]

          raise Exception(f"Operator {condition} tidak dikenal.")

    parameter:
    dataframe (list, list, list): sebuah dataframe
    col_name (string): nama kolom sebagai basis untuk selection
    condition (string): salah satu dari ["<", "<=", "==", ">", ">=", "!="]
    value (tipe apapun): nilai untuk basis perbandingan pada col_name

    return (list, list, list): dataframe baru hasil selection atau filtering

    """
    data = to_list(dataframe)
    col_names = get_column_names(dataframe)
    col_types = get_column_types(dataframe)

    try:
        target_col = col_names.index(col_name)
    except ValueError:
        raise Exception(f"Kolom {target_col} tidak ditemukan.")

    if condition not in ["<", "<=", "==", ">", ">=", "!="]:
        raise Exception(f"Operator {condition} tidak dikenal.")

    filtered_data = []

    for row in data:
        # Only append row to new dataframe if condition is satisfied
        if satisfy_cond(row[target_col], condition, value):
            filtered_data.append(row)

    return filtered_data, col_names, col_types


def select_cols(dataframe: tuple, selected_cols: list) -> tuple:
    """
    Mengembalikan dataframe baru dimana kolom-kolom sudah
    dipilih hanya yang terdapat pada 'selected_cols' saja.

    contoh:
    select_cols(dataframe, ["umur", "nama"]) akan mengembalikan
    dataframe baru yang hanya terdiri dari kolom "umur" dan "nama".

    Exceptions:
      1. jika ada nama kolom pada selected_cols yang tidak
         ditemukan,

           raise Exception(f"Kolom {selected_col} tidak ditemukan.")

      2. jika select_cols adalah list kosong [],

           raise Exception("Parameter selected_cols tidak boleh kosong.")

    parameter:
    dataframe (list, list, list): sebuah dataframe
    selected_cols (list): list of strings, atau list yang berisi
                          daftar nama kolom

    return (list, list, list): dataframe baru hasil selection pada
                               kolom, yaitu hanya mengandung kolom-
                               kolom pada selected_cols saja.

    """
    if selected_cols == []:
        raise Exception(f"Parameter selected_cols tidak boleh kosong.")

    data = to_list(dataframe)
    col_names = get_column_names(dataframe)
    col_types = get_column_types(dataframe)

    # Store indices of target columns and their types
    target_col_idx = []
    target_col_types = []

    filtered_data = []

    # Find indices of selected col names
    for col in selected_cols:
        try:
            target_idx = col_names.index(col)
        except ValueError:
            raise Exception(f"Kolom {col} tidak ditemukan.")

        target_col_idx.append(target_idx)

    # Column names indices correspond to the data type list
    for col_idx in target_col_idx:
        target_col_types.append(col_types[col_idx])

    # Fetch the desired columns from each row of data
    for row_idx in range(len(data)):
        temp = []
        for col_idx in target_col_idx:
            temp.append(data[row_idx][col_idx])
        filtered_data.append(temp)

    return filtered_data, selected_cols, target_col_types


def count(dataframe: tuple, col_name: str) -> dict:
    """
    mengembalikan dictionary yang berisi frequency count dari
    setiap nilai unik pada kolom col_name.

    Tipe nilai pada col_name harus string !

    Exceptions:
      1. jika col_name tidak ditemukan,

           raise Exception(f"Kolom {col_name} tidak ditemukan.")

      2. jika tipe data col_name adalah numerik (int atau float),

           raise Exception(f"Kolom {col_name} harus bertipe string.")

      3. jika tabel kosong, alias banyaknya baris = 0,

           raise Exception("Tabel kosong.")

    Peserta bisa menggunakan Set untuk mengerjakan fungsi ini.

    parameter:
    dataframe (list, list, list): sebuah dataframe
    col_name (string): nama kolom yang ingin dihitung rataannya

    return (dict): dictionary yang berisi informasi frequency count
                   dari setiap nilai unik.
    """
    data = to_list(dataframe)
    col_names = get_column_names(dataframe)
    col_dtypes = get_column_types(dataframe)

    if col_name not in col_names:
        raise Exception(f"Kolom {col_name} tidak ditemukan")

    if col_dtypes[col_names.index(col_name)] != "str":
        raise Exception(f"Kolom {col_name} harus berupa string")

    if data == []:
        raise Exception("Tabel kosong")

    # Select col we want to count
    ls = to_list(select_cols(dataframe, [col_name]))

    final_dict = {}

    # Keep track of occurrence count using dictionary {key:count}
    for item in ls:
        if item[0] in final_dict:
            final_dict[item[0]] += 1
        else:
            final_dict[item[0]] = 1

    return final_dict


def mean_col(dataframe: tuple, col_name: str) -> float:
    """
    Mengembalikan nilai rata-rata nilai pada kolom 'col_name'
    di dataframe.

    Exceptions:
      1. jika col_name tidak ditemukan,

           raise Exception(f"Kolom {col_name} tidak ditemukan.")

      2. jika tipe data col_name adalah string,

           raise Exception(f"Kolom {col_name} bukan bertipe numerik.")

      3. jika tabel kosong, alias banyaknya baris = 0,

           raise Exception("Tabel kosong.")

    parameter:
    dataframe (list, list, list): sebuah dataframe
    col_name (string): nama kolom yang ingin dihitung rataannya

    return (float): nilai rataan
    """
    col_data = get_data_per_col(dataframe, col_name)

    return sum(col_data) / len(col_data)


def median_col(dataframe: tuple, col_name: str):
    col_data = get_data_per_col(dataframe, col_name)

    col_data.sort()

    # Take data point in the middle of sorted list
    if len(col_data) % 2:
        return col_data[int(len(col_data) / 2)]
    else:
        return (
            col_data[int(len(col_data) / 2)] + col_data[int(len(col_data) / 2 + 1)]
        ) / 2


def mode_col(dataframe:tuple, col_name:str) -> tuple:
    occurrences = count(dataframe, col_name)
    # Fetches the dictionary key with the largest value
    mode = max(occurrences)
    return mode, occurrences[mode]


def get_col_stddev(dataframe:tuple, col_name:str) -> float:
    """
    Returns how "spread out" the data in a column is.
    
    Uses the formula:\n

    std_dev = sqrt(sum((i-mu)^2)/N)\n

    where:\n
    i = individual data point\n
    mu = mean of column\n
    N = number of data points\n
    """
    col_data = get_data_per_col(dataframe, col_name)

    col_mean = sum(col_data) / len(col_data)

    temp_sum = 0

    for i in col_data:
        temp_sum += (i - col_mean)**2
    
    variance = temp_sum / len(col_data)

    return np.sqrt(variance)

def show_scatter_plot(x, y, x_label, y_label):
    """
    -- DIBUKA KE PESERTA --

    parameter:
    x (list): list of numerical values, tidak boleh string
    y (list): list of numerical values, tidak boleh string
    x_label (string): label pada sumbu x
    y_label (string): label pada sumbu y

    return None, namun fungsi ini akan menampilkan scatter
    plot dari nilai pada x dan y.

    Apa itu scatter plot?
    https://chartio.com/learn/charts/what-is-a-scatter-plot/
    """
    plt.scatter(x, y)
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.show()


def scatter(dataframe: tuple, col_name_x: str, col_name_y: str) -> None:
    """
    fungsi ini akan menampilkan scatter plot antara kolom col_name_x
    dan col_name_y pada dataframe.

    pastikan nilai-nilai pada col_name_x dan col_name_y adalah angka!

    Exceptions:
      1. jika col_name_x tidak ditemukan,

           raise Exception(f"Kolom {col_name_x} tidak ditemukan.")

      2. jika col_name_y tidak ditemukan,

           raise Exception(f"Kolom {col_name_y} tidak ditemukan.")

      3. jika col_name_x BUKAN numerical,

           raise Exception(f"Kolom {col_name_x} bukan bertipe numerik.")

      4. jika col_name_y BUKAN numerical,

           raise Exception(f"Kolom {col_name_y} bukan bertipe numerik.")

    parameter:
    dataframe (list, list, list): sebuah dataframe
    col_name_x (string): nama kolom yang nilai-nilainya diplot pada axis x
    col_name_y (string): nama kolom yang nilai-nilainya diplot pada axis y

    Call fungsi show_scatter_plot(x, y) ketika mendefinisikan fungsi
    ini!

    return None
    """
    x_col_data = get_data_per_col(dataframe, col_name_x)
    y_col_data = get_data_per_col(dataframe, col_name_y)

    show_scatter_plot(x_col_data, y_col_data, col_name_x, col_name_y)


def show_density_plot(dataframe: tuple, col_name: str, bw_method="scott") -> None:
    col_data = get_data_per_col(dataframe, col_name)

    # Plot a probability density graph by data per column
    density_function = gaussian_kde(col_data, bw_method=bw_method)
    x = np.linspace(min(col_data), max(col_data), int(len(col_data) / 10))

    plt.plot(x, density_function(x))
    plt.xlabel(col_name)
    plt.show()


def get_data_per_col(dataframe: tuple, col_name: str) -> list:
    # Fetch all necessary data for data validation
    data = to_list(dataframe)
    col_names = get_column_names(dataframe)
    col_dtypes = get_column_types(dataframe)

    if data == []:
        raise Exception("Tabel kosong")

    # Initialize empty column to store output
    col_data = []

    if col_name not in col_names:
        raise Exception(f"Kolom {col_name} tidak ditemukan")

    # Get index of column by column name
    col_idx = col_names.index(col_name)

    if col_dtypes[col_idx] == "str":
        raise Exception(f"Kolom {col_name} bukan bertipe numerik")

    # Append data for the desired column of each row to the output list
    for row in data:
        col_data.append(row[col_idx])

    return col_data


if __name__ == "__main__":
    # memuat dataframe dari tabel pada file abalone.csv
    dataframe = read_csv("abalone.csv")
    
    show_density_plot(dataframe, "Height")
    # cetak 10 baris pertama
    print(head(dataframe, top_n=10))

    # cetak informasi dataframe
    print(info(dataframe))

    # kembalikan dataframe baru, dengan kolom Length > 0.49
    new_dataframe = select_rows(dataframe, "Length", ">", 0.49)
    print(head(new_dataframe, top_n=5))

    # kembalikan dataframe baru, dimana Sex == "M" DAN Length > 0.49
    new_dataframe = select_rows(
        select_rows(dataframe, "Length", ">", 0.49), "Sex", "==", "M"
    )
    print(head(new_dataframe, top_n=5))

    # kembalikan dataframe baru yang hanya terdiri dari kolom Sex, Length, Diameter, dan Rings
    new_dataframe = select_cols(dataframe, ["Sex", "Length", "Diameter", "Rings"])
    print(head(new_dataframe, top_n=5))

    # hitung mean pada kolom Length (pada dataframe original)
    print(mean_col(dataframe, "Length"))

    # melihat unique values pada kolom Sex, dan frekuensi kemunculannya (pada dataframe original)
    print(count(dataframe, "Sex"))

    # tampilkan scatter plot antara kolom "Height" dan "Diameter"
    scatter(dataframe, "Length", "Diameter")

    print(mode_col(dataframe, "Sex"))

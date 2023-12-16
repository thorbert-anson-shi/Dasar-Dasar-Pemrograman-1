import matplotlib.pyplot as plt
from memory_profiler import profile
import re
import time


def get_type(a_str) -> str:
    try:
        int(a_str)
        return "int"
    except:
        try:
            float(a_str)
            return "float"
        except:
            return "str"


@profile
def read_csv(file_name, delimiter=",") -> tuple:
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

    # Assumes first row is header column
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

    data_per_col = []

    # Instantiates an empty list for data per column
    for _ in col_names:
        data_per_col.append([])

    # Appends data for the desired column per row
    for col_idx in range(col_num):
        for row_idx in range(len(data)):
            data_per_col[col_idx].append(data[row_idx][col_idx])

    col_dtypes = []

    for col in data_per_col:
        col_idx = data_per_col.index(col)
        col_type = "int"
        for item in col:
            if get_type(item) == "str":
                curr_type = "str"
            elif get_type(item) == "float":
                curr_type = "float"
            elif get_type(item) == "int":
                curr_type = "int"

            if curr_type == "str":
                col_type = "str"
                break
            if curr_type == "float" and col_type == "int":
                col_type = "float"
        
        if col_type == "float":
            for row_idx in range(len(data)):
                data[row_idx][col_idx] = float(data[row_idx][col_idx])
        elif col_type == "int":
            for row_idx in range(len(data)):
                data[row_idx][col_idx] = int(data[row_idx][col_idx])
        
        col_dtypes.append(col_type)
        s = dlim.join(col)

        # Determines column data type using regular expressions
        # Done for efficiency
        if re.search(f"[A-z]|[^\w\s{dlim}.]|(?:.?)-(?:.?)|[{dlim}.]{{2}}", s):
            col_dtypes.append("str")
        elif re.search(f"(?<={dlim}|\b)((-|)(\d+)\.(\d+))(?={dlim}|\b)", s):
            col_dtypes.append("float")
            for row_idx in range(len(data)):
                data[row_idx][col_idx] = float(data[row_idx][col_idx])
        else:
            col_dtypes.append("int")
            for row_idx in range(len(data)):
                data[row_idx][col_idx] = int(data[row_idx][col_idx])

    return data, col_names, col_dtypes


def to_list(dataframe) -> list:
    return dataframe[0]


def get_column_names(dataframe) -> list:
    return dataframe[1]


def get_column_types(dataframe) -> list:
    return dataframe[2]


def head(dataframe, top_n=10) -> str:
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


def info(dataframe) -> str:
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
    out = f"Total baris = {len(dataframe[0])} baris\n\n"
    header = "{:<15.15s}{:<15.15s}\n{}".format("Kolom", "Tipe", "-" * 30)
    out += header
    for col_name, col_dtype in zip(dataframe[1], dataframe[2]):
        out += "\n" + "{:<15.15s}{:<15.15s}".format(col_name, col_dtype)
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
        raise Exception(f"Operator {condition} tidak dikenal.")


def select_rows(dataframe, col_name, condition, value) -> tuple:
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
    # TODO: Implement
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
        if satisfy_cond(row[target_col], condition, value):
            filtered_data.append(row)

    return filtered_data, col_names, col_types


def select_cols(dataframe, selected_cols: list) -> tuple:
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
    # TODO: Implement
    if selected_cols == []:
        raise Exception(f"Parameter selected_cols tidak boleh kosong.")

    data = to_list(dataframe)
    col_names = get_column_names(dataframe)
    col_types = get_column_types(dataframe)

    target_col_idx = []
    target_col_types = []

    filtered_data = []

    for col in selected_cols:
        try:
            target_idx = col_names.index(col)
        except ValueError:
            raise Exception(f"Kolom {col} tidak ditemukan.")

        target_col_idx.append(target_idx)

    for col_idx in target_col_idx:
        target_col_types.append(col_types[col_idx])

    for row_idx in range(len(data)):
        temp = []
        for col_idx in target_col_idx:
            temp.append(data[row_idx][col_idx])
        filtered_data.append(temp)

    return filtered_data, selected_cols, target_col_types


def count(dataframe, col_name: str) -> dict:
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

    final_dict = {}

    ls = to_list(select_cols(dataframe, [col_name]))

    for item in ls:
        if item[0] in final_dict:
            final_dict[item[0]] += 1
        else:
            final_dict[item[0]] = 1

    return final_dict


def mean_col(dataframe, col_name) -> float:
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
    # TODO: Implement
    data = to_list(dataframe)
    col_names = get_column_names(dataframe)
    col_dtypes = get_column_types(dataframe)

    if col_name not in col_names:
        raise Exception(f"Kolom {col_name} tidak ditemukan")

    if col_dtypes[col_names.index(col_name)] == "str":
        raise Exception(f"Kolom {col_name} bukan bertipe numerik")

    if data == []:
        raise Exception("Tabel kosong")

    col_idx = col_names.index(col_name)

    col_data = []
    for row in data:
        col_data.append(row[col_idx])

    return sum(col_data) / len(col_data)


def show_scatter_plot(x, y, x_label, y_label, trend_line=False):
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

    z = np
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
    data = to_list(dataframe)
    col_names = get_column_names(dataframe)
    col_dtypes = get_column_types(dataframe)

    if col_name_x not in col_names:
        raise Exception(f"Kolom {col_name_x} tidak ditemukan.")
    elif col_name_y not in col_names:
        raise Exception(f"Kolom {col_name_y} tidak ditemukan.")

    x_col_idx = col_names.index(col_name_x)
    y_col_idx = col_names.index(col_name_y)

    if col_dtypes[x_col_idx] == "str":
        raise Exception(f"Kolom {col_name_x} bukan bertipe numerik.")
    elif col_dtypes[y_col_idx] == "str":
        raise Exception(f"Kolom {col_name_y} bukan bertipe numerik.")

    x_col = []
    y_col = []

    for row in data:
        x_col.append(row[x_col_idx])
        y_col.append(row[y_col_idx])

    show_scatter_plot(x_col, y_col, col_name_x, col_name_y)


if __name__ == "__main__":
    st = time.time()
    df = read_csv("abalone.csv")
    en = time.time()
    print(en - st)
    # print(get_column_types(df))
    # print(info(df))

    # print(to_list(select_cols(df, ["Height"])))

    # print(count(df, "Sex"))

    # new_dataframe = select_cols(df, ["Height", "Diameter"])
    # print(head(new_dataframe))
    # print(get_column_types(new_dataframe))

    # print(mean_col(df, "Diameter"))

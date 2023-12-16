import matplotlib.pyplot as plt

# Library lain untuk implementasi fungsi lain selain fungsionalitas utama
import numpy as np
import re

from scipy.stats import gaussian_kde

# Used for count() function
from collections import defaultdict, Counter


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
        # Joins contents of a column into a single, long string
        s = dlim.join(col)

        col_idx = data_per_col.index(col)

        # Determines column data type using regular expressions for efficiency with large datasets
        #              Letters and symbols |   Hyphen    | Repeating "," and "."
        if re.search(f"[A-z]|[^\w\s{dlim}.]|(?:.?)-(?:.?)|[{dlim}.]{{2}}", s):
            col_dtypes.append("str")
        elif re.search(f"(?<={dlim}|\b)(-?\d+\.\d+)(?={dlim}|\b)", s):
            col_dtypes.append("float")
            # Convert data per "cell" into float
            for row_idx in range(len(data)):
                data[row_idx][col_idx] = float(data[row_idx][col_idx])
        else:
            col_dtypes.append("int")
            # Convert data per "cell" into int
            for row_idx in range(len(data)):
                data[row_idx][col_idx] = int(data[row_idx][col_idx])

        # The brute force-y method of calling the get_type() function on each cell
        # is inefficient due to the high frequency of raising exceptions for cols
        # of floats and strs. 

        # After testing, the regex approach takes about 1/4th the time of the get_type() approach
        # and similar memory allocation.

        # for col in data_per_col:
        # col_idx = data_per_col.index(col)
        # col_type = "int"
        # for item in col:
        #     if get_type(item) == "str":
        #         curr_type = "str"
        #     elif get_type(item) == "float":
        #         curr_type = "float"
        #     elif get_type(item) == "int":
        #         curr_type = "int"

        #     if curr_type == "str":
        #         col_type = "str"
        #         break
        #     if curr_type == "float" and col_type == "int":
        #         col_type = "float"
        
        # if col_type == "float":
        #     for row_idx in range(len(data)):
        #         data[row_idx][col_idx] = float(data[row_idx][col_idx])
        # elif col_type == "int":
        #     for row_idx in range(len(data)):
        #         data[row_idx][col_idx] = int(data[row_idx][col_idx])
        
        # col_dtypes.append(col_type)

    return data, col_names, col_dtypes


def to_list(dataframe: tuple) -> list:
    return dataframe[0]


def get_column_names(dataframe: tuple) -> list:
    return dataframe[1]


def get_column_types(dataframe: tuple) -> list:
    return dataframe[2]


def head(dataframe: tuple, top_n: int = 10) -> str:
    cols = get_column_names(dataframe)
    out_str = ""
    out_str += "|".join([f"{str(col):>15.15s}" for col in cols]) + "\n"
    out_str += ("-" * (15 * len(cols) + (len(cols) - 1))) + "\n"
    for row in to_list(dataframe)[:top_n]:
        out_str += "|".join([f"{str(col):>15.15s}" for col in row]) + "\n"
    return out_str


def info(dataframe: tuple) -> str:
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
    if selected_cols == []:
        raise Exception(f"Parameter selected_cols tidak boleh kosong.")

    data = to_list(dataframe)
    col_names = get_column_names(dataframe)
    col_types = get_column_types(dataframe)

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
    data = to_list(dataframe)
    col_names = get_column_names(dataframe)
    col_dtypes = get_column_types(dataframe)

    if col_name not in col_names:
        raise Exception(f"Kolom {col_name} tidak ditemukan")

    if col_dtypes[col_names.index(col_name)] != "str":
        raise Exception(f"Kolom {col_name} harus berupa string")

    if data == []:
        raise Exception("Tabel kosong")

    # Use defaultdict for ease of handling new keys
    final_ddict = defaultdict(int)

    # Select col we want to count
    ls = to_list(select_cols(dataframe, [col_name]))

    for item in ls:
        final_ddict[item[0]] += 1

    # Minimal changes using a defaultdict tbh

    # for item in ls:
    #     if item[0] in final_dict:
    #         final_dict[item[0]] += 1
    #     else:
    #         final_dict[item[0]] = 1

    return dict(final_ddict)


def mean_col(dataframe: tuple, col_name: str) -> float:
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


def mode_col(dataframe:tuple, col_name:str):
    
    # This implementation was kind of unecessary
    data = to_list(dataframe)
    col_names = get_column_names(dataframe)
    col_dtypes = get_column_types(dataframe)

    if col_name not in col_names:
        raise Exception(f"Kolom {col_name} tidak ditemukan")

    col_idx = col_names.index(col_name)

    if col_dtypes[col_names.index(col_name)] != "str":
        raise Exception(f"Kolom {col_name} harus berupa string")

    if data == []:
        raise Exception("Tabel kosong")

    col_data = []
    
    for row in data:
        col_data.append(row[col_idx])

    return Counter(col_data).most_common(1)

    # This implementation is simple and efficient enough as is
    # occurrences = count(dataframe, col_name)
    # mode = max(occurrences)
    # return mode, occurrences[mode]


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

def show_scatter_plot(x, y, x_label, y_label, trend_line=False):
    plt.scatter(x, y)

    if trend_line:
        tl = np.polyfit(x, y, 1)
        tl_eq = np.poly1d(tl)
        plt.plot(x, tl_eq(x))
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.show()


def scatter(dataframe: tuple, col_name_x: str, col_name_y: str, trend_line:bool=False) -> None:
    x_col_data = get_data_per_col(dataframe, col_name_x)
    y_col_data = get_data_per_col(dataframe, col_name_y)

    show_scatter_plot(x_col_data, y_col_data, col_name_x, col_name_y, trend_line)


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
    scatter(select_rows(dataframe, "Height", "<", ), "Height", "Diameter", trend_line=True)

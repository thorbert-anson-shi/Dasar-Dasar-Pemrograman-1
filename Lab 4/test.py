file = "tc1.txt"
name = "Apple iPhone X"

with open(file, "r") as file_obj:
    rows = file_obj.readlines()
    for i in range(len(rows)):
        data = rows[i].split("\t")
        idx = 1
        if data[0] == name:
            print(
                "| {: <2} | {: <25} | {: <8} | {: <10} | {: <3}|".format(
                    idx, data[0], data[1], data[2], data[3]
                )
            )
            idx += 1

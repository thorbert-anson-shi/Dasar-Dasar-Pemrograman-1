# Binary to denary converter
def convert(bin_str:str) -> int:
    try:
        int(bin_str)
    except ValueError:
        raise Exception("You funny")

    illegal = [i for i in bin_str if i not in "01"]

    if illegal:
        raise Exception("Binary string should only consist of 0 and 1")

    den = 0

    for i, j in zip(bin_str[::-1], range(len(bin_str))):
        if int(i):
            den += 2**j
        else:
            pass

    return den
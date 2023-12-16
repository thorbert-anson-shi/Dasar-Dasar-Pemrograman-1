def main():
    _in = input("enter a decimal fraction: ")

    bin = []

    temp = float(_in)

    while are_not_equal(temp, 1.0):
        bin.append(str(temp)[0])
        if temp > 8.0:
            temp -= round(temp)

        temp *= 8
    else:
        n = ""
        for i in bin:
            n += bin[i]
        print(n.removeprefix("0"))


def are_not_equal(f1, f2):
    tlr = 1e-9
    return abs(f1 - f2) > tlr


main()

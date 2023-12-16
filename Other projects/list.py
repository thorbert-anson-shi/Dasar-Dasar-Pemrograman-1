A = "abracadabraa"
B = "alacazam"

A = set(A)
B = set(B)


def union():
    return A | B


def intersection():
    return A & B


def difference():
    return A - B


def symmetric_difference():
    return A ^ B


def issubset():
    return A <= B


print(union(), intersection(), difference(), symmetric_difference(), issubset())

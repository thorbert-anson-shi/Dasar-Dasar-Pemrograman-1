def list_length(lst: list) -> int:
    count = 1
    if lst == []:
        return 0
    else:
        count += list_length(lst[1:])
    return count

print(list_length([1,2,3,4,5,6]))

def sum_of_digits(i: int) -> int:
    if i // 10 == 0:
        return i % 10
    return i%10 + sum_of_digits(i//10)

print(sum_of_digits(53432))

def sum_of_digits_2(i: int) -> int:
    if str(i) == "":
        return 0
    return int(str(i)[0]) + sum_of_digits_2(int(str(i)[1:]))

print(sum_of_digits_2(54342))
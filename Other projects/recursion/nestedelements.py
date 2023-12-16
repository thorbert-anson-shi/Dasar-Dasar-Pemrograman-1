def nestedelements(lst: list) -> int:
    count = 0
    for ele in lst:
        if type(ele) == int:
            count += 1
        else:
            count += nestedelements(ele)
    return count

print(nestedelements([1,2,[1,2,3], 5, [1,1,1]]))
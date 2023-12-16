string1 = "among us"

ls = [ord(a) for a in string1]
print([chr(a - 32) for a in ls])

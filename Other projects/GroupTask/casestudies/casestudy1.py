string = input("Masukkan string: ")
new_str = ""
for char in string:
    if char.isupper():
        new_str + char.lower()
    else:
        new_str + char.upper()
print(new_str)

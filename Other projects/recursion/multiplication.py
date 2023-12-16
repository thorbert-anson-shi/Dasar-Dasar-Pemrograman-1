def multiply(a, b):
    if b == 0:
        return 0
    return a + multiply(a, b-1)

print(multiply(4200, 100))
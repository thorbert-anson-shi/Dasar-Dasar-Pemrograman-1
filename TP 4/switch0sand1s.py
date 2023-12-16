l_enc = {
    0: "0001101",
    1: "0011001",
    2: "0010011",
    3: "0111101",
    4: "0100011",
    5: "0110001",
    6: "0101111",
    7: "0111011",
    8: "0110111",
    9: "0001011",
}

r_enc = {}
g_enc = {}

for item in l_enc.items():
    r_enc[item[0]] = "".join("10"[int(i)] for i in item[1])
    g_enc[item[0]] = r_enc[item[0]][::-1]

print(l_enc)
print(r_enc)
print(g_enc)

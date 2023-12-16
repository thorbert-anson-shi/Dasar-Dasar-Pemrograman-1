# # import os
# # import time

# # folder = os.listdir("indo-law-main/dataset")

# # start = time.time()

# # for file in folder:
# #     with open(f"indo-law-main/dataset/{file}", "r") as f:
# #         f.read()
# #         print(file)

# # # for file in folder:
# # #     f = open(f"dataset/{file}", "r")
# # #     content = f.read()
# # #     f.close()
# # #     print(file)


# # end = time.time()

# # print(f"Program finished in {end - start:.5f}s")

# import os


# def get_case_info(string: str):
#     data = string[string.rfind("<putusan") : string.find(">")]
#     fields_string = {
#         1: "provinsi",
#         2: "klasifikasi",
#         3: "sub_klasifikasi",
#         4: "lembaga_peradilan",
#     }

#     out = []
#     for key in fields_string.keys():
#         start_index = data.find(f'{fields_string[key]}="') + len(
#             f'{fields_string[key]}="'
#         )
#         end_index = data.find('"', start_index + 1)
#         out.append(data[start_index:end_index])
#     print(out)


# for file in os.listdir("indo-law-main/subset"):
#     with open(f"indo-law-main/subset/{file}", "r") as content:
#         c = content.read()
#         get_case_info(c)


# def largest(s):
#     x = s[4]
#     for c in s:
#         if x > c:
#             pass
#         else:
#             x = c
#     return int(x, 2)

import copy

# print(largest("Hello"))

print("{:.<20} darkness my old {:.<20}".format("hello", "hi"))

# def two_sort(array):
#     my_str = str(sorted(array)[0])
#     fin_str = ""
#     for i in range(len(my_str)):
#         fin_str += my_str[i] + "***"
#     return fin_str[0:-3]


array= ["turns", "out", "random", "test", "cases", "are", "easier", "than", "writing", "out", "basic", "ones"]

print("***".join(min(array)))

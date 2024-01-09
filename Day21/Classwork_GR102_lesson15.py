import random

my_arr = []
for i in range(10):
    my_arr.append(str(random.randint(1,1000)))
print(my_arr)
print(" ".join(my_arr))

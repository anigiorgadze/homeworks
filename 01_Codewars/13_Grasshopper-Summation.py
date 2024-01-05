num = 22
my_sum = 0
i = 1
while i < num+1:
    my_sum += i
    i += 1
print(my_sum)


#2
def summation(num):
    my_sum = 0
    for i in range(num):
        my_sum += i+1
    return my_sum
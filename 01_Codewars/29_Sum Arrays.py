# Write a function that takes an array of numbers and returns the sum of the numbers. The numbers can be negative or non-integer. If the array does not contain any numbers then you should return 0.

# Examples
# Input: [1, 5.2, 4, 0, -1]
# Output: 9.2

# Input: []
# Output: 0

# Input: [-2.398]
# Output: -2.398

#1
def sum_array(a):
    my_sum = 0
    if len(a) == 0:
        return 0
    for element in a:
        my_sum += element
    return my_sum


#2
def sum_array(a):
    if len(a) == 0:
        return 0
    return sum(a)
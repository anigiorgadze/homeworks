# Convert number to reversed array of digits
# Given a random non-negative number, you have to return the digits of this number within an array in reverse order.

# Example(Input => Output):
# 35231 => [1,3,2,5,3]
# 0 => [0]



# def digitize(n):
#     my_str = str(n)
#     my_arr = []
#     for i in range(len(my_str)):
#         my_arr.append(int(my_str[-i-1]))
#     return my_arr


# print(digitize(123456))


# #2 ვარიანტი
# def digitize(n):
#     arr= []
#     for i in str(n):
#         arr.append(int(i))
        
        
#     arr.reverse()
#     return arr

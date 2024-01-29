
  #1
# def sum_array(arr):
#     if arr == None or len(arr) <= 2:
#         return 0
#     new_arr = sorted(arr)
#     sum = 0
#     for i in range(1,len(new_arr)-1):
#         sum += new_arr[i]
#     return sum
    
#2

def sum_array(arr):

    
    if arr == None or len(arr) <= 2:
        return 0
    return sum(sorted(arr)[1:-1])
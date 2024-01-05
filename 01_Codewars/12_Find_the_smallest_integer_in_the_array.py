#1
def find_smallest_int(arr):
    min_element = arr[0]
    for element in arr:
        if element <= min_element:
            min_element = element
    return min_element
    

 #2
def find_smallest_int(arr):
    return min(arr)

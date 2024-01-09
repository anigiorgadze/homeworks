
def minimum(arr):
    return min(arr)

def maximum(arr):
    return max(arr)



#2

def minimum(arr):
    min_element = arr[0]
    for element in arr:
        if element < min_element:
            min_element = element
    return min_element
        

def maximum(arr):
    max_element = arr[0]
    for element in arr:
        if element > max_element:
            max_element = element
    return max_element
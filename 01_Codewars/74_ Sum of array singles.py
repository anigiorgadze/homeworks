def repeats(arr):
    sum = 0
    for element in arr:
        if arr.count(element) == 1:
            sum += element
    return sum
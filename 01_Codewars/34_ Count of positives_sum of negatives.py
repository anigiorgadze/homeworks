def count_positives_sum_negatives(arr):
    if len(arr) == 0:
        return arr

    amount_of_positives = 0
    sum_of_negatives = 0
    
    for element in arr:
        if element > 0:
            amount_of_positives += 1
        elif element < 0:
            sum_of_negatives += element
            
    return [amount_of_positives,sum_of_negatives]
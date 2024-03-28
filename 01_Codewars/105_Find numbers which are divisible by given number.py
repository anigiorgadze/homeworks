def divisible_by(numbers, divisor):
    new_arr=[]
    
    for number in numbers:
        if number % divisor == 0:
            new_arr.append(number)
        continue
    return new_arr
# Every day you rent the car costs $40. If you rent the car for 7 or more days, you get $50 off your total. Alternatively, if you rent the car for 3 or more days, you get $20 off your total.


def rental_car_cost(d):
    if d >= 7:
        return d * 40 - 50
    elif d >= 3 and d < 7 :
        return d * 40 - 20
    else:
        return d * 40
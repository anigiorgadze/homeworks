# def quarter_of(month):
#     if month <=3:
#         return 1
#     elif month >3 and month <=6:
#         return 2
#     elif month > 6 and month <=9:
#         return 3
#     return 4


def quarter_of(month):
    months =[[1,2,3],[4,5,6],[7,8,9],[10,11,12]]
    
    for i in range(len(months)):
        if month in months[i]:
            return i+1
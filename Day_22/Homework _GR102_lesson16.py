#kahoot ის გარჩევა

#1

# my_arr = [i for i in range(15,25) if i % 4 == 2]
# print(my_arr)



#2

# friends = {
#     "dato" : "14",
#     "andria" : 15,
#     "luka" : "15",
#     "nika" : 14,
#     "AND OTHERS" : "?"
# }
# print(friends["nika"])
# print(friends["dato"])
# # გამოვა 14 14 



#3

# friends = {
#     "dato" : ["luka","nika"],
#     "andria" : ["zuka", "nika", "lasha"],
#     "gabrieli" : ["zuka", "andria", "duta"],
#     "nika" : ["dato", "luka", "tamari", "barbare"],
# }
# print(friends["gabrieli"][3]) #--> index out of range



#4

def twice_as_old(dad_years_old, son_years_old):
    return abs(dad_years_old - 2 * son_years_old)

# print(twice_as_old(47,14)*(33,2))  -- pasuxi vikitxo ? ?
# print(twice_as_old(47,14)*twice_as_old(33,9))   #- 285



#5

# friends = {
#     "dato" : ["luka","nika"],
#     "andria" : ["zuka", "nika", "lasha"],
#     "gabrieli" : ["zuka", "andria", "duta"],
#     "nika" : ["dato", "luka", "tamari", "barbare"],
# }


# print(friends["gabrieli"][0])
# print(friends["nika"][2])
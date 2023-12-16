import random

# print(random.randint(1,100))


my_students = ["nika", "gabrieli", "dato", "luka", "sandro", "oto"]

# print(my_students[random.randint(0,4)])



arr_of_cars = ["BMW", "mercedes", "prius", "subaru", "porsche", "bughati"]


# for i in range(len(my_students)):
#     print(random.choice(my_students), "won the car: : ", random.choice(arr_of_cars))


# print(random.choice(my_students))


for i in range(len(my_students)):
    winner = random.choice(my_students)
    lucky_car = random.choice(arr_of_cars)
    print(winner, "won the car: ", lucky_car)
    my_students.remove(winner)
    arr_of_cars.remove(lucky_car )

#მინიშნება
    # answer = input("did the student answer correctly: ")
    # if asnwer == "yes"
    # .......no
    #          daakldes 5qula
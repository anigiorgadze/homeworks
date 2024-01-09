my_arr = ["banana", 11, True, 10.5 , [1,2,3],5, 10]
print(my_arr[0][2])
# კვადრატული ფრჩხილით შექმნილი კოლექცია არის list

# print(my_arr[-1])
# print(my_arr[3])
# print(my_arr[0:6:2]) 
# print(my_arr[:4]) 

# menu = ["xinkali", "mwvadi", "qababi", "lobiani", "khachapuri", "wyali"]

# if "lobiani" in menu:
#     print("lobiani gvaqvs")

# menu[1] = "BBQ"
# print (menu)

# menu[2:4] = ["aa", "bb", "cc"]
# print(menu)

# my_name = "nikusha"
# new_name =""

# # for i in range(len(my_name)):
# #     if i==2 or i ==3:
# #         new_name +="x"
# #     else:
# #         new_name += my_name[i]

# # print(new_name)

# print(my_name.replace("ku","qq"))


# menu = ["xinkali", "mwvadi","lobiani", "qababi", "khachapuri", "wyali"]
# # menu.insert(3 , "nayini")
# # print(menu)



# menu.append("cecxli")
# menu.append("navti") #ბოლოში ამატებს ელემენტს
# print(menu)

# menu = []
# menu.append("pizza")
# print(menu)


#დავალება 

#მომხმარებელს შემოატანინეთ 5 საჭმელი
#სიაში შეიტანეთ ისინი, რომლებიც შეიცავენ მინიმუმ 2 "ა" -ს


# menu = []

# for i in range(5):
#     food = input("enter food: ")
# #     if food.count("a")>=2:
#         menu.append(food)
# print(menu)

#IIvarianti
# for i in range(5):
#     food = input("enter food: ")
#     ammount_of_a = 0
#     for char in food:
#         if char == "a":
#             ammount_of_a +=1
#     if ammount_of_a >=2:
#         menu.append(food)
#         ammount_of_a = 0
# print(menu)


# menu = ["xinkali", "mwvadi","lobiani", "qababi", "khachapuri", "wyali"]

# menu.remove("wyali")
# menu.remove("mwvadi")
# del menu[2]
# print(menu)

# #davaleb
# menu = ["xinkali", "mwvadi","lobiani", "qababi", "xachapuri", "wyali"]
# #წაშალეთ ის ელემენტები, რომლებშიც მეორე ასო არის a
# new_menu = []
# for food in menu:
#     if food[1] !="a":
#         new_menu.append(food)
# print(new_menu)




# scores = [20,2,43, 56, 73,6,87,97,45]
# scores.sort()
# print (scores)


# students = ["nika", "ana", "mamuka", "ana", "iva"]

# students.sort(reverse=True)
# print(students)
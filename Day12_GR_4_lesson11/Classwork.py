# # დავალების განხილვა
# #შექმენით random password generator პროგრამა, რომელშიც დაგენერირდება პაროლი, 8 სიმბოლოიანი, სადაც აუცილებლად 2 სიმბოლო იქნება !#@#$%, 2 სიმბოლო იქნება absgddbss... , 
# #ბოლო4 სიმბოლო იქნება ციფრები 1253434
# #მაგ: !n8391k*

# import random
 

# password = ""
# chars = "qwertyuiopasdfghjklzxcvbnm"
# symbols = "!@#$%^&*"
# numbers = "1234567890"
# my_arr = []

# for i in range(4):
#     my_arr.append(random.choice(numbers))
# for i in range(2):
#     my_arr.append(random.choice(chars))
#     my_arr.append(random.choice(symbols))

# print("the program chose thes characters:" , my_arr)
# final_password = ""
# for i in range(len(my_arr)):
#     current_char = random.choice(my_arr)
#     final_password += current_char
#     my_arr.remove(current_char)

# print("the final passwprd is: ", final_password)

string = "world"
new_string = ""


for i in range(len(string)):
    new_string += string[-i-1]
print(new_string)

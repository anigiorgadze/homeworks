#1) for loop
#2) while loop

 #i-საიტერაციო ცვლადი
# for i in range(len("giorgi")):  #range(7) = 0,1,2,3,4,5,6
#     print("nika")

# for i in range(3,6):  #range(3,6) = 3,4,5
#     print(str(i)+" nika")

        #start #finish #step
# for i in range(5,10,2):  #range(5,10,2) = 5,7,9
#     print(str(i)+" nika")


#while loop

# i = 0  # საიტერაციო ცვლადი
# while i < 5:
#     print("nika")
#     print(i)
#     i += 1   #საიტერაციო ცვლადის ინკრემენტაციას

 

# full_name = "ana giorgadze"

# i = 0
# while i < len(full_name):
#     print(full_name[i])
#     i += 1

#davaleba 1

#a = "qwerty"
#b = "asdfgh"

#qa
#ws
#ed ...

# a = "qwerty"
# b = "asdfgh"

# i = 0
# while i < len(a):
#     print(a[i]+ b[i])
#     i += 1



# if 10>5 and 3>1:
#     print("cool")
 

#Group4

# for i in range(3):
#   print("Hello")
# print ("nika") # ციკლი ამ პრინტზე აღარ გავრცელდება


#დავალება

#დაწერეთ პროგრამა, რომელიც მომხმარებელს შეეკითხება ასაკს და სახელს.
#ხოლო დაუპრინტავს შემდეგი 10 წლის განმავლობაში რამდენი წლის იქნება ყოველ წელს
#"ნიკა შენ იქნები 40 წლის 2024 წელს"
#"ნიკა შენ იქნები 41 წლის 2025 წელს" და ა.შ


# name = input("Enter your name: ")
# age =int(input ("Enter your age: "))
# i = 0
# year = 2023

# for i in range(1,11):
#     print("{}, you will be {} years old in {}.".format(name,age+i,year+i))
    


#while loop
#ყოველ იტერაციაზე დაიპრინტოს რამდენი ბილეთია დარჩენილი

seats = 10
while seats > 0:
  print("{} tickets left".format(seats))
  seats = seats - 1
else:
  print("There are no more tickets left.")
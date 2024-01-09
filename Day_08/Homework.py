        #ჯგუფი 102 დავალება 
    #davaleba 1

# def calculate_max(scores):
#     max_num = scores[0]

#     for score in scores:
#         if score > max_num:
#             max_num = score

#     print(max_num)

# calculate_max([10,22,44,500,33,111])


    #davaleba2


# # შეატრიალეთ უკუღმა, sort და რევერსის გარეშე

# def sort_reverse_list(arr):
#     new_arr=[]
#     for i in range(len(arr)):
#         if i == 0:
#             new_arr.append(arr[-1])
#         elif i !=0:
#             new_arr.append(arr[-i-1])
#     print(new_arr)


# sort_reverse_list(["ana", "beka","rati", "nika", "lili", "nini"])




    #davaleba 3
# def menu(food,price):
#     for i in range(min([len(food),len(price)])):
#         print ("{}'s price is {} lari.".format(food[i],price[i]))


# menu(["lobiani", "Burger"],[5,15])
    

    #davaleba 4
#მომხმარებლის ნიშნებისგან გამოიანგარიშება საშუალო არითმეტიკული და თუ ცხრაზე მეტი იქნება
#დაუპრინტეთ გილოცავ მატრიცელო შენ გადმოგეცა 300 ლარიანი ბანძი ტოსტერი რისთვისაც შეალიე შენი ცხოვრების წლები
#თუ ეს იქნება 5ზე ნაკლები დაუპრინტე გაექეცი მატრიცას
#თუ ეს იქნება 5დან 9მდე დაუპრინტე YOU ARE MID
#თუ იქნება 10-ზე მეტი ან 0-ზე ნაკლები დაუპრინტე there is something wrong with you

# def average_score(score1,score2,score3):
    
#     aver_score=(score1+score2+score3)/3

#     if aver_score > 10 or aver_score < 0:
#         print("there is something wrong with you")
#     elif aver_score > 9:
#         print("გილოცავ მატრიცელო შენ გადმოგეცა 300 ლარიანი ბანძი ტოსტერი რისთვისაც შეალიე შენი ცხოვრების წლები")
#     elif aver_score  >= 5 and aver_score<= 9:
#         print("YOU ARE MID")
#     elif aver_score <5:
#         print ("გაექეცი მატრიცას")

# average_score(11,2,33)
    





 #davaleba 5
#მომხმარებელს შემოატანინეთ ორი სახელი და ის დაპრინტეთ
#რომლის სახელშიც მეტი თანხმოვანი იქნება 



# def amount_of_consonant_in_name (name1,name2):
#     amount_of_consonant_in_name1=0
#     amount_of_consonant_in_name2=0

#     for char in name1:
#         if char not in "aeiou":
#             amount_of_consonant_in_name1 +=1
    
#     for char in name2:
#         if char not in "aeiou":
#             amount_of_consonant_in_name2 +=1

#     if  amount_of_consonant_in_name1 > amount_of_consonant_in_name2:
#         print("The amount of consonant in name 1 is more than name 2 and it contains {} consonants.".format(amount_of_consonant_in_name1))
#     elif amount_of_consonant_in_name1 < amount_of_consonant_in_name2:
#         print ("The amount of consonant in name 2 is more than name 1 and it contains {} consonants.".format(amount_of_consonant_in_name2))
#     else: 
#         print ("they contains aqual consonant")


# amount_of_consonant_in_name("ana","barbare")





#davaleba 6

#მომხმარებელმა ტერმინალიდან შემოიტანოს 3 რიცხვი
#აქედან მხოლოდ კენტები შეკრიბოს და დაპრინტოს 


# def sum_number(num1,num2,num3):
#     sum_num =0
#     if num1 % 2 != 0:
#         sum_num += num1
#     if num2 % 2 != 0:
#         sum_num += num2
#     if num3 % 2 != 0:
#         sum_num += num3

#     print(sum_num)


# sum_number(5,6,5)


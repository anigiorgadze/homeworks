#შექმენით პროგრამა, რომელშიც შექმნით ჯგუფელებისგან სიას, რენდომად გამოიძახებთ ერთ ჯგუფელს, თუ კითხვაზე უპასუხებს, მოემატება 10 ქულა და გადავა შემდეგზე , თუ ვერ გასცა დააკლდეს 5 ქულა.

import random

student_list = ["ana", "lasha", "lana", "nika", "nino"]
score_list= []
new_student_list = []
i=0



for i in range(len(student_list)):
    student = random.choice(student_list)
    print(student)
    answer = input("did the student answer correctly: ")
    if answer == "yes":
        score_list.append(10)
        new_student_list.append(student)
        student_list.remove(student)     
    elif answer == "no":
        score_list.append(-5)
        new_student_list.append(student)
        student_list.remove(student)
        i +=1   

for i in range(len(new_student_list)):
    print(new_student_list[i], "you have scored ", score_list[i], "points")
        
   








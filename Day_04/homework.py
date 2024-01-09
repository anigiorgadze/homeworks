#მომხმარებელს შემოატანინეთ ორი სახელი და ის დაპრინტეთ
#რომლის სახელშიც მეტი თანხმოვანი იქნება 

name1=input("enter name1: ")
name2=input("enter name2: ")

amount_of_consonant_in_name1 = 0
amount_of_consonant_in_name2 = 0

for char in name1:
    if char not in "aeiou":
        amount_of_consonant_in_name1 +=1


for char in name2:
    if char not in "aeiou":
        amount_of_consonant_in_name2+=1



if amount_of_consonant_in_name1 > amount_of_consonant_in_name2:
    print ("The amount of consonant in name 1 is more than name 2 and it contains {} consonants.".format(amount_of_consonant_in_name1))
elif amount_of_consonant_in_name1 < amount_of_consonant_in_name2:
    print ("The amount of consonant in name 2 is more than name 1 and it contains {} consonants.".format(amount_of_consonant_in_name2))
else: 
    print ("they contains aqual consonant")
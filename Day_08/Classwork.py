# #1) stingebze:

# name="nikax"
# scores=[20,43,5,97,73]

# for i in range(len(name)):
#     print(name[i] + "-" + str(scores[i]))




#davalebis garcheva:

# students = ["nika", "ana", "mamuka", "beqa", "dachi", "iva", "farna"]
# # new_students=[]
# # # შეატრიალეთ უკუღმა, sort და რევერსის გარეშე

# new_arr=[]
# i=len(students)

# while i>0:
#     new_arr.append(students[i-1])
#     i -=1
# print(new_arr)


#lesson 8

#ფუნქციონალური პროგრამირება - functional programming

# print("nika")
# print(max([10, 23, 6]))



# def wish_a_good_day(name, day):
#     print(name + " karg dges gisurveb "+ str(day) +" octombers")

# names =["nika", "ana", "mamuka", "beqa", "dachi", "iva", "farna"]
# # wish_a_good_day("shako",5)
# # wish_a_good_day("tamuna",17)

# for name in names:
#     wish_a_good_day(name, 17)


#შექმენით ფუნქცია, დაარქვით shekreba, არგუმენტად გადაეცემოდეს ორი რიცხვი და  პრინტავდეს მათ ჯამს

# def shekreba(num1, num2):
#     print("mocemuli ori ricxvis jamia "+ str(num1+num2))

# shekreba(15,200)



# def calculate_max(scores):
#     max_num = scores[0]

#     for score in scores:
#         if score > max_num:
#             max_num = score
#     print(max_num)


# calculate_max([20, 43, 5, 97, 10, 45, 83])




# def pair_sum(arr1, arr2):
#     for i in range(len(arr1)):
#         print (arr1[i]+arr2[i])


# pair_sum([20, 43, 5], 
#          [2, 4, 51])




# def pair_sum(arr1, arr2):
#     for i in range(min([len(arr1),len(arr2)])):
#         print (arr1[i]+arr2[i])

# pair_sum([20, 43, 5,6], 
#        [2, 4, 51])

        #1 რა დაიპრინტება
# list_num = list((range(abs(-3),7)))

# print(list_num)   #პას: [3, 4, 5, 6]

        #2 რამდენი ხაზი დაიპრინტება

# greeting ="G O  A"

# for char in greeting:
#     print ("char  + !")  #pass : Len(greeting)


        #3 რა ერორი გამოვა ტერმინალში

# a = [4, 1, 2, 3]
# b = list(range(1, 6, 2))  #b=[1,3,5]
# for i in a:  #=4
#     b.append(a[i+1]+a[i]) #a[5]list index out of range 

# prit(B)

        #4 რას გამოიტანს ტერმინალი:
# user_name = "GigaNigga" 
# Print("Hello, " + user_name) #didi asotia print

#         #5 რა დაიპრინტება ტერმინალში
# list = [[3, 5], [2, 1, 4, 1], [1,1,2]]

# print(list[list[2][list[1][3]]][2]) #pass: 4


        #6 ra aris total-i?

# kalata = [20, 40, 10]
# fasdakleba = 20
# total =0

# for item in kalata:
#     total += item - (item *fasdakleba // 100)

# print(str(float(total)) + " is your total price.")
#pass რადგან თოტალს გვეკითხებონდენიქნება 56 და აარ  რრა დაიპრინტება

    #7 რა დაიპრინტება ტერმინალში

# full_name = "Jeki-Chadi"

# for char in full_name[5::2]:
#     if char == "c":
#         break
#     print(char)

        #8რამდენი ხაზი დაიპრინტება ტერმინალში:
# numbers = list(range(50, 10, -5))

# for number in numbers:
#     if number <= 0:
#         break
#     print(number -20)



# my_arr = [i for i in range(10)]

# print(my_arr)

        #davaleba

def zipped (aa,bb,cc):
        # aa = ["a", "b", "c", "d"]
        # bb = ["1", "2", "3", "4"]
        # cc = ["sandro", "misha", "dato", "nika"]
        final_str = []
        

        for i in range(len(aa)):
                final_str.append("{}{}{}".format(aa[i],bb[i],cc[i]))

        print(final_str)

zipped(["a", "b", "c", "d"],["1", "2", "3", "4"],["z", "x", "y", "w"])









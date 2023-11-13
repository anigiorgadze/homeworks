#მომხმარებელმა ტერმინალიდან შემოიტანოს 3 რიცხვი
#აქედან მხოლოდ კენტები შეკრიბოს და დაპრინტოს 


num_1 = int(input("Enter I number: "))
num_2 = int(input("Enter II number: "))
num_3 = int(input("Enter III number: "))

if (num_1%2 )!=0 and (num_2%2 )!=0 :
    print(num_1 + num_2)
if (num_2%2 )!=0 and (num_3%2) !=0:
    print(num_2+num_3)
if (num_1%2 )!=0 and (num_3%2) !=0:
    print (num_1+num_3)
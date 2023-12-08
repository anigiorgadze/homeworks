# შექმენით random password generator პროგრამა, რომელშიც დაგენერირდება პაროლი, 8 სიმბოლოიანი, სადაც აუცილებლად 2 სიმბოლო იქნება !#@#$%, 2 სიმბოლო იქნება absgddbss... , 
#ბოლო4 სიმბოლო იქნება ციფრები 1253434
#მაგ: !n8391k*
import random

number_arr = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
alphabet_arr = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
symbol_arr = ["!", "@", '$', '%', '^', '&', '*', '(', ')', '_' ,'+']
password = []

for i in range(4):
    choosen_num=random.choice(number_arr)
    password.append(choosen_num)
    number_arr.remove(choosen_num)

for i in range(2):
    choosen_symbol=random.choice(symbol_arr)
    password.append(choosen_symbol)
    symbol_arr.remove(choosen_symbol)

for i in range(2):
    choosen_alp=random.choice(alphabet_arr)
    password.append(choosen_alp)
    alphabet_arr.remove(choosen_alp)

print(password)

print("Password: ",password[0],password[1],password[2],password[3],password[4],password[5],password[6],password[7])
    
str = "hello world"
my_list = str.split() # ['hello', 'world']

arr = ["ana", "luka", "nino", "gio"]
fin_sentence = " ".join(arr)
print(fin_sentence)

print(fin_sentence.upper()) #ყველა ასოს ადიდებს
print(fin_sentence.capitalize()) #პირველ ასოს წერს დიდად

nino_index = arr.index("nino")
print(nino_index)

print(str.index("o"))
 
 # davaleba

name = "rattti"
new_name = ""

for char in name:
    if char == "t":
        new_name += "T"
    else:
        new_name += char
print(new_name)


#2
print(name.replace("t","T"))

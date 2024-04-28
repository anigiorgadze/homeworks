#მომხმარებელს შემოატანინეთ წინადადება და შემოტანილ წინადადებაში დათვალეთ რამდენი ხმოვანი და რამდენი თანხმოვანია

sentence = input("Enter sentence: ")
num_of_vowel = 0
num_of_consonant = 0
for char in sentence:
    if char in "aeiou":
        num_of_vowel +=1
    elif char not in "aeiou" and char not in " ":
        num_of_consonant +=1

print("There are {} vowels and {} consonants in our sentence".format(num_of_vowel, num_of_consonant))



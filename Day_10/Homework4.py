#მომხმარებელს აინტერესებს მისი დაბადების წელი რომელ ზოდიაქოს ეკუთვნის. შემოატანინეთ მომხმარებელს  წელი, რომლის მიხედვით  ავტომატურად უნდა გამოვიდეს რომელ ზოდიაქოს ეკუთვნის

year=int(input("enter the desired year: "))
chinesse_zodiac =["Rat", "Ox", "Tiger", "Rabbit", "Dragon", "Snake", "Horse", "Goat", "Monkey", "Rooster", "Dog",  "Pig"]
rat_year = 1996

for i in range(12):
    if (year-rat_year) % 12 == i:
        print("Your zodiac is "+ chinesse_zodiac[i])
       
   




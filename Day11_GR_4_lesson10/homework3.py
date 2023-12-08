# #turtle-თი რენდომ რიცხვებით დახაზეთ შედევრი
# forward(random.randint(100))


from turtle import *
import random
colors= ["red", "black", "green", "blue", "yellow", "brown"]


for i in range(random.randint(10,50)):
    speed(7)
    width(random.randint(3,5))
    color(random.choice(colors))
    forward(random.randint(200,500))
    left(90)
    forward(random.randint(200,500))
    left(90)
    forward(random.randint(200,500))
    
penup()
goto(20,120)
pendown()


for i in range(random.randint(10,50)):
    speed(7)
    width(random.randint(3,5))
    color(random.choice(colors))
    forward(random.randint(200,500))
    left(90)
    forward(random.randint(200,500))
    left(90)
    forward(random.randint(200,500))
  

    

    




exitonclick()
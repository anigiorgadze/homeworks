#შექმენით ფუნქცია, რომელსაც გადაეცემა ორი მოთამაშის ქულა,
#დაიპრინტოს წინადადება "ამას უფრო მეტი ქულა აქვს ამდენით"


def compare_score(score1,score2):
    if score1 > score2:
        print("First player's score is higher",score1-score2,"than second")
    elif score2 > score1:
        print("Second player's score is higher",score2-score1,"than first")
    else:
        print("Both player's score is same")



def multify(a,b):
    return a * b


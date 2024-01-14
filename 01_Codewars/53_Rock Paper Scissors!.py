# Let's play! You have to return which player won! In case of a draw return Draw!.

# Examples(Input1, Input2 --> Output):

# "scissors", "paper" --> "Player 1 won!"
# "scissors", "rock" --> "Player 2 won!"
# "paper", "paper" --> "Draw!"


#1
def rps(p1, p2):
    if (p1 == "scissors" and p2 == "paper") or (p1 == "rock" and p2 =="scissors") or (p1 == "paper" and p2 == "rock"):
        return "Player 1 won!"
    elif p1 == p2:
        return "Draw!"
    return "Player 2 won!"


#2


def rps(p1, p2):
    winner_combo = { "rock": "scissors",
                    "scissors": "paper",
                    "paper": "rock"                   
    }
    
    if winner_combo[p1] == p2:
        return "Player 1 won!"
    if winner_combo[p2] == p1:
        return "Player 2 won!"
    return "Draw!"
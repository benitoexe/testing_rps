import random
def test_rps(player1, player2):

    player1 = str("rock", "scissors", "paper")
    player2 = str("rock", "scissors", "paper")

if player1 == "rock" and player2 == "paper":
    return "player2"
if player1 == "rock" and player2 == "scissors":
    return "player1"
if player1 == "rock" and player2 == "rock":
    return "tie"

if player1 == "paper" and player2 == "rock":
    return "player1"
if player1 == "paper" and player2 == "scissors":
    return "player2"
if player1 == "paper" and player2 == "paper":
    return "tie"

if player1 == "scissors" and player2 == "paper":
    return "player1"
if player1 == "scissors" and player2 == "rock":
    return "player2"
if player1 == "scissors" and player2 == "scissors":
    return "tie"

def player_choice(ptype):
    if ptype == "c":
        player_choice = random.choice(["r", "p", "s"])
    else:
        player_choice = input("enter r for rock, p for paper, or s for scissors:  ")

    return player_choice

p1 = player_choice("h")
p2 = player_choice("c")

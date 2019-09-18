import random
from banner import banner

def get_player_choice():
    print("1. Rock")
    print("2. Paper")
    print("3. Scissors")
    name = int(input("What is your choice? "))
    return name

banner("Rock, Paper, Scissors", "Lilly")
input("We are going to play a game of Rock,Paper,Scissors.The first to Win two out of three rounds wins.")

print("SCORE:CPU = 0 player= 0")
player_score = 0

player_choice = get_player_choice()
cpu_choice = random.randint(1,3)
if player_choice == 1:
    if cpu_choice == 1:
        print("You chose Rock, and the Computer chose rock. It is a tie.")
    if cpu_choice == 2:
        print("You chose Rock,and the computer chose paper.The computer wins.")
        cpu_score = cpu_score +1
    if cpu_choice == 3:
        print("You chose Rock,and the Computer chose scissors.")
        player_score = player_score +1
    cpu_score = +0
    player_score = +1

player_choice = get_player_choice()
cpu_choice = random.randint(1,3)
if player_choice == 1:
    if cpu_choice == 3:
        print("You chose paper,and the Computer chose Rock. You win.")
    elif cpu_choice ==2:
        print("You chose paper,and the Computer chose scissors. The computer wins.")
    cpu_score = 1
    player_score = 1

player_choice = get_player_choice()
cpu_choice = random.randint(1,3)
if player_choice == 3:
    if cpu_choice == 2:
        print("You chose Scissors,and the Computer chose Rock. It is a tie.")
    if cpu_choice == 12:
        print("You chose paper,and the Computer chose scissors. The computer wins.")
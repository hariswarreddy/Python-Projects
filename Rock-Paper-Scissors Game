"""
The Rock Paper Scissors Game
Designed By : Bontha Hariswar Reddy
This game can be played by maximum of two players and min of 1 player (the other will be the computer)
"""
import random

def rock_paper_scissors(player,computer):
    if player==computer:
        return "It's a tie!"
    elif (player=="rock" and computer =="scissors") or (player == "paper" and computer=="rock") or (player=="scissors" and computer=="paper"):
        return "You Win!!🥳"
    else:
        return "You Lose!!😔"

def rock_paper_scissors_2(player_1,player_2):
    if player_1==player_2:
        return "It's a tie!"
    elif (player_1=="rock" and player_2 =="scissors") or (player_1 == "paper" and player_2=="rock") or (player_1=="scissors" and player_2=="paper"):
        return "Player 1 Wins!!"
    else:
        return "Player 2 Wins!!"


print("Welcome to the Rock-Paper-Scissors Game!")
print("-------------------------------------------------")
print("Instructions:")
print("1. This game can be played by a maximum of two players or just one player against the computer.")
print("2. Enter 'rock', 'paper', or 'scissors' to make your choice.")
print("3. The rules are:")
print("   - Rock crushes Scissors.")
print("   - Scissors cut Paper.")
print("   - Paper covers Rock.")
print("4. Let's start the game! May the best player win.")
print("-------------------------------------------------\n")

n = int(input("Enter number of players 1 or 2:"))
choices = ["rock","paper","scissors"]
if n==1:
    player_choice = input(f"Enter your choice from {choices}:").strip().lower()
    computer_choice = random.choice(choices)
    print(f"Computer's Choice :{computer_choice}")
    result = rock_paper_scissors(player_choice, computer_choice)
    print(result)
elif n==2:
    first_player_choice = input(f"Enter first player choice from {choices}:").strip().lower()
    second_player_choice = input(f"Enter second player choice from {choices}:").strip().lower()
    result = rock_paper_scissors_2(first_player_choice,second_player_choice)
    print(result)
elif n>2:
    print("Number of Players are More")
    print("Try Again !!")
else:
    print("Invalid Number Of Players")

print("-------------------------------------------------")
print("Thank you for playing! We hope you enjoyed the game.")

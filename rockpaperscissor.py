import random

user_score = 0
computer_score = 0

while True:
    user_choice = input("Enter your Choice - (rock, paper, or scisscor) : ")
    
    while user_choice not in ['rock','paper','scissor']:
        user_choice = input("Invalid Choice. Enter your Choice - (rock, paper, or scisscor) : ")
        
    computer_choice = random.choice(['rock','paper','scissor'])
    
    print("\n\tYou Chose    : ",user_choice)
    print("\tComputer Chose : ",computer_choice,"\n")
    
    if user_choice == computer_choice:
        print("It's a Tie!!!")
    elif (user_choice == 'rock' and computer_choice == 'scissor') or \
        (user_choice == 'scissor' and computer_choice == 'paper') or \
        (user_choice == 'paper' and computer_choice == 'rock'):
        print("You Win!")
        user_score +=1
    else:
        computer_score +=1
        
    print(f"Score - You : {user_score}, Computer : {computer_score}\n")
    
    play_aga = input("Do you want to play again? (yes/no) : ")
    while play_aga not in ['yes','no']:
        play_aga = input("Invalid input. Do you want to play again? (yes/no) : ")
        
    if play_aga == 'no':
        break

print("Thanks for Playing..!")
    
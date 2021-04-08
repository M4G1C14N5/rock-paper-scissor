import random 

def play():
    user_score = 0
    computer_score = 0
    round = int(input("How many rounds?: "))
    print("'r' for rock, 'p' for paper, 's' for scissors")
    for x in range(round):
        user = input("What's your play?: ")
        computer = random.choice(['r','p','s'])
        print(f"Round {x+1}:")
        if user == computer:
            print("both played {user}")
            print("It's a tie!")
            print (f"You: {user_score} - Computer: {computer_score}")
        elif(user == 'r' and computer == 's') or (user == 's' and computer == 'p') \
            or (user == 'p' and computer == 'r'):
            print("Player played {user}, and computer played {computer}")
            print(f"Player wins!")
            user_score = user_score +1 
            print (f"You: {user_score} - Computer: {computer_score}")
        elif(user == 's' and computer == 'r') or (user == 'p' and computer == 's') \
            or (user == 'r' and computer == 'p'):
            print("Player played {user}, and computer played {computer}")
            print(f"Computer wins!")
            computer_score = computer_score +1 
            print (f"You: {user_score} - Computer: {computer_score}")
    if user_score == computer_score:
        print("Tie! No winner.")
    elif user_score < computer_score:
        print("You lose sucker!") 
    elif user_score > computer_score:
        print("You won!? That was definitely a fluke")

play()




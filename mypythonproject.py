import random
def RockPaperScissor():
    user_score=0
    computer_score=0
    try:
        rounds=int(input("Enter the number of rounds you want to play: "))
    except ValueError:
        print("Invalid input.Starting with 3 rounds by default.")
        rounds=3
    print("Welcome to Rock-Paper-Scissors!!")
    for round_num in range(1,rounds+1):
        print(f"\nRound {round_num} of {rounds}")
        p1=input("Select Rock(\U0001FAA8),Paper(\U0001F4C4) or Scissor(\U00002702)\n").strip().lower()
        while p1 not in ["rock", "paper" ,"scissor"]:
            p1=input("Invalid choice please select Rock,Paper,Scissors:\n").strip().lower()
        print(f"First player selected: {p1}")
        p2=random.choice(["Rock","paper","Scissor"]).lower()
        print(f"Computer selected: {p2}")
        if p1== "rock" and p2=="paper":
            print("Computer won \U0001F4C4 covers \U0001FAA8")
            computer_score+=1
        elif p1=="paper" and p2=="scissor":
            print("Computer won \U00002702 cuts \U0001F4C4")
            computer_score+=1
        elif p1=="scissor" and p2=="rock":
            print("Computer won \U0001FAA8 crushes \U00002702")
            computer_score+=1
        elif p1==p2:
            print("tie \U0001F91D")
        else:
            print("You won \U0001F389")
            user_score+=1
    print("\n---Game Over---")
    print(f"Final Scores:\n You: {user_score} | Computer: {computer_score}")
    if user_score > computer_score:
        print("Congratulations! You are the overall winner \U0001F389")
    elif user_score < computer_score:
        print("Computer is the overall winner \U0001FAA8 \U0001F4C4 \U00002702")
    else:
        print("The game ended in a tie! \U0001F91D")
    playagain=input("Do you want to play again? choose yes/no :").strip().lower()
    if playagain!="yes":
        print("Thanks for playing!!!")
        print("-------\U0001F64F\U0001F64F\U0001F64F-------")
    else:
        return RockPaperScissor()
RockPaperScissor()
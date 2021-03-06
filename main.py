import random


# used to redo user input if they input something other than y or n

def redo_start(a):
    if "y" not in a:
        if "n" not in a:
            a = input("please type 'y' or 'n': ")
            return a


def wrong_input(a):
    if "rock" not in a:
        if "paper" not in a:
            if "scissors" not in a:
                new_input = input("wrong input! Please type a valid input : ")
                return new_input


start_game = input("start Rock, Paper, Scissors game? (y) (n): ")
start_game = redo_start(start_game)

while start_game == "y":
    player_move = input("Do you choose paper, rock, or scissors? ")
    player_move = wrong_input(player_move)
    # starts computer move and covers tie scenario

    computer_move = random.randint(1, 3)
    if computer_move == 1:
        computer_move = str("rock")
    elif computer_move == 2:
        computer_move = str("paper")
    else:
        computer_move = str("scissors")

    # this section cover outcomes for non-tie scenarios

    if "paper" in computer_move:
        if "rock" in player_move:
            print("Computer chose paper")
            print("Computer wins")
            print()
        elif "scissors" in player_move:
            print("Computer chose paper")
            print("You win!")
            print()

    if "rock" in computer_move:
        if "paper" in player_move:
            print("Computer choose rock")
            print("You win!")
            print()
        elif "scissors" in player_move:
            print("Computer chose rock")
            print("Computer wins")
            print()

    if "scissors" in computer_move:
        if "rock" in player_move:
            print("Computer chose scissors")
            print("You win!")
            print()
        elif "paper" in player_move:
            print("Computer chose scissors")
            print("Computer wins!")
            print()

    if computer_move == player_move:
        print("Computer chose " + computer_move)
        print("This round ends in a draw")
        print()

    if "rock" not in player_move:
        if "paper" not in player_move:
            if "scissors" not in player_move:
                print("input is not valid")
                print()

    # offers user to play another round

    start_game = input("would you like to play another round? (y) (n): ")
    redo_start(start_game)

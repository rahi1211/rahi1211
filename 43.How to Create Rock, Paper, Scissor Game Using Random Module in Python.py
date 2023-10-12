import random

while True:
    ccount = 0
    ucount = 0
    uc = int(input('''
Game Start..
1 Yes
2 No | Exit
'''))
    if uc == 1:
        for a in range(1, 6):
            userTinput = int(input('''
1 Rock
2 Scissors
3 Paper
'''))
            if userTinput == 1:
                uchoice = "rock"
            elif userTinput == 2:
                uchoice = "scissors"
            elif userTinput == 3:
                uchoice = "paper"
            else:
                print("Invalid choice, please choose 1, 2, or 3.")
                continue

            choices = ["rock", "paper", "scissors"]
            cchoice = random.choice(choices)

            print("Computer choice:", cchoice)
            print("Your choice:", uchoice)

            if uchoice == cchoice:
                print("It's a draw!")
            elif (uchoice == "rock" and cchoice == "scissors") or \
                 (uchoice == "scissors" and cchoice == "paper") or \
                 (uchoice == "paper" and cchoice == "rock"):
                print("You win!")
                ucount += 1
            else:
                print("Computer wins!")
                ccount += 1

        if ucount == ccount:
            print("Final Game Draw")
        elif ucount > ccount:
            print("Final win the Game.")
        else:
            print("Final computer win the Game.")
        print("User score:", ucount)
        print("Computer score:", ccount)

    elif uc == 2:
        break
    else:
        print("Invalid choice, please choose 1 or 2.")

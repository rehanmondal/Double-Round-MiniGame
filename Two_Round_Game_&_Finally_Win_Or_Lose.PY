import random

print("\n~~~~~~~~~~~~~~~~   STONE-PAPER-SCISSOR ~~~~~~~~~~~~")
print("\n~~~~~~~~~~~~~~~~~~~~~   BY REHAN ~~~~~~~~~~~~")
print("        \t\tGAME \n")
print("To choose Stone Press - S")
print("To choose Paper Press - P")
print("To choose Scissor Press - C")
# INDENTATION OF DEF = INDENTATION OF CALLING **
score = 0
i = 1
while i <= 5:
    def win_game(comp, you):

        if comp == you:
            return None
            # comp ---------   stone
        elif comp == 'S':
            if you == 'P':
                return True
            elif you == 'C':
                return False
        # comp ---------   paper
        elif comp == 'P':
            if you == 'S':
                return False
            elif you == 'C':
                return True
        # comp ---------   cissor
        elif comp == 'C':
            if you == 'P':
                return False
            elif you == 'S':
                return True


    # ** HERE INDENTATION END , function er baire ese baki kaj, func a sdhu if else condition tuku.
    print("\nComputer's turn - Done")
    comp_rand_turn = random.randint(1, 3)
    if comp_rand_turn == 1:
        comp = 'S'
    elif comp_rand_turn == 2:
        comp = 'P'
    elif comp_rand_turn == 3:
        comp = 'C'

    you = input("Your Turn - ")
    you = you.upper()
    result = win_game(comp, you)

    print(f"Computer choose - {comp}")
    print(f"You choose - {you}")
    if result == True:
        while True:
            score = score + 1
            print("You win !\n")
            break

    elif result == None:
        print("Game is draw \n")
    elif result == False:
        print(":( You Lose \n")

    i = i + 1  # loop er vitor increment
print("5 rounds completed !!")
print('Your score is - ', score)
print("\n")

if score > 2:

    print("Score satisfied ! Next Level is unlocked !")  # ekhan theke next file a
    choice = input("Want to play Next round Now ? Press ( Y / N ) - ")
    if choice.casefold() == 'y':
        print("\n~~~~~~~~~~~~~~~~~ ROUND 2 ~~~~~~~~~~~~~~~~~~~~~~~~")
        print("\nTo Win the Game you have to Guess The number within 10 Attemts")
        print("\tGUESSING THE NUMBER BETWEEN 1 to 10\n")


        # score_2=1  # is there any prob , becoz it is newly added  -> yes prob
        def nextRound():
            score_2 = 1
            game = True

            name = input("Enter your Name - ")
            print("\n")
            while game:
                comp = random.randint(1, 10)

                try:
                    user_gus = int(input("Guess the number :  "))
                    if comp == user_gus:
                        print("Yee ..Its Right guess !!")
                        print(f"Hey {name} you have done it in ", score_2, " attemts \n")
                        game = False
                        if score_2 <= 10:
                            print("HURRAY ! YOU WIN THE GAME")
                        else:
                            print("You LOSE !Too Much Attemts To Guess ,Try Better Next Time.\n")

                        # a= newround=False
                    else:
                        print("It was - ", comp)
                        print("Try again !! \n")
                        score_2 = score_2 + 1
                except:
                    print("Input Must Be a valid Number between 1 to 10\n")


        nextRound()

    else:
        print("Come back soon ..Waiting Intresting Funs for you !!\n")

else:
    print("Score Not Satisfied !Try again !! \n")

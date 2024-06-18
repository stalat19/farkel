import random

score_limit = 1500

rules_text = (
    f"Welcome to the game of Farkle! Please note the rules are as follows:\n"
    f"You and the computer will take turns rolling 6 dice at a time. The first to {score_limit} points wins.\n"
    f"Rolling a 1 is worth 100 points, and rolling a 5 is worth 50 points.\n"
    f"Rolling three 1s is worth 1,000 points. Three of a kind of any other number are worth 100 points x the number, e.g., three 4s are worth 400 points.\n"
    f"Four or more of a kind are worth double the points of three of a kind, so four 4s are worth 800 points, five 4s are worth 1,600 points, etc.\n"
    f"By that same logic, four 1s are worth 2000 points, five 1s are worth 4000 points, etc."
    )

def dice_roll():# roll 6 dice and store the results in a list
    rolls = []
    for i in range(6):
         rolls.append(random.randint(1, 6))
    return rolls

def calculate_score(rolls: list):
    frequencies_dict = {1:0, 2:0, 3:0, 4:0, 5:0, 6:0}
    for roll in rolls:
        frequencies_dict[roll] += 1

    score = 0
    
    # Handle three or more of a kind of a given number
    for num in range(1,7):
        if frequencies_dict[num] >= 3:
            if num == 1:
                score += 1000 * (2 ** (frequencies_dict[num] -3))
            else:
                score += num * 100 * (2 ** (frequencies_dict[num] - 3))
            frequencies_dict[num] = 0 # resets the frequency to avoid double counting
    
    # Count score for remaining 1s and 5s
    score += frequencies_dict[1] * 100
    score += frequencies_dict[5] * 50    

    return score

def main():
    print(f"{rules_text}\n")
    
    while True: # provides option to let the player replay the game
        user_score = 0
        computer_score = 0

        while user_score < score_limit and computer_score < score_limit:
            # human player's turn
            input("Press Enter to roll the dice.")
            user_rolls = dice_roll()
            user_points_bank = calculate_score(user_rolls)
            user_score += user_points_bank
            sorted_user_rolls = sorted(user_rolls)
            print(f"You rolled: {sorted_user_rolls}.\nYou gained {user_points_bank} points. Your score is {user_score}.\n")

            if user_score >= score_limit:
                print("Congratulations, you win!")
                break

            # computer's turn
            input("It's the computer's turn. Please Enter to continue")
            computer_rolls = dice_roll()
            comp_points_bank = calculate_score(computer_rolls)
            computer_score += comp_points_bank
            sorted_computer_rolls = sorted(computer_rolls)
            print(f"The computer rolled: {sorted_computer_rolls}.\nThe computer gained {comp_points_bank} points. The computer's score is {computer_score}.\n")

            if computer_score >= score_limit:
                print("The computer wins! Better luck next time.")
                break

        # prompt player to continue playing
        play_again = input("Do you want to play another round? (yes/no)").strip().lower()
        if play_again != "yes":
            print("Thanks for playing, see you next time!\n")
            break

if __name__ == "__main__":
    main()
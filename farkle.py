import random

score_limit = 1000

rules_text = (
    f"Welcome to the game of Farkle! Please note the rules are as follows:\n"
    f"You and the computer will take turns rolling 6 dice at a time. The first to {score_limit} points wins.\n"
    f"Rolling a 1 is worth 100 points, and rolling a 5 is worth 50 points."
    f"Rolling three 1s is worth 1,000 points. Three of a kind of any other number are worth 100 points x the number, e.g., three 4s are worth 400 points"
    f"Four or more of a kind are worth double the points of three of a kind,\n so four 4s are worth 800 points, five 4s are worth 1,600 points, etc."

    )

def dice_roll():# roll 6 dice and store the results in a list
    rolls = []
    for i in range(6):
         rolls.append(random.randint(1, 6))
    return rolls

def three_of_a_kind(rolls: list):
    score = 0
    frequencies_dict = {1:0, 2:0, 3:0, 4:0, 5:0, 6:0}
    for roll in rolls: # count frequency of dice rolls and update dictionary
        frequencies_dict[roll] = frequencies_dict.get(roll, 0) + 1
    
    for number in frequencies_dict:
        frequency = frequencies_dict[number]
        if frequency == 3:
            if number == 1:
                score += 1000
            else:
                score += number * 100
            frequencies_dict[number] -= 3 # remove the 3 of a kind from the frequencies_dict to avoid double counting
            
    score += frequencies_dict[1] * 100 + frequencies_dict[5] * 50
    return score
    
def four_of_a_kind(rolls: list):
    score = 0
    frequencies_dict = {1:0, 2:0, 3:0, 4:0, 5:0, 6:0}
    for roll in rolls: # count frequency of dice rolls and update dictionary
        frequencies_dict[roll] = frequencies_dict.get(roll, 0) + 1
    
    for number in frequencies_dict:
        frequency = frequencies_dict[number]
        if frequency == 4:
            if number == 1:
                score += 2000
            else:
                score += (number * 200)
            frequencies_dict[number] -= 4 # remove the 4 of a kind from the frequencies_dict to avoid double counting
            
    score += frequencies_dict[1] * 100 + frequencies_dict[5] * 50
    return score

def five_of_a_kind(rolls: list):
    score = 0
    frequencies_dict = {1:0, 2:0, 3:0, 4:0, 5:0, 6:0}
    for roll in rolls: # count frequency of dice rolls and update dictionary
        frequencies_dict[roll] = frequencies_dict.get(roll, 0) + 1
    
    for number in frequencies_dict:
        frequency = frequencies_dict[number]
        if frequency == 5:
            if number == 1:
                score += 4000
            else:
                score += (number * 400)
            frequencies_dict[number] -= 5 # remove the 5 of a kind from the frequencies_dict to avoid double counting
            
    score += frequencies_dict[1] * 100 + frequencies_dict[5] * 50
    return score
    
def six_of_a_kind(rolls: list):
    score = 0
    frequencies_dict = {1:0, 2:0, 3:0, 4:0, 5:0, 6:0}
    for roll in rolls: # count frequency of dice rolls and update dictionary
        frequencies_dict[roll] = frequencies_dict.get(roll, 0) + 1
    
    for number in frequencies_dict:
        frequency = frequencies_dict[number]
        if frequency == 6:
            if number == 1:
                score += 8000
            else:
                score += (number * 800)
            frequencies_dict[number] -= 6 # remove the 6 of a kind from the frequencies_dict to avoid double counting
            
    score += frequencies_dict[1] * 100 + frequencies_dict[5] * 50
    return score
    
def calculate_score(rolls: list):
    score = 0
    score += max(three_of_a_kind(rolls), four_of_a_kind(rolls), five_of_a_kind(rolls), six_of_a_kind(rolls))
    return score


def main():
    print(f"{rules_text}\n")
    
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

    



if __name__ == "__main__":
    main()
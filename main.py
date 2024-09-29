import random

chance = 0

def random_number():
    return random.randint(1,100)

def difficulty_select():
    print("|| E = Easy (20 chances)   ||\n|| M = Medium (10 chances) ||\n|| H = Hard (5 chances)    ||\n")
    choice = str(input("Please select difficulty level :")).lower()
    while True:
        if choice == "e":
            difficulty = "Easy"
            chances = 20
            return difficulty,chances
        elif choice == "m":
            difficulty = "Medium"
            chances = 10
            return difficulty,chances
        elif choice == "h":
            difficulty = "Hard"
            chances = 5
            return difficulty,chances
        else:
            print("Invalid choice,please enter availabel option!!")

def the_game():
    difficulty,chances = difficulty_select()
    number_to_guess = random_number()
    attempts = 0
    global chance
    chance = chance + chances
    
    print(f"You choose {difficulty} diffculty with {chances} chances")
    print("Good Luck & Have Fun \n")
    
    while attempts < chances:
        try:
            guess = int(input("Enter your guess : "))
        except ValueError:
            print("You input an invalid number,please try again")
            continue
        attempts += 1
        
        if guess < number_to_guess:
            print("Incorrect!! Your guess is too low,please enter your guess again\n")
        elif guess > number_to_guess:
            print("Incorrect!! Your guess is too high,please enter your guess again\n")
        else:
            print(f"Congratulations you can guess the number in {attempts} attempts")
            return attempts
    print(f"\nSorry your chances are runs out,the number you must guess is {number_to_guess}")
    return attempts,chance
            
    

def welcome_massage():
    print("###################################")
    print("### Welcome to Guess The Number ###")
    print("###################################")
    name = str(input("Enter your name : "))
    print("Welcome " + name + ",to the Guess The Number\n")
    print("The rules are simple you just guess the number i think between 1 and 100")
    print("Good Luck and Have Fun\n")
    return name

def main():
    high_score = 0
    
    while True:
        name = welcome_massage()
        attempts = the_game()

        if chance == 20:
            high_score = high_score + (100 - (attempts * 5 ))
        elif chance == 10:
            high_score = high_score + (100 - (attempts * 10))
        elif chance == 5:
            high_score = high_score + (100 - (attempts * 20))
        
        if high_score > 0:
            print(f"Your Current High Score is {high_score} point")
        else:
            print(f"Your Current High Score is 0 point")
            
        play_again = input("\n Do you want play again? (y/n) : ").strip().lower()
        if play_again != "y":
            print(f"Thank you for playing with me {name}! Goodbye and Have a nice day!\n\n")
            break

main()
            
    
    

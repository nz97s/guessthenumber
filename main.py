import random

num = random.randint(1,100)

def dif_easy():
    chances = int(15)
    attempt = int(0)
    print("Your chances is " + str(chances))
    g_num = int(input("Enter your guess : "))
    while g_num != num & chances > 0:
        if g_num < num:
            g_num = int(input("Incorrect!! Your guess too low, guess again = "))
            print("Chance remeaning is " + str(chances))
        elif g_num > num:
            g_num = int(input("Incorrect!! Your guess too high, guess again = "))
            print("Chance remeaning is " + str(chances))
        elif g_num == num:
            print("Congratulations! You guessed the correct number in " + str(attempt) + " attempts")
            break
        attempt += 1
        chances -= 1
    else:
        print("Your failed too guess the number")
        print("Back to Main Menu")
        return main()
    

def dif_medium():
    chances = int(10)
    attempt = int(0)
    print("Your chances is " + str(chances))
    g_num = int(input("Enter your guess : "))
    while g_num != num & chances > 0:
        if g_num < num:
            g_num = int(input("Incorrect!! Your guess too low, guess again = "))
            print("Chance remeaning is " + str(chances))
        elif g_num > num:
            g_num = int(input("Incorrect!! Your guess too high, guess again = "))
            print("Chance remeaning is " + str(chances))
        elif g_num == num:
            print("Congratulations! You guessed the correct number in " + str(attempt) + " attempts")
            break
        attempt += 1
        chances -= 1
    else:
        print("Your failed too guess the number")
        print("Back to Main Menu")
        return main()
    

def dif_hard():
    chances = int(5)
    attempt = int(0)
    print("Your chances is " + str(chances))
    g_num = int(input("Enter your guess : "))
    while g_num != num & chances > 0:
        if g_num < num:
            g_num = int(input("Incorrect!! Your guess too low, guess again = "))
            print("Chance remeaning is " + str(chances))
        elif g_num > num:
            g_num = int(input("Incorrect!! Your guess too high, guess again = "))
            print("Chance remeaning is " + str(chances))
        elif g_num == num:
            print("Congratulations! You guessed the correct number in " + str(attempt) + " attempts")
            break
        attempt += 1
        chances -= 1
    else:
        print("Your failed too guess the number")
        print("Back to Main Menu")
        return main()
    

def main():
    print("Welcome to Guess The Number")
    name = str(input("Enter your name : "))
    print(name + ",You must guesss the number i think between 1 and 100")
    print("E = Easy(15 chances) M = Medium(15 chances) H = Hard(15 chances)")
    difficulty = input("Select your difficulty : ")

    if difficulty == "E" or difficulty == "e":
        dif_easy()
    elif difficulty == "M" or difficulty == "m":
        dif_medium()
    elif difficulty == "H" or difficulty == "h":
        dif_hard()
    else:
        print("Your option not available")
        return main()

main()

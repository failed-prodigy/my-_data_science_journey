import random


def game(number,guesses):
    continue_game = 0
    while continue_game <guesses  :
        guess = int(input(" Make a guess : "))
        if guess == number :
            continue_game = guesses
            return print ("You guessed correctly")
        elif guess < number :
            print("Your guess is low")
            continue_game +=1
        elif guess > number :
            print("Your guess is high")
            continue_game += 1

    print("You lost the game")
    return print(f"My number is : {number}")

print("""_______           _______  _______  _______    _______             _                 _______  ______   _______  _______ 
(  ____ \|\     /|(  ____ \(  ____ \(  ____ \  (       )|\     /|  ( (    /||\     /|(       )(  ___ \ (  ____ \(  ____ )
| (    \/| )   ( || (    \/| (    \/| (    \/  | () () |( \   / )  |  \  ( || )   ( || () () || (   ) )| (    \/| (    )|
| |      | |   | || (__    | (_____ | (_____   | || || | \ (_) /   |   \ | || |   | || || || || (__/ / | (__    | (____)|
| | ____ | |   | ||  __)   (_____  )(_____  )  | |(_)| |  \   /    | (\ \) || |   | || |(_)| ||  __ (  |  __)   |     __)
| | \_  )| |   | || (            ) |      ) |  | |   | |   ) (     | | \   || |   | || |   | || (  \ \ | (      | (\ (   
| (___) || (___) || (____/\/\____) |/\____) |  | )   ( |   | |     | )  \  || (___) || )   ( || )___) )| (____/\| ) \ \__
(_______)(_______)(_______/\_______)\_______)  |/     \|   \_/     |/    )_)(_______)|/     \||/ \___/ (_______/|/   \__/
                                                                                                                         """)
print ("Welcome to the Number Guessing Game! \n I'm thinking of a number between 1 and 100.")
difficulty = input("Choose your difficulty: Type 'easy' or 'hard' : ")
if difficulty == "easy":
    print("You chose easy. You got 10 guesses. ")
    guesses = 10
    my_number = random.randint(1,100)
    game(my_number,guesses)

elif difficulty == "hard" :
    print("You chose hard. You get 5 guesses. ")
    guesses = 5
    my_number = random.randint(1, 100)
    game(my_number,guesses)




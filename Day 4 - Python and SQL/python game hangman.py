import random

word_list = ["apple", "banana", "grapes", "mango", "strawberry"]
chosen_word = random.choice(word_list)
word_length = len(chosen_word)
display = ["_" for _ in range(word_length)]
lives = 6

print("Welcome to Hangman!")

while "_" in display and lives > 0:
    guess = input("Guess a letter: ").lower()
    
    if guess in display:
        print("You’ve already guessed that letter.")
        continue

    if guess in chosen_word:
        for index, letter in enumerate(chosen_word):
            if letter == guess:
                display[index] = guess
    else:
        lives -= 1
        print(f"Wrong guess. You have {lives} lives left.")

    print(" ".join(display))

    print("You win! 🎉")
else:
    print(f"You lost! The word was {chosen_word}")

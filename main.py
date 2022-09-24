# We need to pick random word from the list 
import random
import hangman_arts
import hangman_lists
from click import clear

print(hangman_arts.logo)

# every time get a random word from the hangman_list module
chosen_word = random.choice(hangman_lists.word_list)

# Testing code
print(f'Pssst, the solution is {chosen_word}.')

# create an empty list
display = []

# this is used to create the blank space as many as the chosen_word 
for i in range(len(chosen_word)):
    display.append("_")

user_life = 7
game_end = False

# This will loop until all the element are found or the all life are gone
while not game_end:
    guess = input("Guess a letter: ").lower()

    clear()

    if guess in display:
        print(f"You already guess the letter {guess} ")

    # check whether the user guess is in the word one by one
    for index in range(len(chosen_word)):
        letter = chosen_word[index]

        # if the user guess is correct then show the letter in correct position
        if letter == guess:
            display[index] = guess

    # we need to show the user how many they found
    print(f"{' '.join(display)}")

    # check whether the user guess is in the chosen word if not then minus the life by one
    if guess not in chosen_word:
        print(f"You guessed {guess} ,that's not in the word, you lose a life")
        user_life -= 1
        print(hangman_arts.stages[user_life])

        # if all the life has gone then they lose
        if user_life == 0:
            game_end = True
            print("You Lose")
            print(f"The actual answer is '{chosen_word}'")

    # if the user found all the letter before the life out then they win
    if '_' not in display:
        game_end = True
        print("You Won")

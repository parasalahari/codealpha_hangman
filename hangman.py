import random

words = ["apple", "banana", "orange", "grapes", "mango"]

secret_word = random.choice(words)

guessed_letters = []
incorrect_guesses = 0
max_attempts = 6

while incorrect_guesses < max_attempts:

    display_word = ""

    for letter in secret_word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "

    print("\nWord:", display_word)

    if "_" not in display_word:
        print("Congratulations! You guessed the word!")
        break

    guess = input("Enter a letter: ").lower()

    if guess in guessed_letters:
        print("You already guessed that letter!")
        continue

    guessed_letters.append(guess)

    if guess in secret_word:
        print("Correct!")
    else:
        print("Wrong!")
        incorrect_guesses += 1
        print("Attempts left:", max_attempts - incorrect_guesses)

if incorrect_guesses == max_attempts:
    print("\nGame Over!")
    print("The word was:", secret_word)
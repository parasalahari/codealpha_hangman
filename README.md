# codealpha_hangman
# 🎮 Hangman Game (Python)

A simple text-based Hangman game built using Python. The player tries to guess a randomly selected word one letter at a time before running out of attempts.

## 📌 Project Overview

This project is a beginner-friendly implementation of the classic Hangman game. The game selects a random word from a predefined list, and the player must guess the word one letter at a time. The player wins by correctly guessing all the letters before reaching the maximum number of incorrect attempts.

## ✨ Features

- Random word selection from a predefined list
- Letter-by-letter guessing
- Tracks guessed letters
- Maximum of 6 incorrect attempts
- Displays word progress using underscores (`_`)
- Win and lose conditions
- Simple console-based interface

## 🛠 Technologies Used

- Python
- Random Module
- Lists
- Strings
- While Loops
- Conditional Statements (if-else)

## 📂 Project Structure

```text
hangman-game/
│
├── hangman.py
└── README.md
```
## How to run
1.Install Python 3.
2.Download the hangman.py file.
3.Open a terminal in the project folder.
4.Run the command:python hangman.py

## 🎯 How to Play

1. The game randomly selects a word from a predefined list.
2. The word is displayed as underscores (`_`).
3. Enter one letter at a time.
4. Correct guesses reveal the letter's position in the word.
5. Incorrect guesses reduce the remaining attempts.
6. You have a maximum of 6 incorrect guesses.
7. Guess the entire word before running out of attempts to win.

## 📸 Sample Output

```text
Word: _ _ _ _ _
Enter a letter: a
Correct!

Word: a _ _ _ _
Enter a letter: p
Correct!

Word: a p p _ _
Enter a letter: l
Correct!

Word: a p p l _
Enter a letter: e
Correct!

Congratulations! You guessed the word!
```

## 📚 Learning Outcomes

Through this project, you will learn:

- How to use the `random` module
- Working with lists and strings
- Taking user input
- Using loops for repetition
- Implementing conditional logic
- Building simple game mechanics in Python

## 🔮 Future Enhancements

- Add multiple difficulty levels
- Load words from an external file
- Add Hangman ASCII art
- Include score tracking
- Allow multiple rounds
- Add hints for words
## Internship task
This project was completed sa apart of the python programming Internship at codeAlpha.

## 👩‍💻 Author

Parasa Lahari

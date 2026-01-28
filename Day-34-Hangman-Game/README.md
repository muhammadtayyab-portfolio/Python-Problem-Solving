# Day 34: Hangman Lite Game 🎮

A text-based version of the classic Hangman game where you guess letters to reveal a hidden word.

## 📝 Description
This program picks a random word from a predefined list and challenges the user to guess it one letter at a time. You start with 6 lives; every wrong guess costs you a life, while correct guesses reveal the letter's position in the word.

## 🛠️ Concepts Used
* **Random Module:** Used `random.randint` to select a secret word from the list.
* **Game Loop:** A `while True` loop manages the continuous flow of the game until a win or loss.
* **String Manipulation:** Using `.join()` to display the current state of the word with underscores and letters.
* **Input Validation:** Ensures the user only enters a single alphabetical character.
* **List Enumeration:** Used `enumerate()` to find all occurrences of a guessed letter in the target word.

## 🚀 How to Run
```bash
python main.py
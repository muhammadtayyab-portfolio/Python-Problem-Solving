import random

words = ["python", "hangman", "challenge", "programming", "flowchart"]

random_pick = words[random.randint(0,len(words)-1)]
lives = 6
blanks = ["_"] * len(random_pick)

print("Welcome to the game :")
print("Word to guess: "+" ".join(blanks))
print(f"You have {lives} lives.")

while True:
    guess = input("\nGuess a letter: ").lower()
    if len(guess) != 1 or not guess.isalpha():
        print("Please enter only a single letter.")
        continue
    if guess in random_pick:
        for i , word in enumerate(random_pick):
            if word == guess:
                blanks[i] = guess
        print("Good guess: " + " ".join(blanks))
        if "_" not in blanks:
            print("\n🎉 Congratulations! You guessed the word:", word)
            break 
    else:
        lives-=1
        print(f"Wrong guess. You lost a life. Lives left: {lives}")
    if lives == 0:
        print("\n💀 Game Over! The word was:", random_pick)
        break
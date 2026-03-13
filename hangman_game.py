import random

# List of predefined words
words = ["python", "computer", "program", "keyboard", "internet"]

# Select a random word
word = random.choice(words)

guessed_letters = []
wrong_guesses = 0
max_wrong = 6

print("Welcome to Hangman Game!")

# Loop until game ends
while wrong_guesses < max_wrong:
    
    display_word = ""
    
    # Show guessed letters
    for letter in word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "
    
    print("\nWord:", display_word)
    
    # Check if word is guessed
    if "_" not in display_word:
        print("🎉 Congratulations! You guessed the word:", word)
        break
    
    guess = input("Enter a letter: ").lower()
    
    if guess in guessed_letters:
        print("You already guessed this letter!")
    
    elif guess in word:
        print("Correct guess!")
        guessed_letters.append(guess)
    
    else:
        print("Wrong guess!")
        wrong_guesses += 1
        guessed_letters.append(guess)
        print("Remaining attempts:", max_wrong - wrong_guesses)

# Game over condition
if wrong_guesses == max_wrong:
    print("❌ Game Over! The word was:", word)

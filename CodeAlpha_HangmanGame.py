import random

# List of (word, hint) pairs
words_with_hints = [
    ('apple', 'It is a fruit.'),
    ('bread', 'It is a food item.'),
    ('chair', 'You can sit on it.'),
    ('plant', 'It grows in soil.'),
    ('zebra', 'A striped animal.')
]

# Randomly choose a (word, hint) pair
secret_word, hint = random.choice(words_with_hints)

# Game state variables
guessed_letters = []
incorrect_guesses = 0
max_guesses = 6
display_word = ['_' for _ in secret_word]

print("Welcome to Hangman with Hints!")
print("Guess the word, one letter at a time.")
print(f"Hint: {hint}")
print(f"You have {max_guesses} incorrect guesses.\n")

# Game loop
while incorrect_guesses < max_guesses and '_' in display_word:
    print("Word:", ' '.join(display_word))
    guess = input("Enter a letter: ").lower()

    if not guess.isalpha() or len(guess) != 1:
        print("Please enter a single letter.\n")
        continue

    if guess in guessed_letters:
        print("You already guessed that letter. Try again.\n")
        continue

    guessed_letters.append(guess)

    if guess in secret_word:
        print("Good guess!\n")
        for i in range(len(secret_word)):
            if secret_word[i] == guess:
                display_word[i] = guess
    else:
        incorrect_guesses += 1
        print(f"Wrong guess! You have {max_guesses - incorrect_guesses} guesses left.\n")

# Final result
if '_' not in display_word:
    print("Congratulations! You guessed the word:", secret_word)
else:
    print("Game Over! The word was:", secret_word)

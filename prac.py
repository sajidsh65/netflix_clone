import random

def get_random_word():
    words = ['python', 'hangman', 'programming', 'django', 'development']
    return random.choice(words)

def display_word(word, guessed_letters):
    return ' '.join(letter if letter in guessed_letters else '_' for letter in word)

def hangman():
    word = get_random_word()
    guessed_letters = set()
    attempts_left = 6
    guessed_word = set(word)

    print("Welcome to Hangman!")
    print("Try to guess the word.")
    
    while attempts_left > 0 and guessed_word:
        print("\nWord to guess:", display_word(word, guessed_letters))
        print(f"Attempts left: {attempts_left}")
        
        guess = input("Guess a letter: ").lower()
        
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.")
            continue
        
        if guess in guessed_letters:
            print("You already guessed that letter.")
            continue
        
        guessed_letters.add(guess)
        
        if guess in word:
            print(f"Good guess! '{guess}' is in the word.")
            guessed_word.discard(guess)
        else:
            print(f"'{guess}' is not in the word.")
            attempts_left -= 1
    
    if not guessed_word:
        print(f"Congratulations! You guessed the word: {word}")
    else:
        print(f"Game over! The word was: {word}")

if __name__ == "__main__":
    hangman()

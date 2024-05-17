import random

def choose_word():
    words = ["python", "coding", "computer", "csharp", "html", "javascript"]
    return random.choice(words)

def display_word(word, guessed_letters):
    display = ""
    for letter in word:
        if letter in guessed_letters:
            display += letter + " "
        else:
            display += "_ "
    return display

def play_game():
    word = choose_word()
    guessed_letters = []
    attempts = 6

    print("Welcome to the Word Guessing Game!")
    print("Try to guess the word.")

    while True:
        print("\n" + display_word(word, guessed_letters))
        print(f"Attempts left: {attempts}")
        guess = input("Guess a letter: ").lower()

        if guess in guessed_letters:
            print("You've already guessed that letter.")
        elif guess in word:
            guessed_letters.append(guess)
            if set(guessed_letters) == set(word):
                print("Congratulations! You've guessed the word:", word)
                break
        else:
            attempts -= 1
            print("Incorrect guess!")

        if attempts == 0:
            print("Out of attempts! The word was:", word)
            break

    play_again = input("Do you want to play again? (yes/no): ").lower()
    if play_again == "yes":
        play_game()
    else:
        print("Thanks for playing!")

if __name__ == "__main__":
    play_game()

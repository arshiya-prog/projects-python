import random
import words
import text

print(text.text)

word = random.choice(words.words_list)
blanks = []
word_list = list(word)

for i in word:
    blanks.append("_")

# blanks = "".join(blanks)

print(f"Word to guess: {"".join(blanks)}")

guesses = 6

print(word_list)

while(guesses != 0 and "".join(blanks) != word):
    letter_guess = input("\nGuess a letter: ")
    if letter_guess in word_list:
        for idx, char in enumerate(word_list):
            if char == letter_guess:
                blanks[idx] = word[idx]
    else:
        guesses = guesses - 1
        print(f"\nYou guessed {letter_guess}, that's not in the word. You lose a life!")
        print(f"\nLives left: {guesses}")
        
    if guesses == 6:
        print(text.l6)
    elif guesses == 5:
        print(text.l5)
    elif guesses == 4:
        print(text.l4)
    elif guesses == 3:
        print(text.l3)
    elif guesses == 2:
        print(text.l2)
    elif guesses == 1:
        print(text.l1)
    elif guesses == 0:
        print(text.l0)

    if guesses == 0 and blanks != word:
        print(f"\nYou couldn't guess the word. ")
    elif "".join(blanks) == word:
        print("".join(blanks))
        print("\nYou win!")

    print("".join(blanks))
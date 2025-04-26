import random

def load_words_and_hints(filename):
    words = []
    hints = []
    with open(filename, 'r') as file:
        for line in file:
            word, hint = line.strip().split(',')
            words.append(word)
            hints.append(hint)
    return words, hints

def jumble_word(word):
    word = list(word)
    random.shuffle(word)
    return ''.join(word)

def grade(total_points):
    if total_points >= 18:
        return 'A+'
    elif total_points >= 15:
        return 'A'
    elif total_points >= 12:
        return 'B+'
    elif total_points >= 8:
        return 'B'
    else:
        return 'C'

def play_game(words, hints):
    total_points = 0
    first_attempts = 0
    second_attempts = 0

    for i in range(len(words)):
        word = words[i]
        hint = hints[i]
        jumbled = jumble_word(word)
        
        print(f"\nJumbled Word: {jumbled}")
        guess1 = input("Your Guess: ").strip().lower()
        
        if guess1 == word:
            print("\U00002705 Correct!")
            total_points += 2
            first_attempts += 1
            continue
        
        print(f"CLUE: {hint}")
        guess2 = input("Take a second guess: ").strip().lower()
        
        if guess2 == word:
            print("\U00002705 Correct!")
            total_points += 1
            second_attempts += 1
        else:
            print("\U0000274C Incorrect!")  # Cross mark
    
    print("\n" + "-" * 30)
    print(f"Total Points     : {total_points}")
    print(f"First Attempts   : {first_attempts}")
    print(f"Second Attempts  : {second_attempts}")
    print(f"Overall Grade    : {grade(total_points)}")
    print("-" * 30)

# Example usage:
words, hints = load_words_and_hints('words_and_hints.txt')
play_game(words, hints)

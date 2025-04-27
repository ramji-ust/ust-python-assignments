import random

class GuessMyNumber:
    def __init__(self, lower=1, upper=100, max_attempts=10):
        self.lower = lower
        self.upper = upper
        self.max_attempts = max_attempts
        self.number_to_guess = random.randint(lower, upper)
        self.attempts = 0

    def get_user_guess(self):
        while True:
            try:
                guess = int(input("-> "))
                if self.lower <= guess <= self.upper:
                    return guess
                else:
                    print(f"Please enter a number between {self.lower} and {self.upper}.")
            except ValueError:
                print("Invalid input. Please enter a valid integer.")

    def play(self):
        print(f"Computer has chosen a number between {self.lower} and {self.upper}. Can you guess it? Max. {self.max_attempts} guesses!")

        while self.attempts < self.max_attempts:
            guess = self.get_user_guess()
            self.attempts += 1

            if guess < self.number_to_guess:
                print("Higher")
            elif guess > self.number_to_guess:
                print("Lower")
            else:
                print("Correct!!")
                print(f"\nNumber of attempts {self.attempts}/{self.max_attempts}")
                self.excellent_playing()
                break
        else:
            print("\nSorry, you've used all your guesses.")
            print(f"The number was {self.number_to_guess}. Better luck next time!")

    def excellent_playing(self):
        if self.attempts <= self.max_attempts // 2:
            print("Excellent playing!")
        else:
            print("Good job!")

# Create a game instance and play
if __name__ == "__main__":
    game = GuessMyNumber()
    game.play()

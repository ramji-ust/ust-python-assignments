import random

class GuessMyNumber:
    def __init__(self, min_num=1, max_num=100, max_attempts=10):
        self.min_num = min_num
        self.max_num = max_num
        self.max_attempts = max_attempts
        self.secret_number = random.randint(min_num, max_num)
        self.attempts = 0
        self.game_over = False

    def make_guess(self, guess):
        if self.game_over:
            return "Game over! Restart to play again."
        
        self.attempts += 1
        
        if guess < self.secret_number:
            return "Higher"
        elif guess > self.secret_number:
            return "Lower"
        else:
            self.game_over = True
            return f"Correct!!\nNumber of attempts {self.attempts}/{self.max_attempts}"

    def play(self):
        print(f"Computer has chosen a number ({self.min_num}, {self.max_num}), can you guess? Max. {self.max_attempts} guesses.")
        
        while self.attempts < self.max_attempts:
            try:
                guess = int(input("-> "))
                response = self.make_guess(guess)
                print(response)
                
                if "Correct" in response:
                    print("Excellent playing!")
                    break
            except ValueError:
                print("Please enter a valid number.")

        if not self.game_over:
            print(f"Game over! The number was {self.secret_number}.")

# Run the game
if __name__ == "__main__":
    game = GuessMyNumber()
    game.play()

import random
class GuessingGame:
    def __init__(self, name, min_num=1, max_num=100):
        self.name = name
        self.min_num = min_num
        self.max_num = max_num
        self.attempts = 0
        self.score = 1000 + (max-min)*10  # Initialize the score based on the range of numbers
        self.target_num = random.randint(self.min_num, self.max_num)

    def display_scores(self):
        try:
            with open('scores.txt', 'r') as f:
                print("Previous scores:")
                print(f.read())
        except FileNotFoundError:
            print("No previous scores found.")

    def save_score(self):
        scores = []
        try:
            with open('scores.txt', 'r') as f:
                for line in f:
                    name, score = line.strip().split(': ')
                    scores.append((int(score), name))
        except FileNotFoundError:
            pass

        scores.append((self.score, self.name))
        scores.sort(reverse=True)

        with open('scores.txt', 'w') as f:
            for score, name in scores[:5]:
                f.write(f"{name}: {score}\n")

    def play(self):
        self.display_scores()
        while True:
            try:
                guess = int(input(f"Guess a number between {self.min_num} and {self.max_num}: "))
                self.attempts += 1
                if guess < self.min_num or guess > self.max_num:
                    print("Out of bounds! Please try again.")
                elif guess < self.target_num:
                    print("Too low! Try again.")
                elif guess > self.target_num:
                    print("Too high! Try again.")
                else:
                    # display a winning message with ansii art using unicode characters
                    print(f"Congratulations, {self.name}! You've guessed the number in {self.attempts} attempts.")
                    print(" \U0001F389 \U0001F389 \U0001F389")
                    self.score = 1000 - self.attempts * 10  
                    self.save_score()  # Save the score to a file

                    play_again = input("Do you want to play again? (yes/no): ")
                    
                    if play_again == 'yes':
                        self.target_num = random.randint(self.min_num, self.max_num)
                        self.attempts = 0
                        1000 + (max-min)*10  # Initialize the score based on the range of numberss
                        continue
                    else:
                        print("Thanks for playing!")
                        break      
            except ValueError:
                print("Invalid input! Please enter a number.")

def read_int(prompt):
        while True:
            try:
                num = int(input(prompt))
                if(num <= 0):
                    print("Please enter a valid number greater than 0")
                else:
                    return num
            except ValueError:
                print("That's not a valid integer. Please try again.")


if __name__ == "__main__":
    name = input("Please enter your name: ")
    min = read_int("Please enter the minimum number : ")
    max = read_int("Please enter the maximum number: ")
    while  min >= max:
        print("Please enter valid numbers. The min should be less than max and both should be greater than 0")
        max = read_int("Please enter the maximum number: ")
    game = GuessingGame(name, min, max)
    game.play()
print("Enter the integer for the player to guess.")
integer = int(input())
print("Enter your guess.")
guess_answer = integer
num_tries = 1
guess = int(input())
while guess != guess_answer:
    if guess > guess_answer:
        print("Too high - try again:")
    else:
        print("Too low - try again:")
    guess = int(input())
    num_tries += 1
print("You guessed it in",num_tries,"tries")

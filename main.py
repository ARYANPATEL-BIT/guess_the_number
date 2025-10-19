import random

guess = True
chances = 5
tries = 0

while guess:

    user = int(input("Guess a number (1-100): "))
    computer = random.randint(1,100)

    if user > computer :

        chances -=1
        tries += 1
        print("Too High! Guess Lower")
        print(f"{chances} left!")
    elif user < computer:

        chances -= 1
        tries += 1
        print("Too Low! Guess Higher")
        print(f"{chances} left!")
    elif user == computer:

        print(f"🎉Correct! You got it in {tries} tires!")
    if chances == 0:
        guess = False
        print("You lost! Better Luck next Time!")
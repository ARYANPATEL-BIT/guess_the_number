import random

guess = True
chances = 10
tries = 0
computer = random.randint(1,100)

while guess:

    try:
        user = int(input("Guess a number (1-100): "))
    except ValueError:
        print("❌ Enter a number!")
        continue

    if user > computer :
        chances -=1
        tries += 1
        print("Too High! Guess Lower")
        print(f"{chances} chances left!")

    elif user < computer:
        chances -= 1
        tries += 1
        print("Too Low! Guess Higher")
        print(f"{chances} chances left!")

    else:
        tries += 1
        print(f"🎉Correct! You got it in {tries} tires!")
        guess = False

    if chances == 0:
        guess = False
        print("You lost! Better Luck next time!")
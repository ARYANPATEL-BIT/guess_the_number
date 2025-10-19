import random



def guess_The_Number():
   computer = random.randint(1,100)
   tries = 0
   guess = True

   while True:
      level = input("Choose difficulty (easy/medium/hard): ").lower()
      if level == "easy":
         chances = 10
         break
      elif level == "medium":
         chances = 7
         break
      elif level == "hard":
         chances = 5
         break
      else:
         print("❌ Enter a vaild command (easy/medium/hard)!")

   while guess:
     try:
        user = int(input("Guess a number (1-100): "))
     except ValueError:
        print("❌ Enter a number!")
        continue

     if user < 1 or user > 100:
        print("⚠️ Enter a number between 1 and 100!")
        continue

     if user > computer and abs(user - computer) <= 5 and user != computer :
        chances -=1
        tries += 1
        print("🔥 You're very close!")
        print(f"{chances} chances left!")
    
     elif user > computer and abs(user - computer) > 5 :
        chances-=1
        tries += 1
        print("Too High! Choose Lower")
        print(f"{chances} chances left!")

     elif user < computer and abs(user - computer) <= 5 and user != computer :
        chances -= 1
        tries += 1
        print("🔥 You're very close!")
        print(f"{chances} chances left!")

     elif user < computer and abs(user - computer) > 5 :
        chances -= 1
        tries += 1
        print("Too Low! Guess Higher")
        print(f"{chances} chances left!")

     elif user == computer and tries + 1 < 3:
        tries += 1
        print(f"🎉Genius! You nailed it fast! You got it in {tries} tires!")
        guess = False

     else :
        tries += 1
        print(f"🎉Congratulation!You guessed the number in {tries} tries!")
        guess = False

     if chances == 0:
        guess = False
        print(f"So close! The number was {computer}.")
     
     
   score = tries *  10
   print(f"Your final score: {score}")




while True: 
   guess_The_Number()
   play_again = input("Play Agian? (Y/N):").lower()
   if play_again != "y":
      print("Thanks for playing! 👋")
      break
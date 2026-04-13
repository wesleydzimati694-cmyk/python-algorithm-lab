while True:
       guess = int(input("Guess a number: "))
       if guess < "target":
           print("Too Low.")
       elif guess > "target":
           print("Too High.")
       else:
           print("You win!")
           break
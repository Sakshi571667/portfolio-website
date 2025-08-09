import random

while True:
    print("Welcome to the number Guessing Game")
    print("I have choosen a number between 1 to 50")
    print("Can you guess it? Let's find out")
    
    #Generate a random number
    def play_game():
    secret_number = random.randint(1,50)

    #Initialize variables
    guess=0
    attempts=0

    #game loop
    while guess != secret_number:
        guess = int(input("Enter your guess:"))
        attempts +=1

        if guess<secret_number:
            print("Too low! Try again")
        elif guess>secret_number:
            print("Too high! try again")
        else:
            print("Congratulations! You guessed the number correctly")
            print(f"It took you {attempts} attempts.")
            print("Thanks for playing")

            #main loop to ask replay
            while True:
              play_game()
              play_again = input("\nDo you want to play again? (yes/no): ").lower()
              if play_game != "yes":
                  print("Thank you")
                  break

    

    
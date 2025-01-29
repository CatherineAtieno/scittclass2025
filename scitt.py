import random

def guess_the_number():
    secret_number=random.randint(1,10)
    attempts=0
    print("welcome to the number guessing game")
    print("I'm thinking of a number between 1 and 10.")
    
    while True:
        user_input=input("Enter your guess:")

        if not user_input.isdigit():
            print("Invalid input! Please enter a number.")
            continue
        guess=int(user_input)
        attempts += 1

        if guess< secret_number:
            print ("Too low! Try again")
        elif guess > secret_number:
            print ("Too high! Try again")
        else:
          print (f"Congratulations! You have guessed the number in {attempts} attempts.")  
          break
        print ("thank you for playing the number guess game ")
        
guess_the_number()

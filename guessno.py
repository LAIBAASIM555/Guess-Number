import random

print("""
    ____     _   _ U _____ u ____    ____          _   _       _   _   __  __     ____  U _____ u   ____     
U /"___|uU |"|u| |\| ___"|// __"| u/ __"| u      | \ |"|   U |"|u| |U|' \/ '|uU | __")u\| ___"|/U |  _"\ u  
\| |  _ / \| |\| | |  _|" <\___ \/<\___ \/      <|  \| |>   \| |\| |\| |\/| |/ \|  _ \/ |  _|"   \| |_) |/  
 | |_| |   | |_| | | |___  u___) | u___) |      U| |\  |u    | |_| | | |  | |   | |_) | | |___    |  _ <    
  \____|  <<\___/  |_____| |____/>>|____/>>      |_| \_|    <<\___/  |_|  |_|   |____/  |_____|   |_| \_\   
  _)(|_  (__) )(   <<   >>  )(  (__))(  (__)     ||   \\,-.(__) )(  <<,-,,-.   _|| \\_  <<   >>   //   \\_  
 (__)__)     (__) (__) (__)(__)    (__)          (_")  (_/     (__)  (./  \.) (__) (__)(__) (__) (__)  (__) 
      """)

print("Lets play guessing number game!")
print("What level you want to choose 'Easy','Hard'")

difficulty = input("Enter your choice: ")

number = random.randint(1, 100)
print("User have to guess number b/t 1 to 100")

if difficulty.lower() == "easy":
    turns = 10
    print("You have 10 attempts to guess a number")
else:
    turns = 5
    print("You have 5 attempts to guess a number")

attempts = 0
while attempts < turns:
    try:
        num = int(input("Enter your guess: "))
        if num < 1 or num > 100:
            print("Please enter a number between 1 and 100.")
            attempts += 1
            print(f"{turns-attempts} turns are left")
        elif num == number:
            print("Congratulations! You guessed the number.")
            print(f"Guess Number is {number}")
            break
        elif num > number:
            print("Too high, try again!")
            attempts += 1
            print(f"{turns-attempts} turns are left")
        else:
            print("Too low, try again!")
            attempts += 1
            print(f"{turns-attempts} turns are left")
    except ValueError:
        print("Invalid input, please enter a number.")
        attempts += 1
        print(f"{turns-attempts} turns are left")

if attempts == turns:
    print("You ran out of turns. The number was {}.".format(number))
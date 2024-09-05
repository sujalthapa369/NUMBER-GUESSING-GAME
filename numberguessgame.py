import random
import logonum
print(logonum.logo)
EASY_ATTEMPTS = 10
HARD_ATTEMPTS = 5
print("Let me think of a number ranging from 1 to 50: ")
answer = random.randint(1,50)
level = input("\nChoose the level of difficulty: TYPE: ('Easy or Hard')): ").lower()
if(level == "easy"):
    x =  EASY_ATTEMPTS
    attempts = x
elif(level =="hard"):
    y =  HARD_ATTEMPTS
    attempts = y
guess_num=0
while( guess_num!=answer ):
    if(attempts==0):
        print("You lose! You are out of guesses")
        break;
    
    print(f'\nYou have {attempts} attempts remaining to guess the number')
    guess_num = int(input("\nGuess a number:"))
    if(guess_num>answer):
        print("\nNumber is too high")
        attempts = attempts - 1
       
    elif( guess_num==answer):
        print(f"\nYou have guessed the correct answer.. The answer was {answer}")

    else:
        print("\nNumber is too low")
        attempts = attempts - 1
       















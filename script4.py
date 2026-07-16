import random
lowest=0
highest=100
guesses=0
is_running=True
answered=0
answer=random.randint(lowest,highest)
print("Welcome to the python number guessing game")
while is_running and guesses<=9:
         guess=input("Guess the secret number(It's between 0 and 100)")

         if  guess.isdigit() :
             guess=int(guess)
             if guess<lowest or guess>highest:
                 print("Please enter a number between 0 and 100")

             if guess==answer:
                 print("You guessed correctly!")
                 answered=1
                 guesses+=1
                 print(f"you guessed {guesses} times")
                 break
             else:
                 print("try again")
                 if -10<guess-answer<10:
                     print("You're pretty close")
                     guesses+=1
                 else:
                     guesses+=1
                     pass
         else:
             print("Please enter a number")




if guesses>9 and answered==0:
    print("you failed to guess the number")
print(f"The answer was {answer}")
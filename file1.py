import random

comp = random.randrange(1,10)
user = int(input("Guess number 1-9: "))
print("Computer guessed: ", comp)

if comp > user:
    print("Computer wins!")
elif user > comp:
    print("User wins!")
else: 
    print("Draw")
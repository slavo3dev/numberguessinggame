import random

print("Guess a number from 1 to 10!!!")
print("******************************")
def game():
    a = input("Please enter a number: ")
a = int(a)
game()
b = random.randint(1, 10)

if (a == b):
    print("You are a winner your number is ", a)
else:
    print("Please try again")
    game()


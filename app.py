import random

print("Guess a number from 1 to 20!!!")
print("******************************")
print("You will have tree  opportunities")
a = input("Eneter a number: ")
a = int(a)
b = random.randint(1, 20)
def game():
    if (a == b):
        print("You are a Winner your number you guess is:  ", b)
    elif(b > 10):
        print("Number is bigger then 10 please try again")
        c = input("Try again, Enter a number: ")
        c = int(c)
    elif(b < 10):
        print("Number is smoller then 10 please try again")
        c = input("Try again, Enter a number: ")
        c = int(c)
    elif (c == b):
        print ("Well Done, you did it!!! Hidden number is: ", b)
    elif (b > 15):
        print("Number is bigger then 15 please try again")
        d = input("Last try, eneter a number: ")
        d = int(d)
    elif (b < 5):
        print("Number is  smoller then 15 please try again")
        d = input("Last try, eneter a number: ")
        d = int(d)
    elif ( b > 5 and b < 15):
        print("Number is  bigger then 5 but smaller then 15")
        d = input("Last try, eneter a number: ")
        d = int(d)
    elif (d == b):
        print("Great, You did it!!Well Done! Hidden number is: ", b)
    else:
        print ("Try again... don't give up! Hidden number is: ", b)
game()



    


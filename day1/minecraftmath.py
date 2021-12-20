import random
from typing import Match

#list of actions that can be done to flavour it minecraft like
verbNounItem = (
    {
        "verb": "chop",
        "noun": "tree",
        "item": "sapling"
    },{
        "verb": "shear",
        "noun": "sheep",
        "item": "wool"
    },{
        "verb": "milk",
        "noun": "cow",
        "item": "milk"
    },{
        "verb": "dig",
        "noun": "iron",
        "item": "iron ore"
    }
)
randomNumber = random.randrange(len(verbNounItem))
verb = verbNounItem[randomNumber]["verb"]
noun = verbNounItem[randomNumber]["noun"]
item = verbNounItem[randomNumber]["item"]

def addMC(a,b):
    correctAnswer = int(a) + int(b)
    playerAnswer = int(input(f"You have {a} {item}. You {verb} a {noun} and get {b} more {item}. How many {item} do you have?\n"))
    if (playerAnswer == correctAnswer): 
        print("You're right!")
    else: 
        print(f"Better luck next time. The correct answer was {correctAnswer}")

def takeMC(a,b):
    a = int(a)
    b = int(b)
    if (a<b):
        c = a
        a = b
        b = c
    correctAnswer = int(a) - int (b)
    if correctAnswer < 0:
        correctAnswer = 0
    playerAnswer = int(input(f"You have {a} {item}. A sneaky creeper blows up {b} {item}! How many {item} do you have left?\n"))
    if (playerAnswer == correctAnswer): 
        print("You're right!")
    else: 
        print(f"Better luck next time. The correct answer was {correctAnswer}")

print("Welcome to Minecraft math")
num1 = input("Enter a number between 1 and 10: ")
num2 = input("Enter a second number between 1 and 10: ")
operator = input("What are we doing?\n" +
                 "Adding? (+)\n" +
                 "Taking away? (-)\n" +
                 "Type + or - please:\n")


if (operator == "+"): addMC(num1,num2)
if (operator == "-"): takeMC(num1,num2)

print("Thanks for playing!")


    



# city = input("What's city did you grow up in?\n")
# pet = input("What's the name of your pet?\n")
# print("Your band's name could be: " + city + " " + pet)
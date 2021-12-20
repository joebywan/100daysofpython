print("Welcome to the tip calculator!")
bill = int(input("What was the total bill? "))
inCorrect = True
while(inCorrect):
    tipPercentage = int(input("How much tip would you like to give? 10, 12, or 15? "))
    if (tipPercentage in(10,12,15)):
        inCorrect = False
    tipPercentage = float(tipPercentage/100)
numberOfPeople = int(input("How many people to split the bill?"))
billSplit = (bill + (bill*tipPercentage))/numberOfPeople
print(f"Each person should pay: ${billSplit}")
import random

firsts = ["cauliflower","tilapia fillet","pork loin", "green beans","rainbow carrots","potatoes","three color squash","eggplant","eye round of beef","baguette"]#first list of menu items
seconds = [" with balsamico", " with garlic olives"," with minted yogurt", " with soup", " with chutney", " with salad", " with salsa", " over sticky rice", " au jus", " with basmati rice"]#second list of menu items
first_costs = ["2", "8", "10","5", "4", "3", "6", "5", "9", "2"]#first list of costs that correspond with first menu list
second_costs = ["2","3", "2", "4","5", "7", "3", "5", "9","5"]#second list of costs that correpsond with second menu list

while True:#loop which allows "try" to be an infinite loop as long as user inputs a number 
    try:#try this
        number_of_items = int(input("Number of items? "))#computrer asks user for number of items
        break#loop is broken
    except ValueError:#anything but a number
        print("Enter an integer!")#computer will say this if the user responds with anything but a number

for i in range(number_of_items):#index in range for number of items
    print(f"{random.choice(firsts)} {random.choice(seconds)}")#print a random choice from first list and random choice from second list together


'''
Author: Caroline Muzzio
Date: 11/06/2023
Description: Allows user to interact with a series of prompts which recreates my morning routine
Challenges: User errors addressed via while loops and input string conversions to lowercase
Bugs: None
Sources: https://www.w3schools.com/python/python_conditions.asp
'''

print ("Alarm!")

while True:
    snooze= str.lower (input("Snooze?"))

    if snooze=="yes":
        print ("go back to sleep for 10 minutes")
    elif snooze=="no":
        print ("wake up")
        break
    else:
        print("Invalid")
        
while True:
    brush= str.lower (input("do you want to brush your teeth?"))

    if brush== "no":
        print ("thats disgusting!")
        break 
    elif brush== "yes":
        print("good job you are now clean!")
        break 
    else:
        print ("Invalid response")

while True:
    shower= str.lower (input("do you want to take a shower?"))

    if shower== "no":
        print("you will smell!")
        break
    elif shower== "yes":
        print ("you are clean for the day!")
        break
    else:
        print("Invalid response")

while True:
    eat_breakfast= str.lower (input("do you want to eat breakfast?"))

    if eat_breakfast=="no":
        print("you will starve")
        break
    elif eat_breakfast=="yes":
        print ("you are ready for the day!")
        break
    else:
        print ("invalid response")
        break
while True:
    raining= str.lower (input("is it raining?"))

    if raining== "no":
        print ("dont bring jacket!")
        break
    elif raining=="yes":
        print ("bring jacket")
        break
    else:
        print ("invalid response")

while True:
    school= input ("do you want to go to school?")

    if school== "no":
        print("your mom will be mad")
        break
    elif school== "yes":
        print ("you have to leave now!")
        break
    else:
        print ("invalid response")
    

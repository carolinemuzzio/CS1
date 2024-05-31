'''
Author: Caroline Muzzio
Date: 11/06/2023
Description: Allows user to interact with the computer as a magic 8 ball
Challenges: 
Bugs: None
Sources: https://www.w3schools.com/python/python_conditions.asp
'''
import random #DOCUMENTATION

while True:
    question = input("What would you like to ask the magic 8-ball? Enter stop to end:")# prompts user to enter a question for the magic 8 ball
    
    responses = ["Absolutely yes","Definitely not","Possibly"] #creates a list of possible responses

    if question == "stop": #if the user enters stop         
        break #then the program is over and stops looping

    elif "?" in question:# if a question mark is used then a random response is given by the computer
        print(random.choice(responses)) #print a random response from the list of possible responses
    else: #otherwise if the user enters anything else
        print("Not a question") #anything else that does not include a question will be responded to by not a question





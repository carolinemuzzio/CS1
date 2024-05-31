'''
Author: Caroline Muzzio
Date: 11/29/2023
Description: Allows user to interact with the computer playing rock paper and scissors
Challenges: Keeping score over multiple games
Bugs: None
Sources: https://www.w3schools.com/python/python_conditions.asp
'''

import random
import sys

rpslist= ["rock","paper","scissors"]#the rock paper scissors list
user_score = 0#the user score starts at 0
bot_score = 0#the computer score starts at 0
score_limit = 5# the score limit is 5

while True:
    while user_score < score_limit and bot_score < score_limit: #the score limit is greater then both the computer and the user
        user_rps = str.lower(input("Rock, paper, or scissors? Enter stop to end: "))#asking the user if they want to play rock, paper, and scissors 

        if user_rps == "stop": #if the user enters stop then the code will end 
            sys.exit() #the code will stop looping

        if user_rps not in rpslist: #if anything but rock, paper, scissors is inputted then it will say invalid response
            print("Invalid option")#this will be printed
        else:
            bot_rps = random.choice(rpslist)#the computer will input a random choice from the list

            if user_rps == bot_rps:#if both of the computer and bot input the same thig then it will be a tie
                print("it is a tie!")#this will be inputted
            elif user_rps =="rock" and bot_rps == "scissors":# user says rock and the bot says scissors
                print("user wins!")#the user will win and it will say that the user won
                user_score += 1 #1 point will be added to the user score
            elif user_rps=="rock" and bot_rps=="paper":# user says rock and the bot says paper
                print("bot has won!")#the computer will win and it will say this
                bot_score +=1#1 point will be added to the computers score
            elif user_rps=="paper" and bot_rps=="rock":#the user says paper and the computer says rock
                print ("bot has won!")#the computer has won and this will be inputed
                bot_score +=1# 1 point will be added to the computers score
            elif user_rps=="paper" and bot_rps=="scissors":#the user says paper and the computer says scissors
                print("user wins!")#the computer has won
                user_score +=1#1 point was added to the users score
            elif user_rps=="scissors" and bot_rps=="paper":#the user says scissors and the computer says paper
                print("user wins!")#the computer has won
                user_score +=1#1 point will be added to the users score
            elif user_rps== "scissors" and bot_rps== "rock":#the user has said scissors and the computer says rock
                print ("bot has won!")#the computer has won so this will be inputed
                bot_score +=1#1 point will be added to the computers score
            print(f"Score is: user - {user_score} | bot - {bot_score}")#the score will be diplayed after every answer from the computer

            if user_score or bot_score >= score_limit:# if one of the scores is more then the score limit
                if user_score > bot_score:#if the user score is more then the computer score
                    print("You won this round!")#this will be printed when the user wins
                elif bot_score > user_score:#if the computer score is more then the user score
                    print("Bot won this round!")#this will be printed if the computer wins
                else:#this will be a tie
                    print("This round was a tie!")#the round will be a tie so this will be displayed at the end of the round

    while True:
        play = input("Play again? ")#this question will be inputed at the end of the game when someone wins

        if play == "yes":#if the player says yes then the score will be reset
            user_score = 0#the user score will be reset to 0
            bot_score = 0#the bot score will be reser to 0
            break#the loop breaks
        elif play == "no":#if the user says no then the game will end
            sys.exit()#the code will end and NOT restart
        else:#anything byt yes or no
            print("Invalid")#if the user inputs anything but yes or no then invalid will be printed

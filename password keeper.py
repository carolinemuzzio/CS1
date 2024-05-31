'''
Author: Caroline Muzzio
Date: 5/9/24
Description: An code where the user can interact with the computer by entering websites usernames and passwords to gain access
Challenges: None
Bugs: None
Sources: W3 Schools, Ms. Marciano
'''

import random#import random choices
import sys#system control

def add_entries(websites, usernames, passwords):#function about adding entries
    while True:#loop
        website=input("Enter website (or type 'done to finish):")#input this for website

        if website.lower()=='done':#if user inputs done
            break#code will break
        username=input("Enter username for "+website+":")#printed for username
        password=input("Enter password for "+website+":")#printed for password

        websites.append(website)#add website to list
        usernames.append(username)#add username to list
        passwords.append(password)#add password to lst
def main():
    websites=[]#empty website list
    usernames=[]#empty username list
    passwords=[]#empty password list

    add_entries(websites, usernames, passwords)
    while True:
        mode = input("Which would you like: 1. Add entry, 2. Print all, 3. Print specific, 4. Exit")#user inputs a specific number which asks if they want to print all of the sequences or just specific one

        if mode == '4':
            break
        elif mode=="1":#if the user inputs 1
            add_entries(websites, usernames, passwords)
        elif mode == '2':
            for i in range(len(usernames)):#print the usernames in order
                print(f'''usernames:{usernames[i]} usernames: {usernames[i]} password:{passwords[i]}''')
                
        elif mode=="3":
            website=input("Enter a website: ")
            if website in websites:#if the website is in the websites list
                i=websites.index(website)#print that website and all the other options in order below it
                print(f'''\website: {websites[i]}
            username: {usernames[i]}
            passwords: {passwords[i]}''')
        else:
            print("That is not a valid option")

main()



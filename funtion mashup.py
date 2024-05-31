'''
Author: Caroline Muzzio
dDate: 4/23/24
Description: A mix of many different functions mashed into one
Challenges: None
Bugs: None
Sources: W3 Schools, Ms. Marciano
'''
def chorus():
    print ("Twinkle, twinkle, little star,")#print this when running code
    print ("How I wonder what you are!")#print this when running code
    
def sing (): #define sing in the print statements below
    chorus()#repeat this as its chorus
    print("Up above the world so high,")#print when running code
    print("Like a diamond in the sky.")#print when running code
    chorus ()#repeat this as its chorus

sing()#this has been defined above

x=input("Type a number: ")#x is first input asking to type a number
y=input("Type another number: ")#y is second input asking to type a number

sum=int(x)+int(y)#add x and y together to get the sum of the two

print ("The sum is:", sum)#print this statement along with the final sum

fruits=['apple','banana','cherry']#list of fruits
for item in fruits:#if the item is in the list of fruits
    print(item)#print the item

colors= ['red','blue','orange','yellow']#list of colors
if 'red' not in colors:#if the color red is not in the list (loop)
    print("Element not found")#print this if not found in list
else:#if top statement is not true try this
    print("Element found")#print element found if it is in the list

def is_number(number):#define number
    if number.isnumeric():#if the number is numeric
        return True#return as true
    else:#if the above is not true
        return False#return false
number="5"#the number is 5
print(is_number(number))#print is number

import random#random choice
def randomnumber():#define the random number
    low=input("Lower Limit:")#for low input lower limit
    high=input("Upper Limit:")#for high input upper limit
    while True:#while this loop is true
        if not is_number(low):#if the number is not low do the following
            print("error")#print error
        if is_number(low):#if number is low
            continue#continue loop
        else:#if the above is not true
            break#break code
    while True:#while this loop is true
        if isnumber(high):#if number is high
            continue#continue running code
        else:#if the above is not true
            break#break code

    return random.randit(int(low),int(high))#return random low int and high int



def replace_character (string,old_ch,new_ch):#define replace character
    new_string=""#new string
    for s in string:#for s in string do the following
        if s==old_ch:#if s is old character
            new_string+=new_ch#new string add new character
        else:#if the above is not true
            new_string+=S#new string capital S
    return new_string#return the new output
print(replace("hello world", "l", "a"))#replace these elements in the function

    

from santa_claus import santa_claus_ascii
import time
import json

with open('guests.json') as file:
    guests = json.load(file)

#Maybe the easiest way (?) to play sound that will work 
#for all Windows users without the need of installing a module
from os import system
system("start /MIN /B 12DaysOfChristmas.mp3")


## intro
print(f"""
{santa_claus_ascii}
Velkommen til Winter Warriors Julebord 2022!

Time: 18:00, 16th of December 2022

Sted: Amars place (Address TBD)

Dresscode: "Julebordspent" / suit / dress

Food: TBD

** PS: BYOB! **

""")

## asks for users name
name = input("""
********************************************************************
Please enter your first name: """).lower()

# legg inn loading screen
time.sleep(1)

print(f"""
********************************************************************
Hi, {name.capitalize()}! 

This is your current RSVP status of the Julebord: {guests[name]}""")

time.sleep(1)
change_rsvp = input("Do you want to change your RSVP status? (Y / N): ").lower()


if change_rsvp == 'y':

    while True:
        new_rsvp = input("""
        ********************************************************************
        Please chose one of the following options:
        A) Yes! :D
        B) No :(
        C) Maybe :|
        
        Please enter the letter (A, B or C) of your new RSVP status: """).capitalize()


        if new_rsvp == 'A':
            guests[name] = 'Yes! :D'
            break
        if new_rsvp == 'B':
            guests[name] = 'No :('
            break
        if new_rsvp == 'C':
            guests[name] = 'Maybe :|'
            break
        
        else:
            print("""
            ********************************************************************
            Input not valid. Please try again: """)
            continue

    print(f"Your new RSVP status is: {guests[name]}")
    with open('guests.json', 'w') as file:
        json.dump(guests, file)



elif change_rsvp == 'n':
    print(f"""
    ********************************************************************
    Thats okay! 
    
    Your current RSVP status is still: {guests[name]}""")


import colorama
from colorama import Fore, Back, Style
from dir.slowtext import slow_text_centered
import time 
import sys
import random
import shutil 
import os 


def clear_screen():
     os.system('cls')

colorama.init() # Initialise colorama incase it bugs out 

colour_text_menu = Fore.CYAN + Style.BRIGHT + Back.LIGHTWHITE_EX # Series of settings for the starting menu


def prnt_below(text):
    terminal_size = shutil.get_terminal_size()
    width = terminal_size.columns
    horizontal_padding = (width -len(text)) // 2
    print(" " * horizontal_padding + text)

print(slow_text_centered(colour_text_menu))

clear_screen()

slow_text_centered("Welcome to Hyperia", newLine = True, vertical_padding = True)
slow_text_centered("This is an island with infinite problems with solutions only you can solve!", newLine = True, vertical_padding = False)
slow_text_centered("Enter play to continue OR quit to exit: ", newLine = True, vertical_padding = False)
menu_choice = input(">").lower()

if menu_choice == 'play':
    clear_screen()
    print(art)
    time.sleep(3)
elif menu_choice == 'exit':
    clear_screen()
    slow_text_centered("Goodbye see you next time!", newLine = True, vertical_padding = True)
    time.sleep(5)
    close()

clear_screen()
slow_text_centered("Welcome to Hyperia!", newLine = True)
slow_text_centered("What is your name?", newLine = True, vertical_padding = False)
name = input(">").strip().capitalize()

clear_screen()
slow_text_centered(f"Nice to meet you {name},", newLine = True, vertical_padding = True)
slow_text_centered("My name is the GameMaster you can call me GM for short", newLine = True, vertical_padding = False)
clear_screen()
slow_text_centered(f"So {name} i've heard your quite the fighter", newLine = True, vertical_padding = True)
slow_text_centered("Your device activity shows that your into very intensive fights", newLine = True, vertical_padding = False)
slow_text_centered("Dont worry in Hyperia we have quite the challengers for you", newLine = True, vertical_padding = False)
slow_text_centered("First off your going to have to pick a class", newLine = True, vertical_padding = False)

classes = {

"Beserker": {
    "health": 100,
    "attack_speed" : 70,
    "mana" : 20,
    "damage" : 30,
    "agility": 40
},

"Mage": {
    "health": 70,
    "attack_speed": 50,
    "mana": 80,
    "damage": 40,
    "agility": 75
},

"Tank": {
    "health": 200,
    "attack_speed": 30,
    "mana": 20,
    "damage": 25,
    "agility": 30

},

"GM": {
    "health": 1000,
    "attack_speed": 9999,
    "mana": 9999,
    "damage": 9999,
    "agility": 9999

}
}

clear_screen()
slow_text_centered("These are your choices below", min_delay=0.02, max_delay=0.08, newLine = True, vertical_padding = True)
slow_text_centered("Beserker, a combat heavy class with fast attacks, though you will not be wise...", min_delay=0.02, max_delay=0.08, newLine = True, vertical_padding = False)
slow_text_centered("Mage, filled with magic and knowledge. Mana overflows from you. You will be cursed with a short life.,,", min_delay=0.02, max_delay=0.08, newLine = True, vertical_padding = False)
slow_text_centered("Tank, nothing can stop you. You have a heart made of iron and a body made of steel. Though your quite slow...", min_delay=0.02, max_delay=0.08, vertical_padding = False)
slow_text_centered("ERROR 404: CLASS NOT AVAILABLE FOR /-/=-/ BEEP Challenger you must think out the box for this class", min_delay=0.02, max_delay=0.08, newLine=True, vertical_padding = False)
slow_text_centered("So challenger what will be your choice?", min_delay=0.02, max_delay=0.08, newLine = True, vertical_padding = False)

player = (input(">")).strip().capitalize()
clear_screen()
while True:

    if player != 'GM':
        break

    if player == 'GM':
        encrypt = input("Who is the GM?: ")
        if encrypt == 'axinesky':
            slow_text_centered("You have obtained the GM class")
            break
        else: slow_text_centered("Wrong, restart your game to select a new class disappointing..")
        break
    else:
        slow_text_centered("Invalid input")
        break


print(player)
player = classes[player]

clear_screen()


slow_text_centered("Now you chose your class lets actually spawn your character shall we?", min_delay=0.02, max_delay=0.08, newLine = False, vertical_padding = True)
clear_screen()
menu_text = """
===================
     Hyperia Menu
===================

    -> 1. Profile
    -> 2. Inventory
    -> 3. Location
    -> 4. Quests
    -> 5. Resume Game
    -> 6. Exit Game
"""
def menu_screen():
    clear_screen()
    slow_text_centered(menu_text, min_delay=0.04, max_delay=0.12 ,newLine = False, vertical_padding = True)

slow_text_centered("*poof**", min_delay=0.02, max_delay=0.08, newLine = False, vertical_padding = True)

#fix up in the morning

#user_profile = {
#    "name": name,
#    "class": classes.copy(),
#
#}

#print(user_profile)
#def profile():
#       clear_screen()

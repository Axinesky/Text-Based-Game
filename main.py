import colorama
from colorama import Fore, Back, Style, Cursor
from dir.slowtext import slow_text_centered,text_centered_block
from dir.dicts import enemy
import time
import os
import sys
import shutil
import copy
import json

invalid_attempts = 0
MAX_INVALID_ATTEMPTS = 5

# Simple function to kill process if invalid tries too many times
def reset_count():
    global invalid_attempts
    invalid_attempts = 0

# Ascii art
art = r"""

     ___  ___      ___    ___ ________  _______   ________  ___  ________     
    │╲  ╲│╲  ╲    │╲  ╲  ╱  ╱│╲   __  ╲│╲  ___ ╲ │╲   __  ╲│╲  ╲│╲   __  ╲    
    ╲ ╲  ╲╲╲  ╲   ╲ ╲  ╲╱  ╱ │ ╲  ╲│╲  ╲ ╲   __╱│╲ ╲  ╲│╲  ╲ ╲  ╲ ╲  ╲│╲  ╲   
     ╲ ╲   __  ╲   ╲ ╲    ╱ ╱ ╲ ╲   ____╲ ╲  ╲_│╱_╲ ╲   _  _╲ ╲  ╲ ╲   __  ╲  
      ╲ ╲  ╲ ╲  ╲   ╲╱  ╱  ╱   ╲ ╲  ╲___│╲ ╲  ╲_│╲ ╲ ╲  ╲╲  ╲╲ ╲  ╲ ╲  ╲ ╲  ╲ 
       ╲ ╲__╲ ╲__╲__╱  ╱ ╱      ╲ ╲__╲    ╲ ╲_______╲ ╲__╲╲ _╲╲ ╲__╲ ╲__╲ ╲__╲
        ╲│__│╲│__│╲___╱ ╱        ╲│__│     ╲│_______│╲│__│╲│__│╲│__│╲│__│╲│__│
                 ╲│___│╱                                                      

   """
# Function to kill process or to end program
def close():
    sys.exit()
# Function for clearing the terminal
def clear_screen():
     os.system('cls')


colour_text_menu = Fore.CYAN + Style.BRIGHT + Back.LIGHTWHITE_EX # Series of settings for the starting menu
# Ascii art slash animation (AI was used for the mathematics)
def slash_animation(art, delay=0.04, slash_char='/'):
    lines = art.strip().splitlines()
    height = len(lines)
    width = max(len(line) for line in lines)

    term_width = shutil.get_terminal_size().columns  # Terminal width

    print("\n" * height)  # Reserve space

    for step in range(width + height):
        print(Cursor.UP(height), end="")
        print(Cursor.FORWARD(0), end="")   # Reset to start of line
        for y, line in enumerate(lines):
            # pad line to max width
            chars = list(line.ljust(width))
            pos = step - y
            if 0 <= pos < width:
                chars[pos] = colour_text_menu + slash_char
            # Center the line in terminal
            line_str = "".join(chars)
            padding = max((term_width - len(line_str)) // 2, 0)
            print(" " * padding + line_str)
        time.sleep(delay)

colorama.init() # Initialise colorama in case it bugs out


print(slow_text_centered(colour_text_menu))

clear_screen()
# Menu Text
slow_text_centered("Welcome to Hyperia", newLine = True, vertical_padding = True)
slow_text_centered("This is an island with infinite problems with solutions only you can solve!", newLine = True, vertical_padding = False)
slow_text_centered("New Game", newLine = True, vertical_padding = False)
slow_text_centered("Load Game", newLine = True, vertical_padding = False)
slow_text_centered("Quit", newLine = True, vertical_padding = False)
#   Start Screen input with validation
while True:
    menu_choice = input(">").lower()

    if menu_choice == 'play':
            clear_screen()
            slash_animation(art)
            time.sleep(3)
            reset_count()
            break
    elif menu_choice == 'exit':
            clear_screen()
            slow_text_centered("Goodbye see you next time!", newLine = True, vertical_padding = True)
            time.sleep(5)
            close()
            break
    else:
        print("Invalid option!")
        invalid_attempts += 1
    if invalid_attempts == MAX_INVALID_ATTEMPTS:
        clear_screen()
        slow_text_centered("I'm not that forgiving restart your game to retry", newLine = True, vertical_padding = True)
        close()
        break


clear_screen()
slow_text_centered("Welcome to Hyperia!", newLine = True)
slow_text_centered("What is your name?", newLine = True, vertical_padding = False)
#   Name input with validation
while True:
    name = input(">").strip().capitalize()
    if invalid_attempts > MAX_INVALID_ATTEMPTS:
        clear_screen()
        slow_text_centered("I'm not that forgiving restart your game to retry", newLine=True, vertical_padding=True)
        close()
        break
    if name == "":
        print("Please enter a name.")
        invalid_attempts += 1
    else:
        reset_count()
        break



clear_screen()
# Text for new game classes choice
slow_text_centered(f"Nice to meet you {name},", newLine = True, vertical_padding = True)
slow_text_centered("My name is the GameMaster you can call me GM for short", newLine = True, vertical_padding = False)
clear_screen()
slow_text_centered(f"So {name} i've heard your quite the fighter", newLine = True, vertical_padding = True)
slow_text_centered("Your device activity shows that your into very intensive fights", newLine = True, vertical_padding = False)
slow_text_centered("Don't worry in Hyperia we have quite the challengers for you", newLine = True, vertical_padding = False)
slow_text_centered("First off your going to have to pick a class", newLine = True, vertical_padding = False)

# Classes dict
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

# Class Prints
clear_screen()
slow_text_centered("These are your choices below", min_delay=0.02, max_delay=0.08, newLine = True, vertical_padding = True)
slow_text_centered("Beserker, a combat heavy class with fast attacks, though you will not be wise...", min_delay=0.02, max_delay=0.08, newLine = True, vertical_padding = False)
slow_text_centered("Mage, filled with magic and knowledge. Mana overflows from you. You will be cursed with a short life...", min_delay=0.02, max_delay=0.08, newLine = True, vertical_padding = False)
slow_text_centered("Tank, nothing can stop you. You have a heart made of iron and a body made of steel. Though your quite slow...", min_delay=0.02, max_delay=0.08, vertical_padding = False)
slow_text_centered("ERROR 404: CLASS NOT AVAILABLE FOR /-/=-/ BEEP Challenger you must think out the box for this class", min_delay=0.02, max_delay=0.08, newLine=True, vertical_padding = False)
slow_text_centered("So challenger what will be your choice?", min_delay=0.02, max_delay=0.08, newLine = True, vertical_padding = False)

# Class validation check
while True:
    player = (input(">")).strip().capitalize()
    if player == "Gm":
        player = "GM"
    if player not in ["Mage", "Tank", "GM", "Beserker"]:
        print("Sorry, that's not a valid class.")
        invalid_attempts += 1
        if invalid_attempts > MAX_INVALID_ATTEMPTS:
            clear_screen()
            slow_text_centered("I'm not that forgiving restart your game to retry", newLine = True, vertical_padding = True)
            close()
    else:
        reset_count()
        break

clear_screen()
# Easter Egg GM Class Validation Check
while True:

    if player != 'GM':
        break

    if player == 'GM':
        encrypt = input("Who is the GM?: ")
        if encrypt == 'axinesky':
            slow_text_centered("You have obtained the GM class")
            reset_count()
            break
        else: slow_text_centered("Wrong, restart your game to select a new class disappointing..")
        close()
        break
    else:
        slow_text_centered("Invalid input")
        invalid_attempts += 1
        break
# Variable to save User Selected Class
user_class = player
# Player variable is now the inner dict of the chosen class
player = copy.deepcopy(classes[player])


clear_screen()
slow_text_centered("Now you chose your class lets actually spawn your character shall we?", min_delay=0.02, max_delay=0.08, newLine = False, vertical_padding = True)
clear_screen()

slow_text_centered("*poof**", min_delay=0.02, max_delay=0.08, newLine = False, vertical_padding = True)


#Menu print
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

# This is the menu screen function just opens the menu screen
def menu_screen():
    clear_screen()
    slow_text_centered(menu_text, min_delay=0.04, max_delay=0.12 ,newLine = False, vertical_padding = True)
    slow_text_centered("What would you like to do?", min_delay=0.04, max_delay=0.12 ,newLine = True, vertical_padding = False)
    choice = input(">").strip().capitalize()
    while True:
        if choice == 'Profile':
            profile()
        elif choice == 'Inventory':
            print("WIP")

# Dictionary for profile
user_profile = {
    "name": name,
    "class": user_class,
    **classes[user_class],
}
# Variables for game mechanics
p_bal = 0
level = 0
xp = 0

#Profile Function for the menu
def profile():
    global p_bal, level, xp
    clear_screen()


    # Build the top section
    header = f"""+---------------------------+\n| Name : {user_profile['name']:<19}|\n| Class: {user_profile['class']:<19}|\n+---------------------------+"""

    # Build the stats section
    stats_lines = [f"| {key.capitalize():<12}: {value:<11}|" for key, value in player.items() if key not in ('name', 'class')]
    stats_lines.append(f"| Balance     : ${p_bal:<9,} |")
    stats_lines.append(f"| Level       : {level:<9,}  |")
    stats_lines.append(f"| XP          : {xp:<9,}  |")
    stats = "\n".join(stats_lines)

    # Prints the stats section in a separate box
    block = f"""{header}\n+--------------------------+\n{stats}\n+--------------------------+"""
    text_centered_block(block)

# User dict for player inventory (made for game saves)
inventory = {}

# This is a temporary equipped dict which user will use to use items
equipped = {
    "weapon": None,
    "shield": None,
    "armor": None
}


clear_screen()
slow_text_centered("Whoops seems like i spawned in a boss in the Hub LOL", min_delay=0.02, max_delay=0.12, newLine = True, vertical_padding = True)
slow_text_centered("Looks like your gonna have to fight it im not gonna rollback my git commit xd", min_delay=0.02, max_delay=0.12, newLine = True, vertical_padding = False)
slow_text_centered("#sorrybro #dealwithit", min_delay=0.02, max_delay=0.08, newLine = True, vertical_padding = False)
time.sleep(4)
clear_screen()

# This is a health check used in every battle. If player health equals 0 they will need to restart from their game save
def health_check():
    if player["health"] == 0:
        clear_screen()
        slow_text_centered("You have died. Please restart your game and use your game save", min_delay=0.02, max_delay=0.08, newLine = True, vertical_padding = True)


# This is the main combat system function which handles all buffs and enemy interaction
# The nice part about this function is that it uses the enemy dict and parses all the stats into here to make it functional !
def combat_system(enemy, fight_choice):
    global invalid_attempts
    temporary_mana = player["mana"]
    temporary_agility = player["agility"]
    temporary_damage = player["damage"]
    temporary_enemy_health = enemy["health"]
    speedbuff_applied = False
    if enemy["health"] == 0:
        clear_screen()
        slow_text_centered(f"You have killed {enemy}!", min_delay=0.02, max_delay=0.08, newLine = True, vertical_padding = True)
    if not speedbuff_applied and player["agility"] > enemy["agility"]:
        speedbuff = temporary_agility / 250
        temporary_damage += speedbuff
        print("You are faster than the enemy you have gained a ", speedbuff, "damage boost!")
        speedbuff_applied = True

    if fight_choice == "Attack":
        enemy["health"] -= temporary_damage
        clear_screen()
        slow_text_centered(f"You dealt {temporary_damage} to {enemy}")
        reset_count()
    elif fight_choice == "Magicspell":
        reset_count()
        if temporary_mana < 20:
            print("You dont have enough mana it takes 20 per buff")
        if temporary_mana > 20:
            buff = temporary_damage  + (player["damage"] * 0.15)
            temporary_mana -= 20
            enemy["health"] -= buff
            print("You dealt ", buff, "damage!", enemy.capitalize(), "currently has ", enemy["health"])
    elif fight_choice == "Menu":
        reset_count()
        menu_screen()
    else:
        print("Invalid choice")
        invalid_attempts += 1
    if invalid_attempts > MAX_INVALID_ATTEMPTS:
            clear_screen()
            slow_text_centered("I'm not that forgiving restart your game to retry", newLine = True, vertical_padding = True)
            close()


hub_boss = list(enemy.keys())[0]
hub_boss_stats = enemy["Slime"]

slow_text_centered(f"You are being att  acked by a {hub_boss}", min_delay=0.02, max_delay=0.12, newLine = True, vertical_padding = True)
slow_text_centered("What would you like to do? ", min_delay=0.02, max_delay=0.12, newLine = True, vertical_padding = False)
while hub_boss_stats["health"] > 0:
    user_choice = input(">").lower().strip()
    combat_system(enemy["Slime"], user_choice)
    health_check()
    if hub_boss_stats["health"] < 0:
        clear_screen()
        slow_text_centered(f"You have killed {hub_boss}!", min_delay=0.02, max_delay=0.08, newLine = True, vertical_padding = True)


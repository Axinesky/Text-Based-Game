import colorama
from colorama import Fore, Back, Style, Cursor
from dir.slowtext import slow_text_centered, text_centered_block
from dir.dicts import hostile
import time
import os
import sys
import shutil
import copy
import json

# CONSTANTS (please dont change)
invalid_attempts = 0
MAX_INVALID_ATTEMPTS = 5
BASE_DIR = os.path.dirname(os.path.abspath(__file__)) # To get the root of the process
SAVE_PATH = os.path.join(BASE_DIR, "dir", "gamesave.json")



# Variables with empty values later to be overwritten
name = ""
user_class = ""
player = {}
level = 0
xp = 0
p_bal = 0
player_data = {}
location = ""
basic = {}
classes = {}

def update_location(x):
    player_data["location"] = x

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


colour_text_menu = Fore.CYAN + Style.BRIGHT + Back.LIGHTWHITE_EX  # Series of settings for the starting menu


# Ascii art slash animation (AI was used for the mathematics)
def slash_animation(obj, delay=0.04, slash_char='/'):
    lines = obj.strip().splitlines()
    height = len(lines)
    width = max(len(line) for line in lines)

    term_width = shutil.get_terminal_size().columns  # Terminal width

    print("\n" * height)  # Reserve space

    for step in range(width + height):
        print(Cursor.UP(height), end="")
        print(Cursor.FORWARD(0), end="")  # Reset to start of line
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


colorama.init()  # Initialise colorama in case it bugs out

# Formats background and text colour
print(slow_text_centered(colour_text_menu))


clear_screen()


speedbuff_applied = False  # Flag for the speedbuff effect

# Save game function gets all data from the dict formats it as a dict and dumps it in json form
def save_game(filename="gamesave.json"):
    global player_data
    player_data = {         # Data being copied into a dict using variables so it updates if the variable updates
        "name": name,
        "class": user_class,
        "stats": player,
        "level": level,
        "xp": xp,
        "balance": p_bal,
        "location": ""
    }
    full_path = os.path.join(SAVE_PATH, filename)       # Connects the file and path to dict
    with open(os.path.join(full_path), "w") as f:
        json.dump(player_data, f, indent=4)         # Dumps it in json indent 4 is just to make it look cleaner :)
    clear_screen()
    slow_text_centered("Game saved successfully!", min_delay=0.02, max_delay=0.08, newLine=True, vertical_padding=True)
    time.sleep(0.75)
    clear_screen()


# Stat refresh after every fight
def health_refresh():
    global speedbuff_applied
    player["health"] = copy.deepcopy(classes[user_class]["health"])
    player["mana"] = copy.deepcopy(classes[user_class]["mana"])
    speedbuff_applied = False


# This is the main combat system function which handles all buffs and enemy interaction
# The nice part about this function is that it uses the enemy dict and parses all the stats into here to make it functional !
def combat_system(enemy, fight_choice, enemy_name):
    global invalid_attempts
    global speedbuff_applied
    temporary_mana = int(player["mana"])
    temporary_agility = int(player["agility"])
    temporary_damage = int(player["damage"])
    temporary_enemy_health = int(enemy["health"])
    temporary_player_health = int(player["health"])
    temporary_enemy_damage = int(enemy["damage"])
    temporary_attack_speed = int(player["attack_speed"])

    # This is a health check used in every battle. If player health equals 0 they will need to restart from their game save
    def health_check():
        if temporary_player_health <= 0:
            clear_screen()
            slow_text_centered("You have died. Please restart your game and use your game save", min_delay=0.02,max_delay=0.08, newLine=True, vertical_padding=True)
            close()

    if enemy["health"] == 0:
        clear_screen()
        slow_text_centered(f"You have killed {enemy}!", min_delay=0.02, max_delay=0.08, newLine=True,vertical_padding=True)
    if not speedbuff_applied:
        speedbuff = (temporary_agility / 250) + (temporary_attack_speed / 500)
        temporary_damage += int(speedbuff)
        slow_text_centered(f"You are faster than the enemy! You gained a {speedbuff} damage boost!",
                           min_delay=0.02, max_delay=0.08, newLine=True, vertical_padding=True)
        speedbuff_applied = True
        time.sleep(1.5)
        clear_screen()
    while True:
        if fight_choice == "Attack":
            temporary_enemy_health -= int(temporary_damage)
            clear_screen()
            slow_text_centered(f"You dealt {temporary_damage} to {enemy_name}!", min_delay=0.02, max_delay=0.08,
                               newLine=True, vertical_padding=True)
            if 0 < temporary_enemy_health:
                slow_text_centered(f"{enemy_name.capitalize()} currently has {int(temporary_enemy_health)} health!\n",
                                   min_delay=0.02, max_delay=0.08, newLine=True, vertical_padding=False)
                time.sleep(1.75)
                clear_screen()
            else:
                slow_text_centered(f"{enemy_name.capitalize()} currently has 0 health!\n", min_delay=0.02,
                                   max_delay=0.08, newLine=True, vertical_padding=False)
                time.sleep(1.75)
                clear_screen()
            reset_count()
            time.sleep(1.75)
            break
        elif fight_choice == "Magic spell":
            reset_count()
            clear_screen()
            if temporary_mana < 20:
                slow_text_centered("You don't have enough mana it requires 20", min_delay=0.02, max_delay=0.08,newLine=True, vertical_padding=True)
                time.sleep(3)
                clear_screen()
                return temporary_player_health, temporary_enemy_health  # Breaks function to get user input again
            if temporary_mana >= 20:
                buff = int(temporary_damage) + int((player["damage"] * 0.15))
                temporary_mana -= 20
                player["mana"] = temporary_mana
                temporary_enemy_health -= buff
                clear_screen()
                slow_text_centered(f"You dealt {buff} to {enemy_name}!", min_delay=0.02, max_delay=0.08, newLine=True,
                                   vertical_padding=True)
                if 0 < temporary_enemy_health:
                    slow_text_centered(f"{enemy_name.capitalize()} currently has {temporary_enemy_health} health!\n",
                                       min_delay=0.02, max_delay=0.08, newLine=True, vertical_padding=False)
                    time.sleep(1.75)
                else:
                    slow_text_centered(f"{enemy_name.capitalize()} currently has 0 health!\n", min_delay=0.02,
                                       max_delay=0.08, newLine=True, vertical_padding=False)
                time.sleep(1.75)
                break
        else:
            print("> Invalid choice")
            invalid_attempts += 1
        if invalid_attempts > MAX_INVALID_ATTEMPTS:
            clear_screen()
            slow_text_centered("I'm not that forgiving restart your game to retry", newLine=True, vertical_padding=True)
            close()
    if temporary_player_health >= 0 and temporary_enemy_health >= 0:
        temporary_player_health -= temporary_enemy_damage
        clear_screen()
        slow_text_centered(f"{enemy_name} dealt {temporary_enemy_damage} to you!", min_delay=0.02, max_delay=0.08, newLine=True, vertical_padding=True)
        time.sleep(3)
        clear_screen()
        if temporary_mana >= 0:
            slow_text_centered(f"You currently have {temporary_player_health} health left!", min_delay=0.02,max_delay=0.08, newLine=True, vertical_padding=False)
            clear_screen()
        else:
            slow_text_centered(f"You currently have 0 health left!", min_delay=0.02, max_delay=0.08, newLine=True,vertical_padding=False)
            clear_screen()
        health_check()
        time.sleep(3)
    return temporary_player_health, temporary_enemy_health  # Breaks function and goes back to that original while loop that is making this battle run


#   Start Screen input with validation
def setup():
    global invalid_attempts, name, user_class, player, xp, level, p_bal, basic, speedbuff_applied, classes
    clear_screen()
    slow_text_centered("Welcome to Hyperia!", newLine=True)
    slow_text_centered("What is your name?", newLine=True, vertical_padding=False)
    #   Name input with validation
    global name
    while True:
        name = input("> ").strip().capitalize()
        if invalid_attempts > MAX_INVALID_ATTEMPTS:
            clear_screen()
            slow_text_centered("I'm not that forgiving restart your game to retry", newLine=True, vertical_padding=True)
            close()
            break
        if name == "":
            print("> Please enter a name.")
            invalid_attempts += 1
        if len(name) > 10:
            print("> Over 10 character limit. Please enter a name.")
        else:
            reset_count()
            break

    clear_screen()
    # Text for new game classes choice
    slow_text_centered(f"Nice to meet you {name},", newLine=True, vertical_padding=True)
    slow_text_centered("My name is the GameMaster you can call me GM for short", newLine=True, vertical_padding=False)
    clear_screen()
    slow_text_centered(f"So {name} i've heard your quite the fighter", newLine=True, vertical_padding=True)
    slow_text_centered("Your device activity shows that your into very intensive fights", newLine=True,vertical_padding=False)
    slow_text_centered("Don't worry in Hyperia we have quite the challengers for you", newLine=True, vertical_padding=False)
    slow_text_centered("First off your going to have to pick a class", newLine=True, vertical_padding=False)
    time.sleep(2.5)
    clear_screen()
    # Classes dict
    classes = {

        "Beserker": {
            "health": 100,
            "attack_speed": 70,
            "mana": 20,
            "damage": 30,
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
    slow_text_centered("These are your choices below", min_delay=0.02, max_delay=0.08, newLine=True, vertical_padding=True)
    slow_text_centered("Beserker, a combat heavy class with fast attacks, though you will not be wise...", min_delay=0.02, max_delay=0.08, newLine=True, vertical_padding=False)
    slow_text_centered("Mage, filled with magic and knowledge. Mana overflows from you. You will be cursed with a short life...",min_delay=0.02, max_delay=0.08, newLine=True, vertical_padding=False)
    slow_text_centered("Tank, nothing can stop you. You have a heart made of iron and a body made of steel. Though your quite slow...",min_delay=0.02, max_delay=0.08, vertical_padding=False)
    slow_text_centered(f"ERROR 404: CLASS NOT AVAILABLE FOR /-/=-/ BEEP {name} you must think out the box for this class",min_delay=0.02, max_delay=0.08, newLine=True, vertical_padding=False)
    slow_text_centered(f"So {name} what will be your choice?", min_delay=0.02, max_delay=0.08, newLine=True,vertical_padding=False)

    # Class validation check
    while True:
        player = (input("> ")).strip().capitalize()
        if player == "Gm":
            player = "GM"
        if player not in ["Mage", "Tank", "GM", "Beserker"]:
            print("> Sorry, that's not a valid class.")
            invalid_attempts += 1
            if invalid_attempts > MAX_INVALID_ATTEMPTS:
                clear_screen()
                slow_text_centered("I'm not that forgiving restart your game to retry", newLine=True, vertical_padding=True)
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
            slow_text_centered("Who is the GM", min_delay=0.02, max_delay=0.08, newLine=True, vertical_padding=True)
            encrypt = input("> ")
            if encrypt == 'axinesky':
                clear_screen()
                slow_text_centered("You have obtained the GM class", min_delay=0.02, max_delay=0.08, newLine=True, vertical_padding=True)
                reset_count()
                break
            else:
                clear_screen()
                slow_text_centered("Wrong, restart your game to select a new class disappointing..", min_delay=0.02, max_delay=0.08, newLine=True, vertical_padding=False)
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
    slow_text_centered("Now you chose your class lets actually spawn your character shall we?", min_delay=0.02,max_delay=0.08, newLine=False, vertical_padding=True)
    clear_screen()

    slow_text_centered("*poof**", min_delay=0.02, max_delay=0.08, newLine=False, vertical_padding=True)
    clear_screen()
    # Some funny dialog so the user gets the feels of a battle
    slow_text_centered("Whoops seems like i spawned in a boss in the Hub LOL", min_delay=0.02, max_delay=0.12, newLine=True,vertical_padding=True)
    slow_text_centered("Looks like your gonna have to fight it im not gonna rollback my git commit xd", min_delay=0.02,max_delay=0.12, newLine=True, vertical_padding=False)
    slow_text_centered("#sorrybro #dealwithit", min_delay=0.02, max_delay=0.08, newLine=True, vertical_padding=False)
    time.sleep(4)
    clear_screen()


    # Assigned to temporary variables to make sure originals aren't tampered with
    hub_boss = list(hostile.keys())[0]
    hub_boss_stats = copy.deepcopy(hostile["Slime"])

    slow_text_centered(f"You are being attacked by a {hub_boss}", min_delay=0.02, max_delay=0.12, newLine=True,vertical_padding=True)
    clear_screen()
    time.sleep(1.5)
    while hub_boss_stats["health"] > 0:
        slow_text_centered("What would you like to do? ", min_delay=0.02, max_delay=0.12, newLine=True,vertical_padding=True)
        slow_text_centered("Swing your weapon (attack)", min_delay=0.02, max_delay=0.12, newLine=True,vertical_padding=False)
        slow_text_centered("Cast a spell (magic spell)", min_delay=0.02, max_delay=0.12, newLine=True,vertical_padding=False)
        user_choice = input("> ").capitalize()
        clear_screen()  # Failsafe terminal clean incase function one doesn't work
        temporary_player_health, temporary_enemy_health = combat_system(hub_boss_stats, user_choice, hub_boss)
        hub_boss_stats["health"] = temporary_enemy_health  # Update fight turn info
        player["health"] = temporary_player_health
        if temporary_enemy_health < 0:  # Kill check
            clear_screen()
            slow_text_centered(f"You have killed {hub_boss}!", min_delay=0.02, max_delay=0.08, newLine=True,vertical_padding=True)
            health_refresh()
            slow_text_centered(f"You gained 1 XP", min_delay=0.02, max_delay=0.08, newLine=True, vertical_padding=False)
            slow_text_centered(f"The slime spat out a weapon from a fallen Hub Soldier", min_delay=0.02, max_delay=0.08,newLine=True, vertical_padding=False)
            weapon = ""
            if user_class == "Mage":
                weapon = "Basic Staff"
            elif user_class == "Beserker":
                 weapon = "Basic Sword"
            elif user_class == "Tank":
                 weapon = "Basic Shield"
            elif user_class == "GM":
                 weapon = "Ban Hammer"
            slow_text_centered(f"You have obtained a {weapon} your base stats have been upgraded!", min_delay=0.02, max_delay=0.08, newLine=True,vertical_padding=False)
            basic = {} # Basic buff applied
            if user_class == "Mage":
                basic = {"mana": 10, "attack_speed": 5, "damage": 5}
            elif user_class == "Beserker":
                basic = {"damage": 10, "attack_speed": 10, "agility": 5}
            elif user_class == "Tank":
                basic = {"health": 20, "agility": 10, "damage": 10}
            elif user_class == "GM":
                basic = {"health": 9999, "damage": 9999, "mana": 9999}
            else:
                clear_screen()
                slow_text_centered("How did you even get here with no class?? ur banned", min_delay=0.02, max_delay=0.08, newLine=True, vertical_padding=True)
                close()
            for key, value in basic.items():
                slow_text_centered(f"You have gained {key} buff of {value}", min_delay=0.02, max_delay=0.08, newLine=True, vertical_padding=False)
            time.sleep(3.5)
            clear_screen()
            slow_text_centered("Well then i guess my attempt for you to quit didn't work", min_delay=0.02, max_delay=0.08, newLine=True, vertical_padding=True)
            slow_text_centered("Alright fine ill send you to the Hub", min_delay=0.02, max_delay=0.08,newLine=True, vertical_padding=False)
            update_location("Hub")
            save_game()


# Menu print
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
    slow_text_centered(menu_text, min_delay=0.04, max_delay=0.12, newLine=False, vertical_padding=True)
    slow_text_centered("What would you like to do?", min_delay=0.04, max_delay=0.12, newLine=True,vertical_padding=False)
    choice = input("> ").strip().capitalize()
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


    # Profile Function for the menu
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

def add_buff(buff):
    for stat, value in buff.items():
        player[stat] += value

def remove_buff(buff):
    for stat, value in buff.items():
        player[stat] -= value

def locator():
    if player_data["location"] == "Hub":
        hub()

# Menu Text
slow_text_centered("Welcome to Hyperia", newLine=True, vertical_padding=True)
slow_text_centered("This is an island with infinite problems with solutions only you can solve!", newLine=True,vertical_padding=False)
slow_text_centered("New Game", newLine=True, vertical_padding=False)
slow_text_centered("Load Game", newLine=True, vertical_padding=False)
slow_text_centered("Quit", newLine=True, vertical_padding=False)

# Menu choice selection
while True:
    menu_choice = input("> ").lower().strip()

    if menu_choice == 'new game':
        clear_screen()
        slash_animation(art)
        time.sleep(3)
        setup()
        reset_count()
        break
    elif menu_choice == 'exit':
        clear_screen()
        slow_text_centered("Goodbye see you next time!", newLine=True, vertical_padding=True)
        time.sleep(5)
        close()
        break
    else:
        print("> Invalid option!")
        invalid_attempts += 1
    if invalid_attempts == MAX_INVALID_ATTEMPTS:
        clear_screen()
        slow_text_centered("I'm not that forgiving restart your game to retry", newLine=True, vertical_padding=True)
        close()
        break

def load_game(filename="gamesave.json"):
    global player_data, player, name, p_bal, user_class, level, xp, location

    filepath = os.path.join("dir", filename)

    if not os.path.exists(filepath):
        clear_screen()
        slow_text_centered("You have no game save", min_delay=0.02, max_delay=0.08, newLine=True, vertical_padding=True)
        slow_text_centered("Loading you into a new game file", min_delay=0.02, max_delay=0.08, newLine=True, vertical_padding=False)
        time.sleep(2)
        setup()

    with open(filepath, "r") as f:
        player_data = json.load(f)



    # Load in data from the json file
    name = player_data["name"]
    user_class = player_data["class"]
    player = player_data["stats"]
    level = player_data["level"]
    xp = player_data["xp"]
    p_bal = player_data["balance"]
    location = player_data["location"]


def hub():
    clear_screen()
    slow_text_centered("Welcome to the Hub", min_delay=0.02, max_delay=0.08, newLine=True, vertical_padding=True)
    slow_text_centered("You can interact with the options below", min_delay=0.02, max_delay=0.08, newLine=True, vertical_padding=False)
    slow_text_centered("Speak to locals", min_delay=0.02, max_delay=0.08, newLine=True, vertical_padding=False)
    slow_text_centered("Go to the blacksmith", min_delay=0.02, max_delay=0.08, newLine=True, vertical_padding=False)
    slow_text_centered("Enter the Dwarven Mines", min_delay=0.02, max_delay=0.08, newLine=True, vertical_padding=False)
    slow_text_centered("Enter the Guild Hall", min_delay=0.02, max_delay=0.08, newLine=True, vertical_padding=False)

    hub_choice = input("> ").lower().strip()

    if hub_choice == 'speak to the locals':
        clear_screen()
        slow_text_centered("Speak to Certi")
        slow_text_centered("Speak to Ewan")
        slow_text_centered("Speak to Axinesky")
        slow_text_centered("Speak to Damian")
        hub_npc_choice = input("> ").lower().strip()
        if hub_npc_choice == "speak to the certi":
            clear_screen()
            slow_text_centered("Don't speak to Damian.")
            slow_text_centered("If you do and entertain him it wont end well")
            slow_text_centered("P.S sly promo go buy btc")

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
if menu_choice == 'quit':
    clear_screen()
    slow_text_centered("Goodbye see you next time!", newLine = True, vertical_padding = True)
    time.sleep(5)
    sys.exit()
elif menu_choice('play'):
    clear_screen()
    time.sleep(2000)
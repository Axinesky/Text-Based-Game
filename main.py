import colorama
from colorama import Fore, Back, Style
from dir.slowtext import slow_text
import time 
import sys
import random
import shutil 
import os 


def clear_screen():
     os.system('cls')

colorama.init() # Initialise colorama incase it bugs out 

colour_text_menu = Fore.CYAN + Style.BRIGHT + Back.LIGHTWHITE_EX # Series of settings for the starting menu

def center_text(text):
     terminal_size = shutil.get_terminal_size()
     width = terminal_size.columns
     height = terminal_size.lines

     vertical_term = height // 2 

     for _ in range(vertical_term):
        print()


     return text.center(width)

print(center_text(colour_text_menu))

clear_screen()

slow_text(center_text("Welcome to Hyperia!"), 0.02, 0.3)
print(slow_text(center_text(("This is a magical world with joy and despair"))))

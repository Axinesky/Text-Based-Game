import sys 
import time
import random
import shutil
import colorama
from colorama import Fore, Back, Style, Cursor

def slow_text_centered(text, min_delay=0.02, max_delay=0.12, newLine = False, vertical_padding=True):
    terminal_size = shutil.get_terminal_size()
    width = terminal_size.columns
    height = terminal_size.lines


    if vertical_padding:
        vertical_term = height // 2

        print("\n" * vertical_term, end="")

    horizontal_padding = (width - len(text)) // 2
    print(" " * horizontal_padding, end="")


    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(random.uniform(min_delay, max_delay))
        
        
    if newLine:
            print()


def text_centered_block(text):
    terminal_size = shutil.get_terminal_size()
    width = terminal_size.columns
    height = terminal_size.lines

    lines = text.strip().split('\n')
    max_line_length = max(len(line) for line in lines)
    vertical_padding = (height - len(lines)) // 2

    print('\n' * vertical_padding, end='')
    for line in lines:
        line = line.rstrip()
        horizontal_padding = (width - max_line_length) // 2
        print(' ' * horizontal_padding + line)


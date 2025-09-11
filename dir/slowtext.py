import sys 
import time
import random

def slow_text(text, min_delay=0.02, max_delay=0.3, newLine = False):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(random.uniform(min_delay, max_delay))
        
        
    if newLine:
            print()

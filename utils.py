import os
import time
import random

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def countdown():
    for i in range(3, 0, -1):
        print(f"Starting in {i}...")
        time.sleep(1)

def get_random_paragraph():
    paragraphs = [
        "Typing fast requires practice and patience.",
        "Python is a versatile and widely used programming language.",
        "Consistency is the key to improvement in any skill.",
        "The quick brown fox jumps over the lazy dog.",
        "Machine learning is transforming the world around us."
    ]
    return random.choice(paragraphs)

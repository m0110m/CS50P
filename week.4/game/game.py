import random
import sys

def main():
    level = get_level()
    x = random.randint(1,level)
    while True:
        try:
            guess = int(input("Guess: "))
            if guess <= 0:
                continue
            elif guess > x:
                print("Too large!")
            elif guess < x:
                print("Too small!")
            else:
                sys.exit("Just right!")
        except ValueError:
            pass

def get_level():
    while True:
        try:
            n = int(input("Level: "))
            if n < 0:
                continue
            return n
        except ValueError:
            pass

main()

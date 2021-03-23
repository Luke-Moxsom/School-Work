import random

ESCAPE_DISTANCE = 100

RED = '\033[31m'
GREEN = '\033[32m'
ORANGE = '\033[33m'
BLUE = '\033[34m'
PURPLE = '\033[35m'
CYAN = '\033[36m'
GRAY = '\033[37m'
WHITE = '\033[38m'


def title():
    """
    PRINTS THE TITLE OF THE GAME
    """
    print(RED + """
-----------------------------------------------------------------------
-----------------------------------------------------------------------
""" + WHITE + """
          
                            Escape Game

""" + RED + """
-----------------------------------------------------------------------
-----------------------------------------------------------------------""" + WHITE)


def blank_spaces():
    """
    PRINTS 2 BLANK SPACES
    """
    print("")
    print("")


def rules():
    """
    PRINTS THE RULES FOR THE PLAYERS TO READ
    """
    print("""
Welcome traveler,
You have stolen a camel to make your way across the great Mobi desert.
The natives want their camel back and are chasing you down! 
Survive your desert trek and outrun the natives.""")


def player():
    """
    PLAYER STATS
    """
    WATER_AMOUNT = 5
    ENERGY_AMOUNT = 5
    MAX_FULL_SPEED = 20
    MAX_HALF_SPEED = 10

    PLAYER_CHOICE = input("""
1. Drink from your water bottle.
2. Travel ahead at half speed.
3. Travel ahead at full speed.
4. Stop and rest.
5. Status check.
6. Given to the desert.
""")

    if PLAYER_CHOICE == "1":
        print("Your choice was 1")

    elif PLAYER_CHOICE == "2":
        print("Your choice was 2")

    elif PLAYER_CHOICE == "3":
        print("Your choice was 3")

    elif PLAYER_CHOICE == "4":
        print("Your choice was 4")

    elif PLAYER_CHOICE == "5":
        print("Your choice was 5")

    elif PLAYER_CHOICE == "6":
        print("Your choice was 6")

    else:
        print("Please choose an option")



def main():
    blank_spaces()
    title()
    blank_spaces()
    rules()
    player()

main()

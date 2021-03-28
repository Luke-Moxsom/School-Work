import random

RED = '\033[31m'
GREEN = '\033[32m'
ORANGE = '\033[33m'
BLUE = '\033[34m'
PURPLE = '\033[35m'
CYAN = '\033[36m'
GRAY = '\033[37m'
WHITE = '\033[38m'
BOLD = '\033[1m'
RESET = '\033[0m'


def title():
    """
    PRINTS THE TITLE OF THE GAME
    """
    print(RED + """
-----------------------------------------------------------------------
-----------------------------------------------------------------------
""" + RESET + """
          
"""+BOLD+RED+"""                            Escape Game"""+RESET+"""

""" + RED + """
-----------------------------------------------------------------------
-----------------------------------------------------------------------""" + RESET)


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
    player_travelled = 0
    natives_travelled = -50
    if_continue = "0"
    thirst = 5
    energy = 10
    water_bottle = 5

    while if_continue != 6:

        blank_spaces()

        player_choice = input(RED + "1." + RESET + " Drink from your water bottle.\n" + RED + "2." + RESET +
                              " Travel ahead at full speed.\n" + RED + "3." + RESET + " Travel ahead at half speed.\n"
                              + RED + "4." + RESET + " Stop and rest.\n" + RED + "5." + RESET + " Status check.\n"
                              + RED + "6." + RESET + " Given to the desert.\n"+BOLD+RED+"CHOOSE : "+RESET)

        blank_spaces()

        if water_bottle == 0:
            """
            CHECK IF WATER BOTTLE IS EMPTY
            """
            natives_distance_round_travelled = random.randrange(10, 25, 1)
            natives_travelled += natives_distance_round_travelled
            print("You pull out your water bottle to find out that it was empty")
            print("You wasted a turn while the"+RED+" natives"+RESET +
                  " continued forwards and traveled"+RED, natives_travelled)

        elif player_choice == "1":
            """
            DRINKS WATER
            """
            natives_distance_round_travelled = random.randrange(10, 25, 1)
            thirst = water_bottle + random.randrange(2, 5, 1)
            natives_travelled += natives_distance_round_travelled
            print("You stop and take a break to have a"+BLUE+" drink"+RESET)
            water_bottle -= 1

        elif player_choice == "2":
            """
            MOVES FORWARDS AT FULL SPEED
            """
            energy -= 3
            thirst -= 1
            player_distance_round_travelled = random.randrange(10, 20, 1)
            natives_distance_round_travelled = random.randrange(10, 20, 1)
            player_travelled += player_distance_round_travelled
            natives_travelled += natives_distance_round_travelled
            print("You travelled"+RED, player_distance_round_travelled, RESET+" and the natives travelled"+RED,
                  natives_distance_round_travelled, RESET)

        elif player_choice == "3":
            """
            MOVES FORWARDS AT HALF SPEED
            """
            energy -= 1
            thirst -= 1
            player_distance_round_travelled = random.randrange(1, 10, 1)
            natives_distance_round_travelled = random.randrange(10, 20, 1)
            player_travelled += player_distance_round_travelled
            natives_travelled += natives_distance_round_travelled
            print("You travelled"+RED, player_distance_round_travelled, RESET+" and the natives travelled"+RED,
                  natives_distance_round_travelled, RESET)

        elif player_choice == "4":
            """
            STOPS AND RESTS
            """
            energy_gain = random.randrange(5, 10, 1)
            natives_distance_round_travelled = random.randrange(10, 25, 1)
            natives_travelled += natives_distance_round_travelled
            energy += energy_gain
            print("You stopped for a rest, you have gained"+RED, energy_gain, RESET+"energy")

        elif player_choice == "5":
            """
            STATS CHECK
            """
            print("Kilometers travelled:"+RED, player_travelled, RESET)
            print("Drinks left in water bottle:"+RED, water_bottle, RESET)
            print("The natives are"+RED, player_travelled-natives_travelled, "kilometers"+RESET+" behind you")

        elif player_choice == "6":
            print(RED+"You have given into the heat of the desert"+BOLD+", you have lost")
            break

        else:
            """
            TELLS THE PLAYER THEY NEED TO CHOOSE AN OPTION
            """
            print("If your considering giving up press 6 or chose an option")

        if natives_travelled >= player_travelled:
            print("The"+RED+" natives"+RESET+" caught you!")
            break

        if thirst == 0:
            """
            CHECK IF THE PLAYER IS OUT OF WATER
            """
            print("You forgot to take a drink and"+RED+" died"+RESET+" of dehydration")
            break

        elif thirst == 1:
            """
            WARNS THE PLAYER THEY ARE VERY THIRSTY
            """
            print("Your throat is as dry is the desert and all you can think about is water")

        elif thirst <= 3:
            """
            TELLS THE PLAYER THEY ARE BEGINNING TO BECOME THIRSTY
            """
            print("Your throat is feeling dry")

        if energy < 4:
            """
            TELLS THE PLAYER IS STARTING TO BECOME TIRED
            """
            print("You can barely keep your eyes open")

        elif energy < 1:
            """
            CHECK IF THE PLAYER IS OUT OF ENERGY
            """
            print("You didn't take a rest and collapsed"+RED+" unconscious"+RESET)
            break

        if player_travelled >= 100:
            print("You out ran the natives and escaped to safety")
            break


def main():
    blank_spaces()
    title()
    blank_spaces()
    rules()
    player()


main()

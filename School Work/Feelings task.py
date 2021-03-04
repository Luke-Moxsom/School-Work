import random

# Creates variable that have a list inside of them.
happy_quote = ["\"Be happy with what you have. Be excited about what you want\" - Alan Cohen", "\"Its the little things that make life BIG\" - Action for Happiness"]
exuberant_quote = ["\"Exuberance of heart\nRadiates far and wide.\nLove self and\nBe bright light\"", "\"Noting ever succeeds which exuberant spirits have not helped to produce\" - Fredrich Nietzsche"]
sad_quote = ["\"Tears come from the heart not from the brain\"", "\"Tears are words that need to be written\" - Paulo Coelho"]
depressed_quote = ["\"Depression is not a sign of weakness. It means you've been strong for too long - Greeting Card Poet\"", "\"Depression is being colourblind and constantl told how colourfil the world is\" - Atticus"]


def list_feelings():
    # Prints out all the options for the user to choose.
    print("1. Happy\n2. Exuberant\n3. Sad\n4. Depressed")


def check_feelings():
    loop = 1
    while loop == 1:
        # Asks the user how they are feeling.
        feelings = input("")
        # Checks their feeling and prints a quote to match their feelings.
        if feelings == "1" or feelings == "Happy" or feelings == "happy":
            print(happy_quote[random.randrange(len(happy_quote))])
            break
        elif feelings == "2" or feelings == "Exuberant" or feelings == "exuberant":
            print(exuberant_quote[random.randrange(len(exuberant_quote))])
            break
        elif feelings == "3" or feelings == "Sad" or feelings == "sad":
            print(sad_quote[random.randrange(len(sad_quote))])
            break
        elif feelings == "4" or feelings == "Depressed" or feelings == "depressed":
            print(depressed_quote[random.randrange(len(depressed_quote))])
            break
        else:
            print("Please enter a valid feeling that is listed above")


def main():
    check_quit = "1"
    # The main function that runs all the code.
    name = input("What is your name?\n")
    while check_quit == "1":
        print("Hello " + name + " how are you feeling today?(You can type the word or number)\n")
        # Calls the function (list_feelings).
        list_feelings()
        # Calls the function (check_feelings).
        check_feelings()
        # Asks the user if they want to quit.
        check_quit = input("\nWould you like to retry? to retry type 1 or to quit press any key.\n")
        if check_quit == "1":
            pass
        else:
            print("Thank you for telling me about your feelings :)")
            break


# Calls the main code.
main()

from asciify import runner
import os

eventNumber = 1  # The event loop
playerAlive = True  # Check if the player is alive
playerInventory = []  # List of the player's inventory
eventCheck = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]  # Event checks booleans


def format_options(options):
    output = ""
    for option in range(0, len(options)):
        output += str(option + 1) + ". " + options[option] + "\n"

    return output

def bold_output():
    print('\033[1m')

def unbold_output():
    print('\033[0m')

# Function: Prints out help commands if player asks for it
def HelpCommands():
    print("-------------------------------------------------------------")
    print("Help Commands")
    print("Move <direction parameter>")
    print("Parameters: North, South, East, West")
    print("Example: Move South")
    print("Shortcuts: m <letter of direction>, i.e. 'm s' ")
    print("")
    print("Take <object name parameter>")
    print("Parameters: Any object in the room/cell")
    print("Example: Take sword")
    print("Shortcuts: None ")
    print("")
    print("Attack <entity name parameter> with <weapon/object parameter>")
    print("Parameters: Any entity in the room/cell")
    print("Parameters: Any weapon or object in inventory or room/cell")
    print("Example: Attack orge with sword")
    print("Shortcuts: None ")
    return


# Function: Prints out the player's inventory
def DisplayInventory(playerInventory):
    if not playerInventory:
        print("------------------------------------------------------------")
        print("Your inventory is empty...")
    else:
        print("------------------------------------------------------------")
        print("You have on you")
        for x in range(len(playerInventory)):
            print(playerInventory[x])
    return

def start_game():
    while playerAlive == True:
        # Intro event cell
        while eventNumber == 1:
            if eventNumber == 1:
                if "cube" in playerInventory:
                    print("------------------------------------------------------------")
                    print("You stand inside of a debug area, devoid of color or detail.")

                else:
                    print("------------------------------------------------------------")
                    print("You stand inside of a debug area, devoid of color or detail.")
                    print("In front of you is a cube.")
                    runner("images/cube.jpg")

                bold_output()
                print("What will you do?")
                print(format_options(["take cube", "do not take cube", "move north", "move south", "move east", "move west", "check inventory", "help commands"]))
                unbold_output()

                playerInput = input()

            if playerInput.lower() == ("take cube"):
                if "cube" not in playerInventory:
                    print("------------------------------------------------------------")
                    print("Added cube to inventory")
                    playerInventory.append("cube")
                else:
                    print("------------------------------------------------------------")
                    print("There is no cube to be seen...")
            elif playerInput.lower() == ("move north") or playerInput.lower() == ("m n"):
                aquarium()
            elif playerInput.lower() == ("move south") or playerInput.lower() == ("m s"):
                print("Can't move south here...")
            elif playerInput.lower() == ("move east") or playerInput.lower() == ("m e"):
                print("Can't move east here...")
            elif playerInput.lower() == ("move west") or playerInput.lower() == ("m w"):
                print("Can't move west here...")
            elif playerInput.lower() == ("check inventory"):
                DisplayInventory(playerInventory)
            elif playerInput.lower() == ("help commands"):
                HelpCommands()
            else:
                print("I do not understand your input of " + "'" + playerInput + "'")

        # Event Cell (can be used in future)
        while eventNumber == 2:
            if eventNumber == 2:
                print("------------------------------------------------------------")
                print("Put something descriptive here")
                print("What will you do?")
                playerInput = input()

            if playerInput.lower() == (""):
                print("Something here")
            elif playerInput.lower() == ("move north") or playerInput.lower() == ("m n"):
                aquarium()
            elif playerInput.lower() == ("move south") or playerInput.lower() == ("m s"):
                print("Change event number to corresponding room")
            elif playerInput.lower() == ("move east") or playerInput.lower() == ("m e"):
                print("Change event number to corresponding room")
            elif playerInput.lower() == ("move west") or playerInput.lower() == ("m w"):
                print("Change event number to corresponding room")
            elif playerInput.lower() == ("check inventory"):
                DisplayInventory(playerInventory)
            elif playerInput.lower() == ("help commands"):
                HelpCommands()
            else:
                print("I do not understand your input of " + "'" + playerInput + "'")


def aquarium():
    print("------------------------------------------------------------")
    runner("images/aquarium.png")
    print("You hear the screaming of children and the smell of saltwater")
    print("As you walk towards the blue tinged light, and escape the darkness")
    print("You realize you are in an aquarium. As you walk throughout it")
    print("you realize that the animals are not typical from ones you've seen, they look almost human...\n\n\n")

    bold_output()
    print("What will you do?")
    print(format_options(
        ["move north", "move south", "move east", "move west", "check inventory",
         "help commands"]))
    unbold_output()

    playerInput = input()

    if playerInput.lower() == ("move north") or playerInput.lower() == ("m n"):
        gift_shop()
    elif playerInput.lower() == ("move south") or playerInput.lower() == ("m s"):
        start_game()
    elif playerInput.lower() == ("move east") or playerInput.lower() == ("m e"):
        shark()
    elif playerInput.lower() == ("move west") or playerInput.lower() == ("m w"):
        employees_only()
    elif playerInput.lower() == ("check inventory"):
        DisplayInventory(playerInventory)
    elif playerInput.lower() == ("help commands"):
        HelpCommands()
    else:
        print("I do not understand your input of " + "'" + playerInput + "'")


def shark():
    return

def employees_only():
    return

def gift_shop():
    return
if __name__ == '__main__':
    print("---------------------------------------------")
    # print("Welcome to Zronk - A Zork-like text base game.")
    runner("images/title.png")
    print("By Lewis Truong, Andrew Mei, Alexis Sanchez, ")
    print("Ryan Recta, and Setsuka Aust.")
    print("---------------------------------------------")
    print("This game operates at a prompt of an")
    print("action, then an object of reference.")
    print("---------------------------------------------")
    print("For example, ")
    print("		'take sword' ")
    print(" an action and an object of reference or ")
    print("		'attack orge with sword' ")
    print(" an action and an object of reference.")


    while True:
        i = input("Press Enter to begin ")
        if not i:
            break


    print("")
    start_game()

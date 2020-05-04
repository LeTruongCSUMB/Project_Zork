eventNumber = 1					# The event loop
playerAlive = True				# Check if the player is alive
playerInventory = []			# List of the player's inventory

print("---------------------------------------------")
print("Welcome to Zronk - A Zork-like text base game.")
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
print("---------------------------------------------")
print("Due note that not every possibly action in")
print("in the known universe is possible for us to")
print("have a reply of so try not to do the most")
print("complex and outlandish things.")
print("Thank you and have fun!")
print("---------------------------------------------")
print("")

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

			print("What will you do?")
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
			print("Can't move north here...")
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
			print("Change event number to corresponding room")
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

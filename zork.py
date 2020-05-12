eventNumber = 0												# The event loop
playerAlive = True											# Check if the player is alive
playerInventory = []										# List of the player's inventory

eventCheck = [
	{
		"room" : 0,
		"visited" : 0,
		"event" : 0,
		"objects" : []
	},
	{
		"room" : 1,
		"visited" : 0,
		"event" : 0,
		"objects" : []
	},
	{
		"room" : 2,
		"visited" : 0,
		"event" : 0,
		"objects" : []
	},
	{
		"room" : 3,
		"visited" : 0,
		"event" : 0,
		"objects" : []
	},
	{
		"room" : 4,
		"visited" : 0,
		"event" : 0,
		"objects" : []
	},
	{
		"room" : 5,
		"visited" : 0,
		"event" : 0,
		"objects" : []
	},
	{
		"room" : 6,
		"visited" : 0,
		"event" : 0,
		"objects" : ["key"]
	},
	{
		"room" : 7,
		"visited" : 0,
		"event" : 0,
		"objects" : ["radio"]
	},
	{
		"room" : 8,
		"visited" : 0,
		"event" : 0,
		"objects" : []
	},
	{
		"room" : 9,
		"visited" : 0,
		"event" : 0,
		"objects" : ["wrench"]
	},
	{
		"room" : 10,
		"visited" : 0,
		"event" : 0,
		"objects" : []
	},
	{
		"room" : 11,
		"visited" : 0,
		"event" : 0,
		"objects" : []
	}
]

print("---------------------------------------------")
print("Welcome to our Zork-like text base game.")
print("By Lewis Truong, Andrew Mei, Alexis Sanchez, ")
print("Ryan Recta, and Setsuka Aust.")
print("---------------------------------------------")
print("This game operates at a prompt of an")
print("action, then an object of reference.")
print("---------------------------------------------")
print("For example, ")
print("		'take sword' ")
print(" an action and an object of reference or ")
print("		'sit on bench' ")
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
	# EVENT CELL 0 BUNK BEDS
	# =====================================================================================
	while eventNumber == 0:
		if eventNumber == 0:
			print("------------------------------------------------------------")
			if eventCheck[0]["visited"] == 0:
				print("You wake up on the cold metal floor.")
				print("Your head is spinning into focus.")
				print("You find yourself inside a room with bunk beds, most of ")
				print("which seemed to have been recently used.")
				print("On the floor seems to be full of clutter, as if people were ")
				print("recently here and in a panic to leave... ")
				eventCheck[0]["visited"] = 1
			elif eventCheck[0]["visited"] == 1:
				print("You are in the room where you woke up, it's still in a mess.")
			
			if eventCheck[0]["objects"]:
				print("------------------------------------------------------------")
				print("Objects in this room: ")
				for x in range(len(eventCheck[0]["objects"])):
					print(eventCheck[0]["objects"][x])

			print("------------------------------------------------------------")
			# CHECKS IF ROOM 1 HAS BEEN VISITED OR NOT
			if eventCheck[1]["visited"] == 0:
				print("To your west is a door.")
			elif eventCheck[1]["visited"] == 1:
				print("To your west is the corridor with the large window with the ")
				print("bench.")

			# CHECKS IF ROOM 10 HAS BEEN VISITED OR NOT
			if eventCheck[10]["visited"] == 0:
				print("To your east is a door with a sign that has been torn off.")
			elif eventCheck[10]["visited"] == 1:
				print("To your east is the airlock controls room.")

			print("What will you do?")
			playerInput = input()

			if playerInput.lower() == ("move north") or playerInput.lower() == ("m n"):
				print("Cannot move North here...")
			elif playerInput.lower() == ("move south") or playerInput.lower() == ("m s"):
				print("Cannot move South here...")
			elif playerInput.lower() == ("move east") or playerInput.lower() == ("m e"):
				eventNumber = 10
			elif playerInput.lower() == ("move west") or playerInput.lower() == ("m w"):
				eventNumber = 1
			elif playerInput.lower() == ("check inventory"):
				DisplayInventory(playerInventory)
			elif playerInput.lower() == ("help commands"):
				HelpCommands()
			else:
				print("I do not understand your input of " + "'" + playerInput + "'")
	# =====================================================================================

	# EVENT CELL 1 OBSERVATION DECK
	# =====================================================================================
	while eventNumber == 1:
		if eventNumber == 1:
			print("------------------------------------------------------------")
			if eventCheck[1]["visited"] == 0:
				print("You enter a corridor that has a large window and a bench.")
				print("As you entered, you noticed a large shadow cast in the room.")
				print("But before you can make another step the shadow binks away..")
				eventCheck[1]["visited"] = 1
			elif eventCheck[1]["visited"] == 1:
				print("You are in the corridor with a large window and a bench.")
				print("There's nothing outside in the waters as far as you can see.")
			
			if eventCheck[1]["objects"]:
				print("------------------------------------------------------------")
				print("Objects in this room: ")
				for x in range(len(eventCheck[1]["objects"])):
					print(eventCheck[1]["objects"][x])

			print("------------------------------------------------------------")
			# CHECKS IF ROOM 3 HAS BEEN VISITED OR NOT
			if eventCheck[3]["visited"] == 0:
				print("To your north is the end of the corridor.")
			elif eventCheck[3]["visited"] == 1:
				print("To your north is the corridor with the sign pointing to the ")
				print("airlock exit.")

			# CHECKS IF ROOM 7 HAS BEEN VISITED OR NOT
			if eventCheck[7]["visited"] == 0:
				print("To your south is a door.")
			elif eventCheck[7]["visited"] == 1:
				print("To your south is a door to a rec room.")
			
			# CHECKS IF ROOM 0 HAS BEEN VISITED OR NOT
			if eventCheck[0]["visited"] == 0:
				print("To your east is a room of mysterious intent.")
			elif eventCheck[0]["visited"] == 1:
				print("To your east is the room where you woke up in.")

			print("What will you do?")
			playerInput = input()

			if playerInput.lower() == ("sit on bench") or playerInput.lower() == ("sit at bench"):
				print("------------------------------------------------------------")
				print("You take a seat on the bench and look out at window, showing")
				print("you the dark ocean floor.")
				print("After some time you get up to continue on.")
			elif playerInput.lower() == ("move north") or playerInput.lower() == ("m n"):
				eventNumber = 3
			elif playerInput.lower() == ("move south") or playerInput.lower() == ("m s"):
				eventNumber = 7
			elif playerInput.lower() == ("move east") or playerInput.lower() == ("m e"):
				eventNumber = 0
			elif playerInput.lower() == ("move west") or playerInput.lower() == ("m w"):
				print("------------------------------------------------------------")
				print("We cannot go this direction and it would be not wise to ")
				print("break this window...")
			elif playerInput.lower() == ("check inventory"):
				DisplayInventory(playerInventory)
			elif playerInput.lower() == ("help commands"):
				HelpCommands()
			else:
				print("I do not understand your input of " + "'" + playerInput + "'")
	# =====================================================================================

	# EVENT CELL 2 EMPTY DOCKING PORT
	# =====================================================================================
	while eventNumber == 2:
		print("------------------------------------------------------------")
		if eventNumber == 2:
			if eventCheck[2]["visited"] == 0:
				print("You enter a large chamber that has a large puddle of water.")
				print("You notice a giant vault like door that has a small porthole")
				print("where you can see the ocean...")
				print("This is an empty airlock docking port.")
				eventCheck[2]["visited"] = 1
			elif eventCheck[2]["visited"] == 1:
				print("You are in an empty airlock docking port.")
			
			if eventCheck[2]["objects"]:
				print("------------------------------------------------------------")
				print("Objects in this room: ")
				for x in range(len(eventCheck[2]["objects"])):
					print(eventCheck[2]["objects"][x])

			print("------------------------------------------------------------")
			# CHECKS IF ROOM 3 HAS BEEN VISITED OR NOT
			if eventCheck[3]["visited"] == 0:
				print("To your west is the end of the corridor.")
			elif eventCheck[3]["visited"] == 1:
				print("To your west is the corridor with the sign pointing to the ")
				print("airlock exits.")

			print("What will you do?")
			playerInput = input()

			if playerInput.lower() == ("move north") or playerInput.lower() == ("m n"):
				print("------------------------------------------------------------")
				print("You cannot move there.")
			elif playerInput.lower() == ("move south") or playerInput.lower() == ("m s"):
				print("------------------------------------------------------------")
				print("You cannot move there.")
			elif playerInput.lower() == ("move east") or playerInput.lower() == ("m e"):
				print("------------------------------------------------------------")
				print("You cannot be expected to go swim out this way...")
			elif playerInput.lower() == ("move west") or playerInput.lower() == ("m w"):
				eventNumber = 3
			elif playerInput.lower() == ("check inventory"):
				DisplayInventory(playerInventory)
			elif playerInput.lower() == ("help commands"):
				HelpCommands()
			else:
				print("I do not understand your input of " + "'" + playerInput + "'")
	# =====================================================================================

	# EVENT CELL 3 CORRIDOR TO AIRLOCK WEST
	# =====================================================================================
	while eventNumber == 3:
		print("------------------------------------------------------------")
		if eventNumber == 3:
			if eventCheck[3]["visited"] == 0:
				print("You enter the north end of the corridor.")
				print("There in front of you is a sign that says: ")
				print("'AIRLOCK WEST: DOCKING PORT 1, DOCKING PORT 2'.")
				eventCheck[3]["visited"] = 1
			elif eventCheck[3]["visited"] == 1:
				print("You are in the north end of the corridor with the sign.")

			if eventCheck[3]["objects"]:
				print("------------------------------------------------------------")
				print("Objects in this room: ")
				for x in range(len(eventCheck[3]["objects"])):
					print(eventCheck[3]["objects"][x])

			print("------------------------------------------------------------")
			# CHECKS IF ROOM 4 HAS BEEN VISITED OR NOT
			if eventCheck[4]["visited"] == 0:
				if eventCheck[10]["event"] == 0:
					print("To your west is a large airlock door that is locked.")
				else:
					print("To your west is a docking airlock with what appears to be an")
					print("escape pod...")
			
			# CHECKS IF ROOM 2 HAS BEEN VISITED OR NOT
			if eventCheck[2]["visited"] == 0:
				print("To your east is a large airlock door that is unlocked.")
			elif eventCheck[2]["visited"] == 1:
				print("To your east is a large airlock door that leads to ")
				print("an empty airlock docking port.")

			# CHECKS IF ROOM 1 HAS BEEN VISITED OR NOT
			if eventCheck[1]["visited"] == 0:
				print("To your south is a corridor.")
			elif eventCheck[1]["visited"] == 1:
				print("To your south is the corridor with the large window and the ")
				print("bench.")

			print("What will you do?")
			playerInput = input()

			if playerInput.lower() == ("read sign"):
				print("------------------------------------------------------------")
				print("The sign says: ")
				print("'AIRLOCK WEST: DOCKING PORT 1, DOCKING PORT 2'.")
			elif playerInput.lower() == ("move north") or playerInput.lower() == ("m n"):
				print("------------------------------------------------------------")
				print("You cannot move there, there's a sign here...")
			elif playerInput.lower() == ("move south") or playerInput.lower() == ("m s"):
				eventNumber = 1
			elif playerInput.lower() == ("move east") or playerInput.lower() == ("m e"):
				eventNumber = 2
			elif playerInput.lower() == ("move west") or playerInput.lower() == ("m w"):
				if eventCheck[10]["event"] == 0:
					print("The large airlock door is locked...")
				elif eventCheck[10]["event"] == 1:
					eventNumber = 4
			elif playerInput.lower() == ("check inventory"):
				DisplayInventory(playerInventory)
			elif playerInput.lower() == ("help commands"):
				HelpCommands()
			else:
				print("I do not understand your input of " + "'" + playerInput + "'")
	# =====================================================================================

	# EVENT CELL 4 VICTORY CELL
	# =====================================================================================
	while eventNumber == 4:
		if eventNumber == 4:
			print("------------------------------------------------------------")
			print("You manage to climb into the escape pod and buckle into the ")
			print("seat. A voice from a speaker tells you that the pod will be ")
			print("ascending. Soon the pod jolts and disconnects with the dock ")
			print("and you feel and uplifting force as the pod moves up...")
			print("------------------------------------------------------------")
			print("Congratulations, You escaped the station!")
			playerAlive = False
			break;
	# =====================================================================================
			
	# EVENT CELL 5 POWER ROOM
	# =====================================================================================
	while eventNumber == 5:
		if eventNumber == 5:
			print("------------------------------------------------------------")
			if eventCheck[5]["visited"] == 0 and eventCheck[5]["event"] == 0:
				print("You enter the room, & find a large generator that is silent.")
				print("In front of you is a large switch that seems connected to ")
				print("the generator.")
				print("This is the power room.")
				eventCheck[5]["visited"] = 1
			elif eventCheck[5]["visited"] == 1 and eventCheck[5]["event"] == 0:
				print("You're in the power room, the generator isn't running.")
			elif eventCheck[5]["visited"] == 1 and eventCheck[5]["event"] == 1:
				print("You're in the power room, the generator is running.")

			if eventCheck[5]["objects"]:
				print("------------------------------------------------------------")
				print("Objects in this room: ")
				for x in range(len(eventCheck[5]["objects"])):
					print(eventCheck[5]["objects"][x])

			print("------------------------------------------------------------")
			# CHECKS IF ROOM 7 HAS BEEN VISITED OR NOT
			if eventCheck[7]["visited"] == 0:
				if eventCheck[7]["event"] == 0:
					print("To your north is a door that is locked.")
				else:
					print("To your north is a door that is unlocked.")
			elif eventCheck[7]["visited"] == 1:
				if eventCheck[7]["event"] == 0:
					print("To your north is a locked door to the rec room.")
				else:
					print("To your north is an unlocked door to the rec room.")

			print("What will you do?")
			playerInput = input()

			if playerInput.lower() == ("flip switch") or playerInput.lower() == ("use switch"):
				print("------------------------------------------------------------")
				print("The switch seems to be jammed in the off state...")
			elif playerInput.lower() == ("use wrench") or playerInput.lower() == ("wrench switch"):
				print("------------------------------------------------------------")
				if "wrench" in playerInventory:
					print("Using the wrench has turned the switch to the on state.")
					print("The generator makes a rumbling noise as it turns on.")
					eventCheck[5]["event"] == 1
				else:
					print("You do not have a wrench in your inventory...")
			elif playerInput.lower() == ("move north") or playerInput.lower() == ("m n"):
				print("------------------------------------------------------------")
				print("You cannot move there, there's a sign here...")
			elif playerInput.lower() == ("move south") or playerInput.lower() == ("m s"):
				eventNumber = 1
			elif playerInput.lower() == ("move east") or playerInput.lower() == ("m e"):
				eventNumber = 2
			elif playerInput.lower() == ("move west") or playerInput.lower() == ("m w"):
				if eventCheck[10]["event"] == 0:
					print("The large airlock door is locked...")
				elif eventCheck[10]["event"] == 1:
					eventNumber = 4
			elif playerInput.lower() == ("check inventory"):
				DisplayInventory(playerInventory)
			elif playerInput.lower() == ("help commands"):
				HelpCommands()
			else:
				print("I do not understand your input of " + "'" + playerInput + "'")
	# =====================================================================================

	# EVENT CELL 6 KITCHEN
	# =====================================================================================
	while eventNumber == 6:
		print("------------------------------------------------------------")
		if eventNumber == 6:
			if eventCheck[6]["visited"] == 0:
				print("You enter the room, & find counters and food strewn about.")
				print("The smell of food premeats the area, however you don't have ")
				print("the time to eat.")
				print("This is the kitchen.")
				eventCheck[6]["visited"] = 1
			elif eventCheck[6]["visited"] == 1:
				print("You're in the kitchen.")

			if eventCheck[6]["objects"]:
				print("------------------------------------------------------------")
				print("Objects in this room: ")
				for x in range(len(eventCheck[6]["objects"])):
					print(eventCheck[6]["objects"][x])

			print("------------------------------------------------------------")
			# CHECKS IF ROOM 7 HAS BEEN VISITED OR NOT
			if eventCheck[7]["visited"] == 0:
				print("To your east is a door that leads somewhere...")
			elif eventCheck[7]["visited"] == 1:
				print("To your east is a door leads to the rec room.")

			print("What will you do?")
			playerInput = input()

			if playerInput.lower() == ("take key") or playerInput.lower() == ("grab key"):
				print("------------------------------------------------------------")
				print("Key has been added to inventory")
				eventCheck[7]["objects"].remove("key")
				playerInventory.append("key")
			elif playerInput.lower() == ("open fridge"):
				print("------------------------------------------------------------")
				print("Opening the fridge reveals nothing of importance.")
			elif playerInput.lower() == ("open oven"):
				print("------------------------------------------------------------")
				print("Opening the oven just shows how dirty it is.")
			elif playerInput.lower() == ("use sink") or playerInput.lower() == ("wash hands"):
				print("------------------------------------------------------------")
				print("OTrying to turn on the sink results in a single drip.")
			elif playerInput.lower() == ("move north") or playerInput.lower() == ("m n"):
				print("------------------------------------------------------------")
				print("You cannot move there, there's a sink here...")
			elif playerInput.lower() == ("move south") or playerInput.lower() == ("m s"):
				("------------------------------------------------------------")
				print("You cannot move there, there's a fridge here...")
			elif playerInput.lower() == ("move east") or playerInput.lower() == ("m e"):
				eventNumber = 7
			elif playerInput.lower() == ("move west") or playerInput.lower() == ("m w"):
				("------------------------------------------------------------")
				print("You cannot move there, there's a oven here...")
			elif playerInput.lower() == ("check inventory"):
				DisplayInventory(playerInventory)
			elif playerInput.lower() == ("help commands"):
				HelpCommands()
			else:
				print("I do not understand your input of " + "'" + playerInput + "'")
	# =====================================================================================

	# EVENT CELL 7 REC ROOM
	# =====================================================================================
	while eventNumber == 7:
		if eventNumber == 7:
			print("------------------------------------------------------------")
			if eventCheck[7]["visited"] == 0:
				print("You enter the room, where there are chairs all astrewn about.")
				print("This is the rec room.")
				eventCheck[7]["visited"] = 1
			elif eventCheck[7]["visited"] == 1:
				print("You're in the rec room.")

			if eventCheck[7]["objects"]:
				print("------------------------------------------------------------")
				print("Objects in this room: ")
				for x in range(len(eventCheck[7]["objects"])):
					print(eventCheck[7]["objects"][x])

			print("------------------------------------------------------------")
			# CHECKS IF ROOM 6 HAS BEEN VISITED OR NOT
			if eventCheck[6]["visited"] == 0:
				print("To your west is a door that emiting good smells")
			elif eventCheck[6]["visited"] == 1:
				print("To your west is a door leads to the kitchen.")

			# CHECKS IF ROOM 1 HAS BEEN VISITED OR NOT
			if eventCheck[1]["visited"] == 0:
				print("To your north is a door.")
			elif eventCheck[1]["visited"] == 1:
				print("To your north is the corridor with the large window with the ")
				print("bench.")

			# CHECKS IF ROOM 8 HAS BEEN VISITED OR NOT
			if eventCheck[8]["visited"] == 0:
				print("To your east is a door.")
			elif eventCheck[8]["visited"] == 1:
				print("To your east is a corridor with the poster.")

			# CHECKS IF ROOM 8 HAS BEEN VISITED OR NOT
			if eventCheck[5]["visited"] == 0:
				print("To your south is a door with a lighting sign on it.")
			elif eventCheck[5]["visited"] == 1:
				print("To your south is the power room.")

			print("What will you do?")
			playerInput = input()

			if playerInput.lower() == ("use radio"):
				print("------------------------------------------------------------")
				print("The radio has a very thin antenna that can snapped off, and ") 
				print("a few knobs to scan however it seems to be broken...")
			elif playerInput.lower() == ("take radio"):
				print("------------------------------------------------------------")
				print("Radio added to inventory.")
				eventCheck[7]["objects"].remove("radio")
				playerInventory.append("radio")
			elif playerInput.lower() == ("snap off antenna"):
				print("------------------------------------------------------------")
				print("You break off the antenna on the radio.")
				print("------------------------------------------------------------")
				print("antenna added to inventory.")
				playerInventory.append("antenna")
			elif playerInput.lower() == ("use antenna"):
				print("------------------------------------------------------------")
				print("Using the thin antenna on the south locked door unlocks it.") 
				print("The south door is now unlocked.")
				eventCheck[7]["event"] = 1
			elif playerInput.lower() == ("move north") or playerInput.lower() == ("m n"):
				eventNumber = 1
			elif playerInput.lower() == ("move south") or playerInput.lower() == ("m s"):
				if eventCheck[7]["event"] == 0:
					print("------------------------------------------------------------")
					print("The door appears to be locked.")
				else:
					eventNumber = 5
			elif playerInput.lower() == ("move east") or playerInput.lower() == ("m e"):
				eventNumber = 8
			elif playerInput.lower() == ("move west") or playerInput.lower() == ("m w"):
				eventNumber=6
			elif playerInput.lower() == ("check inventory"):
				DisplayInventory(playerInventory)
			elif playerInput.lower() == ("help commands"):
				HelpCommands()
			else:
				print("I do not understand your input of " + "'" + playerInput + "'")
	# =====================================================================================

	# EVENT CELL 8 CORNER CORRIDOR WITH POSTER
	# =====================================================================================
	while eventNumber == 8:
		print("------------------------------------------------------------")
		if eventNumber == 8:
			if eventCheck[8]["visited"] == 0:
				print("You enter the north end of the corridor.")
				print("There in front of you is a sign that says: ")
				print("'AIRLOCK WEST: DOCKING PORT 1, DOCKING PORT 2'.")
				eventCheck[8]["visited"] = 1
			elif eventCheck[8]["visited"] == 1:
				print("You are in the north end of the corridor with the sign.")

			if eventCheck[8]["objects"]:
				print("------------------------------------------------------------")
				print("Objects in this room: ")
				for x in range(len(eventCheck[8]["objects"])):
					print(eventCheck[8]["objects"][x])

			print("------------------------------------------------------------")
			# CHECKS IF ROOM 10 HAS BEEN VISITED OR NOT
			if eventCheck[10]["visited"] == 0:
				print("To your north is a door with porthole.")
			elif eventCheck[10]["visited"] == 1:
				print("To your north is the airlock controls room.")
			
			# CHECKS IF ROOM 7 HAS BEEN VISITED OR NOT
			if eventCheck[7]["visited"] == 0:
				print("To your west is a door that leads somewhere...")
			elif eventCheck[7]["visited"] == 1:
				print("To your west is a door leads to the rec room.")


			print("What will you do?")
			playerInput = input()

			if playerInput.lower() == ("read poster") or playerInput.lower() == ("view poster"):
				print("------------------------------------------------------------")
				print("The poster is a recruitment poster for underwater bases.")
			elif playerInput.lower() == ("look out porthole") or playerInput.lower() == ("view porthole"):
				print("------------------------------------------------------------")
				print("You can't see inside due to being all dirty & fogged up...")
			elif playerInput.lower() == ("move north") or playerInput.lower() == ("m n"):
				eventNumber = 10
			elif playerInput.lower() == ("move south") or playerInput.lower() == ("m s"):
				print("------------------------------------------------------------")
				print("There is a wall and a poster in the way.")
			elif playerInput.lower() == ("move east") or playerInput.lower() == ("m e"):
				print("------------------------------------------------------------")
				print("There is a wall in the way.")
			elif playerInput.lower() == ("move west") or playerInput.lower() == ("m w"):
				eventNumber = 7
			elif playerInput.lower() == ("check inventory"):
				DisplayInventory(playerInventory)
			elif playerInput.lower() == ("help commands"):
				HelpCommands()
			else:
				print("I do not understand your input of " + "'" + playerInput + "'")
	# =====================================================================================

	# EVENT CELL 9 SUPPLY CLOSET
	# =====================================================================================
	while eventNumber == 9:
		if eventNumber == 9:
			print("------------------------------------------------------------")
			if eventCheck[9]["visited"] == 0:
				print("You enter a small dark room with cleaning supplies in here.")
				print("This is the supply closet.")
				eventCheck[9]["visited"] = 1
			elif eventCheck[9]["visited"] == 1:
				print("You are in the supply closet.")
			
			if eventCheck[9]["objects"]:
				print("------------------------------------------------------------")
				print("In this room there: ")
				for x in range(len(eventCheck[9]["objects"])):
					print(eventCheck[9]["objects"][x])

			print("------------------------------------------------------------")
			# CHECKS IF ROOM 10 HAS BEEN VISITED OR NOT
			if eventCheck[10]["visited"] == 0:
				print("To your south is a door.")
			elif eventCheck[10]["visited"] == 1:
				print("To your south is the airlock controls room.")

			print("What will you do?")
			playerInput = input()

			if playerInput.lower() == ("move north") or playerInput.lower() == ("m n"):
				print("------------------------------------------------------------")
				print("You are just met with a wall here.")
			elif playerInput.lower() == ("move south") or playerInput.lower() == ("m s"):
				eventNumber = 10
			elif playerInput.lower() == ("move east") or playerInput.lower() == ("m e"):
				print("------------------------------------------------------------")
				print("You are just met with a wall here.")
			elif playerInput.lower() == ("move west") or playerInput.lower() == ("m w"):
				print("------------------------------------------------------------")
				print("You are just met with a wall here.")
			elif playerInput.lower() == ("check inventory"):
				DisplayInventory(playerInventory)
			elif playerInput.lower() == ("help commands"):
				HelpCommands()
			else:
				print("I do not understand your input of " + "'" + playerInput + "'")
	# =====================================================================================

	# EVENT CELL 10 AIRLOCK CONTROL ROOM
	# =====================================================================================
	while eventNumber == 10:
		if eventNumber == 10:
			print("------------------------------------------------------------")
			if eventCheck[10]["visited"] == 0:
				print("You enter a room with many blinking lights and controls.")
				print("There seems to a button with the labels under them ")
				print("called 'Airlock West', and 'Airlock East'.")
				print("This must be the airlock control room.")
				eventCheck[10]["visited"] = 1
			elif eventCheck[10]["visited"] == 1:
				print("You are in the Airlock control room.")
				print("There's a button labeled 'Airlock West' & 'Airlock East'.")
			
			if eventCheck[10]["objects"]:
				print("------------------------------------------------------------")
				print("In this room there: ")
				for x in range(len(eventCheck[10]["objects"])):
					print(eventCheck[10]["objects"][x])

			print("------------------------------------------------------------")
			# CHECKS IF ROOM 0 HAS BEEN VISITED OR NOT
			if eventCheck[0]["visited"] == 0:
				print("To your west is a room of mysterious intent.")
			elif eventCheck[0]["visited"] == 1:
				print("To your west is the room where you woke up in.")

			# CHECKS IF ROOM 9 HAS BEEN VISITED OR NOT
			if eventCheck[9]["visited"] == 0:
				print("To your north is a door.")
			elif eventCheck[9]["visited"] == 1:
				print("To your north is a supply closet.")
			
			# CHECKS IF ROOM 11 HAS BEEN VISITED OR NOT
			if eventCheck[11]["visited"] == 0:
				print("To your east is a door with a valve on it.")
			elif eventCheck[11]["visited"] == 1:
				print("To your east is the Captain's quarters.")

			# CHECKS IF ROOM 8 HAS BEEN VISITED OR NOT
			if eventCheck[8]["visited"] == 0:
				print("To your south is a room door that has a porthole.")
			elif eventCheck[8]["visited"] == 1:
				print("To your south is a corridor with the poster.")

			print("What will you do?")
			playerInput = input()

			if playerInput.lower() == ("look out porthole") or playerInput.lower() == ("view porthole"):
				print("------------------------------------------------------------")
				print("You can't see outside due to being all dirty & fogged up...")
			elif playerInput.lower() == ("break window") or playerInput.lower() == ("smash window"):
				print("------------------------------------------------------------")
				print("It would be not wise to break this window...")
			elif playerInput.lower() == ("push button") or playerInput.lower() == ("press button"):
				print("------------------------------------------------------------")
				if eventCheck[5]["event"] == 1 and eventCheck[10]["event"] == 0:
					print("Loud alarms ring off and a red light flashes around.")
					print("A loudspeaker states 'Airlock doors are now open'.")
					eventCheck[10]["event"] == 1
				elif eventCheck[5]["event"] == 0 and eventCheck[10]["event"] == 0:
					print("Nothing happens.")
				elif eventCheck[5]["event"] == 1 and eventCheck[10]["event"] == 1:
					print("Nothing happens but the alarms are still ringing.")
			elif playerInput.lower() == ("move north") or playerInput.lower() == ("m n"):
				eventNumber = 9
			elif playerInput.lower() == ("move south") or playerInput.lower() == ("m s"):
				eventNumber = 8
			elif playerInput.lower() == ("move east") or playerInput.lower() == ("m e"):
				eventNumber = 11
			elif playerInput.lower() == ("move west") or playerInput.lower() == ("m w"):
				eventNumber = 0
			elif playerInput.lower() == ("check inventory"):
				DisplayInventory(playerInventory)
			elif playerInput.lower() == ("help commands"):
				HelpCommands()
			else:
				print("I do not understand your input of " + "'" + playerInput + "'")
	# =====================================================================================

	# EVENT CELL 11 CAPTAIN'S QUARTERS
	# =====================================================================================
	while eventNumber == 11:
		if eventNumber == 11:
			print("------------------------------------------------------------")
			if eventCheck[11]["visited"] == 0:
				print("You enter a room with a bed, a shelf, and a desk.")
				print("There seems to a handwritten paper on the desk ")
				print("labeled 'Captain's Log ")
				print("This must be the Captain's quarters.")
				eventCheck[11]["visited"] = 1
			elif eventCheck[11]["visited"] == 1:
				print("You are in the Captain's Quarters.")
			
			if eventCheck[11]["objects"]:
				print("------------------------------------------------------------")
				print("In this room there: ")
				for x in range(len(eventCheck[11]["objects"])):
					print(eventCheck[11]["objects"][x])

			print("------------------------------------------------------------")
			# CHECKS IF ROOM 10 HAS BEEN VISITED OR NOT
			if eventCheck[10]["visited"] == 0:
				print("To your west is a room of mysterious intent.")
			elif eventCheck[10]["visited"] == 1:
				print("To your west is the airlock control room.")

			print("What will you do?")
			playerInput = input()

			if playerInput.lower() == ("read log") or playerInput.lower() == ("view log"):
				print("------------------------------------------------------------")
				print("You look at the log:")
				print("It states that they are abandoning the station")
			elif playerInput.lower() == ("move north") or playerInput.lower() == ("m n"):
				print("------------------------------------------------------------")
				print("There is a desk in the way")
			elif playerInput.lower() == ("move south") or playerInput.lower() == ("m s"):
				print("------------------------------------------------------------")
				print("There is a shelf in the way")
			elif playerInput.lower() == ("move east") or playerInput.lower() == ("m e"):
				print("------------------------------------------------------------")
				print("There is a bed here can't go any further.")
			elif playerInput.lower() == ("move west") or playerInput.lower() == ("m w"):
				eventNumber = 10
			elif playerInput.lower() == ("check inventory"):
				DisplayInventory(playerInventory)
			elif playerInput.lower() == ("help commands"):
				HelpCommands()
			else:
				print("I do not understand your input of " + "'" + playerInput + "'")
	# =====================================================================================
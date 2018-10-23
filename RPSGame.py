print("Rules that govern the state of water")
current_temp = False
while current_temp is False:
	current_temp = input("Enter a temperature:\n")
	print("you unput:", current_temp)
	if (int(current_temp) < 0 or (int(current_temp) == 0)):
		print("Water is a solid! cuzit's at or below freezing")
		current_temp = False

	elif (int(current_temp) < 100):
		print("water is a liquid! because it's above preezing and below boiling")
		current_temp = False
	elif (int(current_temp) > 100 or (int(current_temp) == 100)):
		print("Water is a gas! because it is.. extremly hot")
		current_temp = False
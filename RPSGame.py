from random import randint

choices = ["Rock","Paper","Scissors"]

computer_choice = choices[randint(0,2)]

player_life = 3

computer_life = 3



player = False

while player == False:

	print("Your lives: ", player_life)

	print("Computer lives: ", computer_life)

	print("Choose your weapon!")

	player = input("Rock, Paper or Scissors ?\n")


	if player == "quit":

		exit()

	print("Player chooses:", player)

	print("Computer chooses: ", computer_choice)

	

	if player == "restart":

		player_life = 3

		computer_life = 3

		player = False

		computer_choice = choices[randint(0,2)]


	if player == computer_choice:

		print("Tie! You live to try again!")

	elif player == "Rock":

		if computer_choice == "Scissors":

			computer_life = computer_life - 1

			print("You win!", player, "smashes" ,computer_choice)

			

		else:

			player_life = player_life - 1

			print("You lose!", computer_choice, "smashes" , player)

			

	elif player == "Scissors":

		if computer_choice == "Paper":

			computer_life = computer_life - 1

			print("You win!", player, "smashes" ,computer_choice)

		else:

			player_life = player_life - 1

			print("You lose!", computer_choice, "smashes" , player)

			



	elif player == "Paper":

		if computer_choice == "Rock":

			computer_life = computer_life - 1

			print("You win!", player, "smashes" ,computer_choice)

			

		else:

			player_life = player_life - 1

			print("You lose!", computer_choice, "smashes" , player)

	

	else:

		print("Rock, Paper, or Scissors")


	player = False

	computer_choice = choices[randint(0,2)]
	

	while player_life == 0:

		print()

		print("Your lives: ", player_life)

		print("Computer lives: ", computer_life)

		print("Rauugh! You have been Terminated! Try again!")

		player = input("restart or quit ??\n")

		if player == "restart":

			player_life = 5

			computer_life = 5

			player = False

			computer_choice = choices[randint(0,2)]



		if player == "quit":

				exit()

		else:

			print("Check your spelling ...")
	

	while computer_life == 0:

		print()

		print("Your lives: ", player_life)

		print("Computer lives: ", computer_life)

		print("No fair! You beat me! Meh.. -3-")

		player = input("restart or quit ??\n")

		if player == "restart":

				player_life = 5

				computer_life = 5

				player = False

				computer_choice = choices[randint(0,2)]

		if player == "quit":

				exit()

		else:

			print("Rock, Paper, or Scissors")

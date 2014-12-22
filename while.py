number = 40
running = True

while(running):

	guess = int(input('Enter an integer : '))

	if guess>number:
		print("No! its a little lower")

	elif guess<number:
		print("No! its a little higher")

	else:
		print("you are correct! The number is {0}".format(number))
		running = False;
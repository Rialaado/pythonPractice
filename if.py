number = 23
guess = int(input('Enter an Integer: '))



if guess == number:
	print ('congratulations you guessed it')
	print ('but you dont win any prizes :-(')
elif guess < number:
	print ('no, it is a little higher than that')
else:
	print ('no, its a little lower than that')


print ('done')
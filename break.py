while(True):
	userInput = input("please enter anything!")
	if userInput == "quit":
		break
	else: 
		leng = len(userInput)
		print("the lenght of the inputted string is: ", leng)
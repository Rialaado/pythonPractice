while(True):
	s = input("Enter Something")
	if s == "quit":
		break
	elif len(s)<3:
		print("too small!")
		continue

	print ("input is of sufficient lenght!")
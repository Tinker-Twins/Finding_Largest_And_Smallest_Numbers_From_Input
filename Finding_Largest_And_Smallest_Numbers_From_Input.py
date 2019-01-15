largest = None
smallest = None

while True:
	num = input("Enter a number: ")

	if num == "done":
		break
	else:
		try:
			i = int(num)
		except:
			i = -1
		if i < 0:
			print("Invalid input")
			continue
		else:
			if smallest is None:
				smallest = i
			if i < smallest:
				smallest = i
			if largest is None:
				largest = i
			if i > largest:
				largest = i
print("Maximum is",largest)
print("Minimum is",smallest)

total = 0

while True:
	color = input()
	if color == "white":
		total += 1000
	elif color == "yellow":
		total += 2000
	elif color == "blue":
		total += 3000
	elif color == "red":
		total += 5000
	else:
		break

print(f"Total price = {total}")

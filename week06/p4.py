sum = 0

for i in range(10):
	color = input()
	if color == "yellow":
		continue
	if color == "red":
		break
	dice = int(input())
	sum += dice

print(f"Sum = {sum}")
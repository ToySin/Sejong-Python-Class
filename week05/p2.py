total = 0
count = 0

while True:
	dice = int(input())
	total += dice;
	count += 1
	if dice == 4:
		break

print(f"Count = {count}, Total = {total}")
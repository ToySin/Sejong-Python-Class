count = 0
total = 0

while True:
	if total >= 20:
		break
	dice = int(input())
	if dice != 4:
		total += dice
	count += 1

print(f"Count = {count}")
print(f"Total = {total}")
count = 0
total = 0

while True:
	if total >= 20:
		break
	dice = int(input())
	count += 1
	if dice == 4:
		break
	total += dice
	

print(f"Count = {count}")
print(f"Total = {total}")
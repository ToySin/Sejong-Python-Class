n = int(input())
num = 1
factorial = 1

while True:
	if factorial >= n:
		break
	factorial *= num
	num += 1

print(f"Num = {num - 1}")
print(f"Total = {factorial}")
n = int(input())
m = int(input())

for i in range(1, n + 1):
	for j in range(1, n + 1):
		if i == m:
			print("*", end="")
		elif j == m:
			print("*", end="")
		else:
			print(" ", end="")
	print()
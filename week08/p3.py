n1 = int(input())
n2 = int(input())

for h in range(0, n1 + 1):
	for m in range(0, 60):
		if (h == n1) and (m > n2):
			break
		print(f"{h:02d}:{m:02d}")
def enlarge(n):
	if n > 0:
		return n + 1
	if n < 0:
		return n - 1


n = int(input())

print(enlarge(n))
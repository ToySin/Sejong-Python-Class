def isEven(n):
	return n % 2 == 0


def countEvenNums(n):
	cnt = 0
	for i in range(1, n + 1):
		if isEven(i):
			cnt += 1
	return cnt


n = int(input())
print("The number of evens is", countEvenNums(n))
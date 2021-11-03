def isInList(n, num_list):
	for num in num_list:
		if num == n:
			return True
	return False
	

n = int(input())

num_list = []

for _ in range(n):
	num_list.append(int(input()))

while True:
	n = int(input())
	if n == 0:
		break
	elif n in num_list:
		print("YES")
	else:
		print("NO")



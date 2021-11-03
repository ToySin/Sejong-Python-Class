def isInList(n, num_list):
	for num in num_list:
		if num == n:
			return True
	return False
	

num_list = []

for _ in range(10):
	num = int(input())
	if num in num_list:
		print("exist")
	else:
		num_list.append(num)
	
print(num_list)
n = int(input())

num_list = []

for _ in range(n):
	num_list.append(int(input()))

index = int(input())

print(num_list[n - 1 - index])


# 0 1 2 3 ... n-2 n-1

# 0 -> n-1
# 1 -> n-2 -> n-1 - 1
# 2 -> n-3 -> n-1 - 2

# n-1 -> 0 -> n-1 - (n-1) = 0
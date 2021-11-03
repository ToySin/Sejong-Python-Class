def bubble_sort(num_list):
	for i in range(4):
		for j in range(4 - i):
			if num_list[j] > num_list[j + 1]:
				# swap
				num_list[j], num_list[j + 1] = num_list[j + 1], num_list [j]


num_list = []

for _ in range(5):
	num_list.append(int(input()))

print(f"before = {num_list}")

bubble_sort(num_list)

print(f"after = {num_list}")

# 0 1 2 3 4
# * * (a, b) 큰 수를 b에 위치시킵니다.
#   * *
#     * * .. * * 거품처럼 붙어서 이동하면서 정렬한다고
# 버블정렬이라고 부릅니다.

# 5 4 3 2 1
# 4 5 3 2 1
# 4 3 5 2 1
# 제일 큰 값이 제일 뒤로 보내진다.
# 4 3 2 1 5
# 제일 뒤에 제일 큰값이 위치했다. (제일 뒷자리는 정렬되었다.)
# 3 2 1 4 5

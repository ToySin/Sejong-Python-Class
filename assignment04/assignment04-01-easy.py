# Assignment 04-01 easy

N = int(input())

info = []
for _ in range(N):
	info.append(sum(list(map(int, input().split()))))

for i in range(N - 1):
	for j in range(N - 1 - i):
		if info[j] < info[j + 1]:
			info[j], info[j + 1] = info[j + 1], info[j]

total = 0

# a = [1, 2, 2, 2, 1, 3]
# a.count(1) -> 2
# a.count(2) -> 3
# a.count(3) -> 1

first_next_index = info.count(info[0])
total += first_next_index * 100

if first_next_index < N:
	second_next_index = info.count(info[first_next_index])
	total += second_next_index * 80

	if first_next_index + second_next_index < N:
		third_next_index = info.count(info[second_next_index])
		total += third_next_index * 50

print(total)

"""
5
50 60 100
80 60 50
80 70 100
50 60 90
60 80 100
"""

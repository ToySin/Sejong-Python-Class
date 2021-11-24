N = int(input())

info = [[], [], []]
for _ in range(N):
	score = list(map(int, input().split()))
	info[0].append(score[0])
	info[1].append(score[1])
	info[2].append(score[2])

class_name = ["SW", "OS", "DB"]
for i in range(3):
	print(f"Average({class_name[i]}) = \
		{sum(info[i]) // N}")

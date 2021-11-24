scores = []
for _ in range(8):
	scores.append(int(input()))

# bubble
for i in range(8 - 1):
	for j in range(8 - 1 - i):
		if scores[j] < scores[j + 1]:
			scores[j], scores[j + 1] = \
				scores[j + 1], scores[j]

# selection
# 1 5 4 3 2
# 5 4 3 2 1

# i = 0
# 1 5 4 3 2 -> max -> 5
# 5 1 4 3 2

# i = 1
# 5 | 1 4 3 2 -> max -> 4
# 5 | 4 1 3 2

# i = 2
# 5 4 | 1 3 2 ........
for i in range(8 - 1):
	max_index = scores.index(max(scores[i: ]))
	scores[i], scores[max_index] = \
		scores[max_index], scores[i]

for score in scores:
	print(score)

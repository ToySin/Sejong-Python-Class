s = []

while True:
	score = int(input())
	if score == 0:
		break
	s.append(score)

print(s)
print(f"Avg = {sum(s) / len(s):.2f}")

"""
list_len = 0
for _ in s:
	list_len += 1
"""
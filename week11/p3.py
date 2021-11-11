n = int(input())

s = []
for _ in range(n):
	s.append(int(input()))

print(s)
print(f"Avg = {sum(s) / len(s):.2f}")
# print("Avg = %.2f" % sum(s) / len(s))

"""
total = 0
for score in s:
	total += score

print(total / n)
"""
n = int(input())

s = []

for i in range(n):
	kor_score = int(input())
	s.append(kor_score)

print(f"max = {max(s)}")
print(f"min = {min(s)}")

# print("max = %d" % max(s))
# print("min = %d" % min(s))
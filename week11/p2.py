s = [8, 6, 9, 10, 4, 7, 10, 6, 8, 7]

print(f"s = {s}")
max_index = 0
for i in range(10):
	if s[max_index] < s[i]:
		max_index = i

print(f"Max = {s[max_index]}")
print(f"Idx = {max_index}")

# max_value = s[max_index]
# print(s.index(max_value))
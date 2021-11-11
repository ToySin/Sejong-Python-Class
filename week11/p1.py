a = [2, 3, 1, 4]

print(f"a = {a}")
max_value = a[0]
for i in range(4):
	if max_value < a[i]:
		max_value = a[i]
	print(i, max_value)
print(f"Max = {max_value}")
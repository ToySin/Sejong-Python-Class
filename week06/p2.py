num = int(input())

sum1 = 0
sum2 = 0

for i in range(1, num + 1):
	if i % 2:
		sum1 += i
	else:
		sum2 += i

print(f"Sum1 = {sum1}")
print(f"Sum2 = {sum2}")
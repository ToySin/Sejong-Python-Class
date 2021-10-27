n1 = int(input())
n2 = int(input())
n3 = int(input())

min_value = n1;
if min_value > n2:
	min_value = n2
if min_value > n3:
	min_value = n3

print(f"Min = {min_value}")

# print(f"Min = {min(n1, n2, n3)})
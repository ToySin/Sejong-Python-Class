## solution 1
height, gender = input().split()
# (180 M).split() -> heigt = '180', gender = 'M'
height = int(height) / 100

## solution 2
# info = input().split()
# (180 M).split() -> ['180', 'M']
# info[0] = int(info[0]) / 100


if gender == 'M':
	standard_weight = height * height * 22
elif gender == 'F':
	standard_weight = height * height * 21

print(f"{standard_weight:.1f}kg")

# print("%.1fkg" % standard_weight)
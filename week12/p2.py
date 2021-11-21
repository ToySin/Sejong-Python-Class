score = [
		[90, 80, 100, 70, 80, 90, 100, 90], \
		[60, 30, 90, 90, 85, 80, 75, 70], \
		[85, 60, 99, 100, 90, 80, 70, 60]]

min_0, min_1, min_2 = 0, 0, 0 #min_index

for i in range(8):
	if score[0][i] < score[0][min_0]:
		min_0 = i
	if score[1][i] < score[1][min_1]:
		min_1 = i
	if score[2][i] < score[2][min_2]:
		min_2 = i

print(f"Min[0] = {score[0][min_0]}")
print(f"Min[1] = {score[1][min_1]}")
print(f"Min[2] = {score[2][min_2]}")

"""
for i in range(3) : 
    min = score[i][0]
    for j in range(8) :
        if score[i][j] < min :
            min = score[i][j]
    print("Min[%d] = %d" %(i, min)) 
"""
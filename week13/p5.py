grade = [
	['C', 'B', 'A', 'C', 'D'],
	['F', 'D', 'C', 'D', 'B'],
	['A', 'B', 'A', 'B', 'A'],
	['A', 'A', 'B', 'C', 'D'],
	['B', 'B', 'B', 'B', 'B'],
	['B', 'B', 'C', 'D', 'F'],
	['C', 'A', 'A', 'A', 'A'],
	['D', 'A', 'A', 'C', 'F']
]

credit = [3, 3, 3, 2, 1]

rating = {
	'A': 4.0,
	'B': 3.0,
	'C': 2.0,
	'D': 1.0,
	'F': 0.0
}

students_avg = []
for i in range(8):
	student_sum = 0
	for j in range(5):
		student_sum += credit[j] * rating[grade[i][j]]
	students_avg.append(student_sum / 12)

for i in range(8):
	print(f"{i + 1} {students_avg[i]:.2f}")

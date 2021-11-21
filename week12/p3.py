num = int(input())

score = []

for i in range(num):
	# score.append(list(map(int, input().split())))
	score.append(input().split()) # string ""

for i in range(num):
	for j in range(3):
		score[i][j] = int(score[i][j])

for i in range(num):
	average = round(sum(score[i]) / len(score[i]), 2) # %.2f->x
	print(f"Student {i + 1}'s Average Score : {average}")


"""
for i in range(num):
    total = 0
    for j in range(3):
        total += int(score[i][j])
    avg = round(total/3, 2)
    print("Student " + str(i+1) + "'s Average Score :", avg)
"""

# map
"""
list(map(int, input().split()))

input().split() -> 한줄로 입력받아서 ' '공백으로 구분해서 "문자열"로 나눈
리스트를 생성.

12 34 56
["12", "34", "56"] -> list

map() -> list, dict, tuple 이 자료형의 각 원소에 적용시킬 규칙
map(int, ["12", "34", "56"])
map int->각 원소에 적용시킵니다.
([12, 34, 56])이라는 list를 만들수있는 map자료형의 설계도를 만들어줍니다.
<map object at 0x000002CD08592F80>

score.append(list(map(int, input().split())))
score -> [
	[12, 34, 56],
	[34, 56, 78],
]
"""
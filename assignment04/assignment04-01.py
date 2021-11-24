# Assignment 04-01

N = int(input())

info = []
for _ in range(N):
	info.append(list(map(int, input().split())))

# bubble sort
for i in range(N - 1):
	for j in range(N - 1 - i):

		# 국어점수를 먼저 내림차순으로 정렬
		if info[j][0] < info[j + 1][0]:
			info[j], info[j + 1] = info[j + 1], info[j]

		# 국어점수가 동점일 경우
		elif info[j][0] == info[j + 1][0]:

			# 수학점수를 내림차순으로 정렬
			if info[j][1] < info[j + 1][1]:
				info[j], info[j + 1] = info[j + 1], info[j]

			# 수학점수도 동점인 경우
			elif info[j][1] == info[j + 1][1]:

				# 영어점수를 내림차순으로 정렬
				if info[j][2] < info[j + 1][2]:
					info[j], info[j + 1] = info[j + 1], info[j]

# 여기까지 왔다면 높은 등수대로 리스트가 정렬됨
# 동점자들은 근접하게 정렬되어있습니다.
# 1등 1등 2등 3등 -> o
# 1등 2등 1등 3등 -> x

# 총 장학금
total = 0

# 현재 몇번째 학생의 등수를 체크하는가?
index = 0

# 구현구조
# 현재 등수 순서대로 학생들이 정렬되어 있습니다.
# 1등부터 몇명인지 세면서 장학금을 더하고
# 2등이 몇명인지 세면서 장학금을 더하고
# 3등이 몇명인지 세면서 장학금을 더한 후
# 그 이후는 세지 않습니다.
# (계산식 블럭이 3개 -> 1등 2등 3등만 계산)

# 조건설명
# if index < N
# 인덱스가 학생 수 범위를 벗어나지 않았는지 확인한다.
# 학생이 3명인데 3명 모두 1등인 경우
# 더 이상 진행하면 안되기 때문입니다.
# 따라서 매 블럭마다 위 조건을 추가했습니다.

# rank_index = int(index)
# 1등은 첫번째 학생 (index -> 0)
# 2등은 1등 학생들을 다 지나고 등장하는 첫번째 학생
# 3등은 2등 학생들을 다 지나고 등장하는 첫번째 학생

# while index < N
# 반복문을 돌면서 등수를 계산할 때
# 인덱스가 학생 수 범위를 벗어나지 않았는지 확인합니다.
# 학생이 3명인데 3명 모두 1등인 경우
# 반복문 도중에 빠져나올 조건이 필요합니다.

# if not is_same(info[rank_index], info[index])
# rank_index에는 1, 2, 3등 학생의 정보가 있습니다.
# 그 기준 정보와 현재 index의 정보를 비교해서 다르다면
# 현재 rank의 학생들을 다 센것입니다.
# 만약 2명의 학생
# 100 90 80
# 100 80 90
# 학생 두명이 있을 때, 단순히 총합만으로 계산하면
# 1등 두명 -> 200만원이 나옵니다.
# 하지만 문제 조건대로 계산 시,
# 위 학생이 1등, 아래 학생이 2등 -> 180만원이 나옵니다.
# 따라서 단순히 총합이 같은 지 비교하는 것이 아닌,
# 국어, 영어, 수학 각 점수 모두가 같은 지 비교해야합니다.


# 1등 계산 블럭
# 1등 블럭에서는 if index < N, first_index = int(index)
# 두 문장이 필요없지만, 이해하기 편하시라고 통일했습니다.
if index < N:
	first_index = int(index)
	while index < N:
		if info[first_index] != info[index]:
			break
		index += 1
		total += 100

# 2등 계산 블럭
if index < N:
	second_index = int(index)
	while index < N:
		if info[second_index] != info[index]:
			break
		index += 1
		total += 80

# 3등 계산 블럭
if index < N:
	third_index = int(index)
	while index < N:
		if info[third_index] != info[index]:
			break
		index += 1
		total += 50

# 만약 index < N이라도 3등까지만 계산하고
# 4..5..6... 이후의 등수는 계산하지 않는다.

print(total)

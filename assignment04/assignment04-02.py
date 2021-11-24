# Assignment 04-02

n = int(input())

info = []
for _ in range(n):
	score = []
	for _ in range(3):
		score.append(int(input()))
	info.append(score)

print(info)

avg_info = []
for info_list in info:
	avg_info.append(sum(info_list) / 3)

print(f"1st score = {info[avg_info.index(max(avg_info))]}")

print(f"1st avg = {max(avg_info):.2f}")

kor = []
eng = []
math = []
for i in range(n):
	kor.append(info[i][0])
	eng.append(info[i][1])
	math.append(info[i][2])

print(f"korean = {max(kor)}, english = {max(eng)}, math = {max(math)}")

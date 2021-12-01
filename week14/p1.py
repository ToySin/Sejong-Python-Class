name = input()
n = int(input())

fp = open(name, "w")
for i in range(1, n + 1):
	fp.write(f"{i}\n"); # 총 1개의 인자, 문자열 형태 5
fp.close()


# 'r' 읽기 전용
# 'r+' 기존 파일에 있던 데이터 위에 입력

# 'w' 쓰기 전용
# 'w+' 기존 파일에 있던 데이터를 완전 지우고 입력

# 'a' 쓰기 전용(추가)
# 'a+' 기존 파일에 있던 데이터에 추가

print()

fp = open("plus_oper.txt", 'w')
fp.write("Hello, world!")
fp.close()

fp = open("plus_oper.txt", 'r')
print(f"Before w+ : {fp.read()}")
fp.close()

fp = open("plus_oper.txt", 'w+')
fp.write("Hi, python.")
fp.close()

fp = open("plus_oper.txt", 'r')
print(f" After w+ : {fp.read()}")
fp.close()

print()

fp = open("plus_oper.txt", 'w')
fp.write("Hello, world!")
fp.close()

fp = open("plus_oper.txt", 'r')
print(f"Before r+ : {fp.read()}")
fp.close()

fp = open("plus_oper.txt", 'r+')
fp.write("Hi, python.")
fp.close()

fp = open("plus_oper.txt", 'r')
print(f" After r+ : {fp.read()}")
fp.close()

print()

fp = open("plus_oper.txt", 'w')
fp.write("Hello, world!")
fp.close()

fp = open("plus_oper.txt", 'r')
print(f"Before a+ : {fp.read()}")
fp.close()

fp = open("plus_oper.txt", 'a+')
fp.write("Hi, python.")
fp.close()

fp = open("plus_oper.txt", 'r')
print(f" After a+ : {fp.read()}")
fp.close()

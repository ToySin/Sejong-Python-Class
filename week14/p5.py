string = " ".join(input().split())
n = int(input())

fp = open("python.txt", 'w')
fp.write(string)
fp.close()

fp = open("python.txt", 'r')
fp.seek(n)
print(f"{n} bytes: {fp.read(1)}")
fp.close()

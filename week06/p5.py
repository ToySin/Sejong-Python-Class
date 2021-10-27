n = int(input())

for i in range(n + 1):
	if i > 23:
		break
	print(f"{i:02d} : 00")
	#print("%02d : 00" % i)
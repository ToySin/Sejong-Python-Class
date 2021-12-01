total = 0;

fp = open("test.txt", 'r')

# line = fp.read(5)
# print(line)
# line = fp.readlines()
# print(line)
# line = fp.readline()
# print(line)

while True:
	line = fp.readline()
	if not line:
		break
	total += int(line)
fp.close()

print(f"Total = {total}")

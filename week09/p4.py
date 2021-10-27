def get_gcd_euclidean(n1, n2): # n1 > n2
	if n2 == 0:
		return n1
	else:
		return get_gcd_euclidean(n2, n1 % n2)


def get_gcd_normal1(n1, n2): # n1 > n2
	max_div = 1
	for div in range(1, n2 + 1):
		if (n1 % div == 0) and (n2 % div == 0):
			max_div = div
	return max_div


def get_gcd_normal2(n1, n2): # n1 > n2
	for div in range(n2, 0, -1):
		if (n1 % div == 0) and (n2 % div == 0):
			return div


n1 = int(input())
n2 = int(input())

if n1 < n2:		# n1 > n2
	n1, n2 = n2, n1

print(get_gcd_normal2(n1, n2))




##
# if 8 and 6, 5 and 4
# gcd is 2
#
# 8 case
# ㅁ ㅁ ㅁ ㅁ ㅁ ㅁ ㅁ ㅁ
#
# 6 case
# ㅁ ㅁ ㅁ ㅁ ㅁ ㅁ 
#
# 8 % 6
# ㅁ ㅁ
# ㅁ ㅁ ㅁ ㅁ ㅁ ㅁ
#
# 6 % 2
# ㅁ ㅁ
# X

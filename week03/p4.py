dice1 = int(input())
dice2 = int(input())

if dice1 + dice2 <= 5:
	print("sum <= 5")

elif dice1 + dice2 < 10:
	print("5 < sum < 10")

else:
	print("sum >= 10")
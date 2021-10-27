dice1 = int(input())
dice2 = int(input())

if (dice1 % 2) and (dice2 % 2):
	print("All dices are odd!")

elif (dice1 % 2 == 0) and (dice2 % 2 == 0):
	print("All dices are even!")
user_info = {
	'name':'David',
	'age':21,
	'address':'Gwangjin-gu, Seoul'
}

N = int(input())
print()

for i in range(N):
	print(f"Edit #{i + 1}")
	key = input()
	value = input()
	user_info[key] = value
# studentID key -> new? create key:value
# address key -> old? update key:value

print()
print("USER INFO")
for key in user_info: # dict's key iter
	print(f"{key} : {user_info[key]}")
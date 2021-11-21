user_info = {	# key:item
	'id':'software',
	'pw':'python',
}

print(user_info[0])

# variable id, pw
# key 'id', 'pw'
id = input()
pw = input()

key1 = 'id'

# dict[key] -> item return
if id != user_info[key1]:
	print("ID Mismatch!")
elif pw != user_info['pw']:
	print("PW Mismatch!")
else:
	print("Success in Login")
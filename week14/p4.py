menu_count = int(input("The number of menu: "))

fp = open("menu.txt", 'w')
for _ in range(menu_count):
	fp.write(input("Menu name: "))
	fp.write(" ")
	fp.write(input("Menu price: ") + "\n")
fp.close()

fp = open("menu.txt", 'r')
print(fp.read())
fp.close()


menu_dict = {}

fp = open("menu.txt", 'r')

lines = fp.readlines()
print(lines)

for _ in range(menu_count):
	lines = fp.readline().split()
	menu_name = " ".join(lines[:-1])
	menu_price = int(lines[-1])
	menu_dict[menu_name] = menu_price
fp.close()

print(menu_dict)

for menu_name in menu_dict:
	print(f"{menu_name}: {menu_dict[menu_name]}")

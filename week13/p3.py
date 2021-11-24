menu = {
	"salmon roe": 1000,
	"red sea bream": 3000,
	"egg roll": 1000,
	"shrimp": 2000,
	"kimbab": 1000,
	"tuna": 5000,
}

N = int(input())

total = 0
for _ in range(N):
	total += menu[input()]

print(f"Total price = {total}")

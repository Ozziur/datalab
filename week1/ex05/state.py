import sys

states = {
"Oregon" : "OR",
"Alabama" : "AL",
"New Jersey": "NJ",
"Colorado" : "CO"
}
capital_cities = {
"OR": "Salem",
"AL": "Montgomery",
"NJ": "Trenton",
"CO": "Denver"
}

if len(sys.argv) != 2:
	exit(0)
x = capital_cities.values()
trigger = 1
for x, y in capital_cities.items():
	if y == sys.argv[1]:
		for ripa, dav in states.items():
			if x == dav:
				print(ripa)
				trigger=0
if trigger==1:
	print("Unknown state")
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

x = states.keys()
trigger = 1
for n in x:
	if n == sys.argv[1]:
		print(capital_cities[states[sys.argv[1]]])
		trigger=0
if trigger==1:
	print("Unknown state")
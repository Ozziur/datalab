import sys

def valid(str1, str2, str3):
	if any(chr.isalpha() for chr in str1):
		return False
	if any(chr.isalpha() for chr in str2):
		return False
	if any(chr.isalpha() for chr in str3):
		return False
	return True

def minute(min):
	return min * 60

def hour(ho):
	return minute(ho * 60)


if len(sys.argv) == 4:
	if valid(sys.argv[1], sys.argv[2], sys.argv[3]):
		a = int(sys.argv[3])
		b = minute(int(sys.argv[2]))
		c = hour(int(sys.argv[1]))
		print(a+b+c)
	else:
	 	print("caratteri alfabetici non validi")
else:
	print("numero dei valori non valido")
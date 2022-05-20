import sys

def valid(str1, str2):
	if any(chr.isalpha() for chr in str1):
		return False
	if any(chr.isalpha() for chr in str2):
		return False
	return True

if len(sys.argv) == 3:
	if valid(sys.argv[1],sys.argv[2]):
		print(int(sys.argv[1]) + int(sys.argv[2]))
	else:
	 	print("caratteri alfabetici non validi")
else:
	print("numero dei valori non valido")
#Brittany Sloane
#100568757

def has_no_e(string):
	string_index = len(string) - 1
	while(string_index >= 0):
		string_index -= 1
		if string[string_index] == 'e':
			return False
	return True
print(str(has_no_e("without")))
print(str(has_no_e("with e")))


with open('gadsby_stripped.txt') as gadsby_file:
	for line in gadsby_file:
		print(str(has_no_e(line)))



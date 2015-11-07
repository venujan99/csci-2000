#defining the has_no_e function with accepting string as input
def has_no_e(string):
	#defining variable to count letter e
	count_e = 0
	for letter in textfile:
		if letter == 'e':
			#if letter is in file, will increase count 
			count_e += 1
			string = reader.read()
		#if count is equal to zero, then no e were found
	if count_e == 0:
		return 'True - This File Does Not Contains The Letter e'
		#else e was found in the file
	else:
		return 'False - This File Contains The Letter e'	

reader = open('gadsby_stripped.txt', 'r')
textfile = reader.read()
#prints result of program
print(has_no_e(textfile))
#stop reading the file
reader.close()
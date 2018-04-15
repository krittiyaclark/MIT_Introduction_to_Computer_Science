# Assume s is a string of lower case characters.
# Write a program that prints the number of times the string 'bob' occurs in s. 
# For example, if s = 'azcbobobegghakl', then your program should print
# Number of times bob occurs is: 2

# Paste your code into this box 
s = 'azcbobobegghakl'
count = 0
string = 'bob'

for i in range(len(s)):
	if s[i:i+3] == string:
		count = count + 1
print(str(count))

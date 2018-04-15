# Assume s is a string of lower case characters.
# Write a program that counts up the number of vowels contained in the string s. 
# Valid vowels are: 'a', 'e', 'i', 'o', and 'u'. For example, if s = 'azcbobobegghakl', your program should print:
# Number of vowels: 5

# Paste your code into this box 
s = 'azcbobobegghakl'
vowels = 'aeioiu'
count = 0

for i in s:
	if i in vowels:
		count = count + 1
print(count)
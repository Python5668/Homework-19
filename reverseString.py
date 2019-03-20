"""
Loop through the string and push contents
Character by Character onto stack
"""
from stack import Stack
def revString(inputStr):
	s = Stack()
	index = 0 # points to the initial string from the inputStr
	while index in range(len(inputStr)): # while the index is the the range of the string
		s.push(inputStr[index]) # pushing all these letters into a stack starting from the bottom (the 1st letter of the string will now be the last letter of the string)  
		index += 1
	revStr = ''
	while not s.is_empty():
		revStr += s.pop()
	return revStr
print(revString('ENORYT'))

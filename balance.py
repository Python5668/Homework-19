"""
 Use a stack to check whether or not a string has balanced usuage of parenthesis
 example of balanced ones: ({{[]})
 example of unblanced ones: ((),))
"""
# The first version, has some flaws
from stack import Stack
def isMatch(p1,p2):
	if p1 == '(' and p2 == ')':
		return True
	elif p1 == '[' and p2 == ']':
		return True
	elif p1 == '{' and p2 == '}':
		return True
	else:
		return False
def isParenBalanced(parenString):
	index = 0
	isBalanced = True
	s=Stack()
	if parenString == '':
		isBalance = False
		return False
	elif parenString[-1] in '([{':
		isBalanced = False
		return False
	else:
		while index < len(parenString) and isBalanced == True:
			if parenString[index] in '([{':
				s.push(parenString[index])
			else:
				if s.is_empty(): # Added for cases of '())', or '))', or all popped and done
					isbalanced = False # Added
					return False # Added
				elif isMatch(s.pop(), parenString[index]):
					isBalanced = True
				else:
					isBalanced = False
					return False
			index += 1
		if s.is_empty() and isBalanced == True:
			return True
print(isParenBalanced('[]')) # works
print(isParenBalanced('([{}])')) # works
print(isParenBalanced('(([)')) # works
print(isParenBalanced('))')) # works
print(isParenBalanced('((')) # works
print(isParenBalanced('')) # works


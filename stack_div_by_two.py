from stack import Stack
# converting decimal numbers to binary numbers!
def divByTwo(decNum):
	s = Stack() 
	binNum = '' # Empty string that keeps adding binary numbers into it
	while decNum > 0: # Stops when decimal number has been divided down to is zero
		remainder = decNum % 2 # Get remainder
		decNum = decNum // 2 # update decimal number
		s.push(remainder) # push the remainder into a stack, so it'll be at the bottom
	while not s.is_empty(): # Go until the stack is empty
		binNum += str(s.pop()) # keep popping from the stack and adding to the string 
	return binNum
print(divByTwo(15))

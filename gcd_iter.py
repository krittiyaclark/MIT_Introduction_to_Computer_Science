def gcdIter(a, b):
    '''
    a, b: positive integers
    
    returns: a positive integer, the greatest common divisor of a & b.
    '''
    # Your code here
    while a != b:
    	if a > b:
    		a = a - b
    	else:
    		b = b - a
    return a

print(gcdIter(252, 182))
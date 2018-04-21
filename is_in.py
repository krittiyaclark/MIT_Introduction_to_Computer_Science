def isIn(char, aStr):
    '''
    char: a single character
    aStr: an alphabetized string
    
    returns: True if char is in aStr; False otherwise
    '''
    # Your code here

    mid = len(aStr)//2

    # Base case
    if aStr == '' or mid == 0:
        return False
    if char == aStr[mid]:
        return True
    elif char >= aStr[mid]:
        return isIn(char, aStr[mid:] )
    elif char <= aStr[mid]:
        return isIn(char, aStr[:mid])
    else:
        return True


print(isIn('k', 'l'))
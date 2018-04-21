def iterPower(base, exp):
    '''
    base: int or float.
    exp: int >= 0
 
    returns: int or float, base^exp
    '''
    # Your code here

    ## Version 1 ##

	# i = 0
	# result = 1
	# while i < exp:
	# 	result *= base
	#     i += 1   
	# return result

	## Version 2 ##

	result = 1
    for i in range(exp):
        result = result * base
    return result

    ## Version 3 ##

    # result = 1
    # while exp > 0:
    #     result *=base
    #     exp -= 1
    # return result


    
# This is the name of the function 

def sum_divisors(n):

    # Initialize i, sum as a global variable, and result. 
    
    i = n
    global sum
    sum = 0
    result = 0
    
    # if n is zero, we will return zero. Else, we will open a while loop that will check if n divide i is zero, then the loop should break.
    # if n is not zero, then sum will be sum plus i, then we decrement i by 1. The result will be the sum minus n
    # let's use a case statement of n = 10. 10 is not equal to zero, and 10 / 10 is not zero, hence, sum will be 0 + i = 10. and i will be i - 1 = 9
    # result which was initalized to zero will be 10 - 10 = 0 
    # using n = 10, after first else statement , n = 10, sum = 10, i = 9. Since i is not zero, as long as n == i is not zero, decrement i by 1. Thus, i will reduce by 1 till i is zero
    # when i is zero, result will be 10 - 10 = 0. The while loop continues
    
    if n == 0:
        result = 0
    else:
        while n % i == 0:
            if i == 0:
                break
            else:
                sum = sum + i
                i = i - 1
                # print(sum - n, i + 1)
                result = sum - n
            if i == 0:
                break
            else:
                while n % i != 0:
                    i = i - 1
            result = sum - n
    return result
    
            
            
print(sum_divisors(0))
# 0
print(sum_divisors(3)) # Should sum of 1
# 1
print(sum_divisors(36)) # Should sum of 1+2+3+4+6+9+12+18
# 55
print(sum_divisors(102)) # Should be sum of 2+3+6+17+34+51
# 114

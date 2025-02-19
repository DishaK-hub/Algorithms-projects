from time import time
def factors(num):

    is_prime = True
    # this flag checks if the number is prime
    factor_list = []
    i = 2

    # this loop finds the factors
    while i * i <= num:
        if num % i == 0:
            factor_list.append(i)
            num = num // i
            is_prime = False
        else:
            i = i + 1  #O(n)

    if num != 1 and is_prime == False:
        factor_list.append(num)
    return factor_list





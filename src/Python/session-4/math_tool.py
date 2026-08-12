def factorial(num : int) -> int:
    '''' calculate n! using recursion 
    Args:
        num (int): user input the int number
    Returns:
       num! (int): factorial of the number
    Example:
        factorial(5) returns 120
    '''

    if num == 0:
        return 1
    else:
        return num * factorial(num - 1)


def is_prime(num : int) -> bool:
    '''' check if the number is prime or not
    Args:
        num (int): user input the int number to check
    Returns: 
         bool: True if the number is prime, False otherwise
    Example:
        is_prime(17) returns True
        '''
    if num < 2:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

'''
Another solution 

if num < 2:
        return False
for i in range(2, int(num ** 0.5) + 1):
    if num % i == 0:
        return False
 return True
'''

def is_armstrong(number):
    """
    Checks if number is an armstrong number, which is is a number that is the
    sum of its own digits each raised to the power of the number of digits.
    
    Input: integer
    Output: True or False
    """
    return sum([int(i)**len(str(number)) for i in str(number)]) == number

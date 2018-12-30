def classify(number):
    """Based on the aliquot sum, this function determines if the number is
    perfect, abundant or deficient. 
    Aliquot sum: sum of the factors of a number, not including the number
    itself.
    
    Input: positive integer
    Returns: string that indicates result:
        perfect: aliquot sum == number
        abundant: aliquot sum > number
        deficient: aliquot sum < number
    """
    
    if type(number) != int or number < 1:
        raise ValueError("Provide a positive integer as input")
    
    factors = []
    for i in range(1, number):
        if number % i == 0:
            factors.append(i)
    
    if sum(factors) > number:
        return "abundant"
    elif sum(factors) < number:
        return "deficient"
    else:
        return "perfect"
    

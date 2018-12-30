def prime_factors(natural_number):
    """Prime factorisation of an integer
    """
    
    prime_factors = []
    i = 2
    while natural_number > 1:
        if natural_number % i == 0:             # check if i is a factor
            if is_prime_number(i):              # if i is a factor, check if i is a prime
                prime_factors.append(i)
                natural_number = natural_number / i
        else:
            i += 1
    return prime_factors
            
            
def is_prime_number(x):
    if x >= 2:
        for y in range(2,x):
            if not ( x % y ):
                return False
    else:
        return False
    return True
    	
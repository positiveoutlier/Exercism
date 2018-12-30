def sum_of_multiples(limit, multiples):
    """
    Given a number, find the sum of all the unique multiples of particular 
    numbers up to but not including that number.
    
    Input:
        limit: determines the upper value of the unique multiples
        multiples: the numbers that are used to determine the unique multiples
    
    Returns:
        sum of all the unique multiples up until but not including the limit
    """
    
    unique_multiples = set()
    
    for integer in multiples:
        unique_multiples.update(range(integer, limit, integer))
    
    return sum(unique_multiples)
 

#'set.update' expects an iterable as an argument. 'range' is an iterable, which
#is why the code below can be replaced by the code above.
#This way, 'unique_multiples.update' does not need to update one i at the time.    
# =============================================================================
#     for integer in multiples:
#         for i in range(integer, limit, integer):
#             unique_multiples.update([i])
#     
# =============================================================================

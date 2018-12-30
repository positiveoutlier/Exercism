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
        for i in range(integer, limit, integer):
            if i < limit:
                unique_multiples.update([i])
    
    return sum(unique_multiples)
# =============================================================================
#     unique_multiples = []
#      
#     for i in range(1, limit):
#          for integer in multiples:
#              if i * integer not in unique_multiples and i * integer < limit:
#                  unique_multiples.append(i * integer)
#      
#     return sum(unique_multiples)
# =============================================================================
 

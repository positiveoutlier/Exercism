def largest_product(series, size):
    """For a string of digits, this function will calculate the largest product 
    for a contiguous substring of digits of length 'size'.
    
    Input:
        series: a string that should only contain digits. If string is empty,
                then 1 will be returned if size is equal to zero. Otherwise,
                a ValueError is raised.
        size: an integer greater than or equal to 0
        
    Output:
        the largest product for contiguous substring of digits of length 'size'
        
    Example:
        for the input '1027839564', the largest product for a series of 3 
        digits is 270 (9 * 5 * 6), and the largest product for a series of 
        5 digits is 7560 (7 * 8 * 3 * 9 * 5).
    """
    
    # Testing the 'series' input:
    if type(series) != str:
        raise ValueError("series input has to be of type string")
    if not series:
        if size == 0:
            return 1
        else:
            raise ValueError("the series input cannot be empty")
    if not series.isdigit():
        raise ValueError("all characters in the series string should be digits")
    
    # Testing the 'size' input:
    if type(size) != int:
        raise ValueError("size input has to be of type integer")
    if size > len(series):
        raise ValueError("size input cannot be greater than the length of the series")
    if size < 0:
        raise ValueError("size input has to be greater than or equal to zero")
    
    largest_product = []
    for i in range(len(series) - (size - 1)):
        product = 1
        for digit in series[i : (size + i)]:
            product *= int(digit)
        largest_product.append(product)
    return max(largest_product)
def distance(strand_a, strand_b):
    """
    This function checks the hamming distance between two DNA strands,
    by counting the number of differences between two homologous DNA strands.
    
    Input: 
        strand_a, strand_b = string that depicts the DNA strands
        
    Returns:
        The hamming_distance (integer), or a ValueError if
        strand_a and strand_b do not have equal length.
    """
    if len(strand_a) != len(strand_b):
        raise ValueError("The two DNA strands do not have the same length." +
                        "Please provide two DNA strands with equal length.")
    hamming_distance = 0
    for i in range(len(strand_a)):
        if strand_a[i] != strand_b[i]:
            hamming_distance += 1
    return hamming_distance
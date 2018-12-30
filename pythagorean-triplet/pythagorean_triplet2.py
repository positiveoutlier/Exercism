def triplets_with_sum(sum_of_triplet):
    """Finds the Pythagorean triplet(s) based on the sum of the
    three natural numbers, such that a**2 + b**2 == c**2,
    and a + b + c == sum_of_triplet
    """
    triplets = []
    for a in range(1, int(sum_of_triplet/3)):
        for b in range(a, int(sum_of_triplet/2)):
            c = sum_of_triplet - a - b
            if a < b < c:
                if is_triplet((a, b, c)):
                    triplets.append((a, b, c))
    return print(triplets)

def triplets_in_range(range_start, range_end):
    """Finds all triplets in a range
    """
    triplets = set([])
    for a in range(range_start, range_end):
        for b in range(a, range_end):
            for c in range(b, range_end):
                if is_triplet((a, b, c)):
                    triplets.append((a, b, c))
    return triplets
    
def is_triplet(triplet):
    """Determines if input is a triplet.
    
    Input expected: list with three integers (>= 0)
    Returns: True or False
    """
    a, b, c = sorted(triplet)
    return a**2 + b**2 == c**2
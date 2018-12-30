def triplets_with_sum(sum_of_triplet):
    """Finds the Pythagorean triplet(s) based on the sum of the
    three natural numbers, such that a**2 + b**2 == c**2,
    and a + b + c == sum_of_triplet
    """
    triplets = []
    for a in range(1, int(sum_of_triplet/3)):
        for b in range(a + 1, int(sum_of_triplet/2)):
            c = sum_of_triplet - a - b
            if b < c:
                if a*a + b*b == c*c:
                    triplets.append((a, b, c))
            else:
                break
    return set(triplets)

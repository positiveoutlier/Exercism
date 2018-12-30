def is_triangle(sides):
    """Tests, if given 3 sides, they make up a triangle.
    
    For a shape to be a triangle at all, all sides have to be of length > 0, 
    and the sum of the lengths of any two sides must be greater than or equal 
    to the length of the third side.
    
    Input: list with 3 integers
    Returns: True or False
    """
    if all(v == 0 for v in sides) or sorted(sides)[0] + sorted(sides)[1] < sorted(sides)[2]:
        return False
    else:
        return True 

def is_equilateral(sides):
    """Tests if all three sides of a triangle have the same length.
    
    Input: list with 3 integers
    Returns: True or False
    """
    if is_triangle(sides):
        return sides[0] == sides[1] == sides[2]
    else:
        return False

def is_isosceles(sides):
    """Tests if at least two sides of a triangle have the same length.
    
    Input: list with 3 integers
    Returns: True or False
    """
    if is_triangle(sides):
        return sides[0] == sides[1] or sides[0] == sides[2] or sides[1] == sides[2]
    else:
        return False

def is_scalene(sides):
    """Tests if all sides of a triangle have different lengths.
    
    Input: list with 3 integers
    Returns: True or False
    """
    if is_triangle(sides):
        return sides[0] != sides[1] and sides[0] != sides[2] and sides[1] != sides[2]
    else:
        return False


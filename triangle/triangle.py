def is_triangle(func):
    """Tests, if given 3 sides, they make up a triangle.
    
    For a shape to be a triangle at all, all sides have to be of length > 0, 
    and the sum of the lengths of any two sides must be greater than or equal 
    to the length of the third side.
    
    Input: list with 3 integers
    Returns: True or False
    """
    def wrapper(arg):
        if all(v == 0 for v in arg) or sorted(arg)[0] + sorted(arg)[1] < sorted(arg)[2]:
            return False
        else:
            return func(arg)
    return wrapper

@is_triangle
def is_equilateral(sides):
    """Tests if all three sides of a triangle have the same length.
    
    Input: list with 3 integers
    Returns: True or False
    """
    return sides[0] == sides[1] == sides[2]
    

@is_triangle
def is_isosceles(sides):
    """Tests if at least two sides of a triangle have the same length.
    
    Input: list with 3 integers
    Returns: True or False
    """
    return sides[0] == sides[1] or sides[0] == sides[2] or sides[1] == sides[2]

@is_triangle    
def is_scalene(sides):
    """Tests if all sides of a triangle have different lengths.
    
    Input: list with 3 integers
    Returns: True or False
    """
    return sides[0] != sides[1] and sides[0] != sides[2] and sides[1] != sides[2]


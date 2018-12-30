def is_leap_year(year):
    """
    Function takes as input a year (positive integer),
    and uses the following rules to determine if it is
    a leap year:
    on every year that is evenly divisible by 4
        except every year that is evenly divisible by 100
            unless the year is also evenly divisible by 400
    """
    if type(year) != int:
        raise Exception("Use a positive integer as input for year")
        return
    if year % 400 == 0:
        return True
    elif year % 4 == 0 and year % 100 != 0:
        return True  
    else:
        return False          
        
    

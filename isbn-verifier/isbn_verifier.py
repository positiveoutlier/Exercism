import re


def verify(isbn):
    """Checks if a string is a valid ISBN.
    The ISBN-10 format is 9 digits (0 to 9) plus one check character
    (either a digit or an X only).

    Input: string
    Output: True or False
    """
    isbn = isbn.replace("-", "")
    r = re.compile(r'\d{9}[0-9X]')
    isbn_check = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
    if r.match(isbn) and len(isbn) == 10:
        isbn_reformatted = []
        for i in range(len(isbn) - 1):
            isbn_reformatted.append(int(isbn[i]))
        if isbn[9] == 'X':
            isbn_reformatted.append(10)
        else:
            isbn_reformatted.append(int(isbn[9]))
        return sum([a*b for a, b in zip(isbn_reformatted,
                                        isbn_check)]) % 11 == 0
    return False

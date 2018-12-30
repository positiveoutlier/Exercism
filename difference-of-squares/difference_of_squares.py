def square_of_sum(count):
    total = 0
    for i in range(count + 1):
        total = total + i
    return total * total


def sum_of_squares(count):
    total = 0
    for i in range(count + 1):
        total = total + (i * i)
    return total

def difference(count):
    return square_of_sum(count) - sum_of_squares(count)

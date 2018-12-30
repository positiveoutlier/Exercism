def on_square(integer_number):
    if integer_number < 1 or integer_number > 64:
        raise ValueError("Only use positive integers between 1 and 64")
    return 2 ** (integer_number - 1)


def total_after(integer_number):
    if integer_number < 1 or integer_number > 64:
        raise ValueError("Only use positive integers between 1 and 64")
    return 2 ** integer_number - 1

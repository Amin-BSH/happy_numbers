def is_happy(n: int) -> bool:
    """A happy number is a number which eventually reaches 1 when replaced by the sum of the square of each digit.

    :param n: The number to check
    :return: return True if the number is a happy number, False otherwise

    :Example:
    >>> is_happy(19)
    >>> True

    >>> is_happy(45)
    >>> False

    """
    seen_numbers = set()
    while n != 1 and n not in seen_numbers:
        seen_numbers.add(n)
        n = sum([int(i) ** 2 for i in str(n)])
    return n == 1

if "__main__" == __name__:
    assert is_happy(19) is True
    assert is_happy(7) is True
    assert is_happy(45) is False
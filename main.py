"""Task 1
from typing import Optional
def to_power(x: Optional[int, float], exp: int) -> Optional[int, float]:
    Returns  x ^ exp
    >>> to_power(2, 3) == 8
    True
    >>> to_power(3.5, 2) == 12.25
    True
    >>> to_power(2, -1)
    ValueError: This function works only with exp > 0.
    pass"""
from typing import Union


def to_power(x: Union[int, float], exp: int) -> Union[int, float]:
    if exp == 0:
        return 1
    elif exp < 0:
        raise ValueError("This function works only with exp > 0.")
    else:
        return x * to_power(x, exp - 1)


'''Task 2

from typing import Optional
def is_palindrome(looking_str: str, index: int = 0) -> bool:
    """
    Checks if input string is Palindrome
    >>> is_palindrome('mom')
    True

    >>> is_palindrome('sassas')
    True

    >>> is_palindrome('o')
    True
    """
    pass'''


def is_palindrome(looking_str: str, index: int = 0) -> bool:
    if len(looking_str) > 0 and index != len(looking_str):
        if looking_str[len(looking_str) - 1] == looking_str[index]:
            return is_palindrome(looking_str[:len(looking_str) - 1], index + 1)
'''Task 3
from typing import Optional
def mult(a: int, n: int) -> int:
    """
    This function works only with positive integers

    >>> mult(2, 4) == 8
    True

    >>> mult(2, 0) == 0
    True

    >>> mult(2, -4)
    ValueError("This function works only with postive integers")
    """
'''


def mult(a: int, n: int) -> int:
    if n == 0:
        return 0
    elif n == 1:
        return a
    elif n < 0:
        raise ValueError('This function works only with postive integers')
    else:
        return a + mult(a, n - 1)


'''Task 4
def reverse(input_str: str) -> str:
    """
    Function returns reversed input string
    >>> reverse("hello") == "olleh"
    True
    >>> reverse("o") == "o"
    True
    """'''


def reverse(input_str: str) -> str:
    if len(input_str) > 0:
        return f"{input_str[len(input_str) - 1]}{reverse(input_str[:len(input_str) - 1])}"
    else:
        return ''


'''Task 5
def sum_of_digits(digit_string: str) -> int:
    """
    >>> sum_of_digits('26') == 8
    True

    >>> sum_of_digits('test')
    ValueError("input string must be digit string")
    """'''

def sum_of_digits(digit_string: str) -> int:
    if type(digit_string) is int or digit_string.isdigit():
        ds = int(digit_string)
        if ds == 0:
            return 0
        return ds % 10 + sum_of_digits(ds // 10)
    else:
        raise ValueError("input string must be digit string")


if __name__ == '__main__':
    print(to_power(2, 3))
    print(to_power(3.5, 2))
    # print(to_power(2, -1))
    print(mult(2, 4))
    print(mult(2, 0))
    #print(is_palindrome('mom'))
    print(reverse("hello"))
    print(reverse("o"))
    print(sum_of_digits("22"))

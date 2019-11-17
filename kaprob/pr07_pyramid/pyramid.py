"""Program that creates beautiful pyramids."""


def make_pyramid(base: int, char: str) -> list:
    """
    Construct a pyramid with given base.

    Pyramid should consist of given chars, all empty spaces in the pyramid list are ' '. Pyramid height depends on
    base length. Lowest floor consists of base-number chars. Every floor has 2 chars less than the floor lower to it.
    make_pyramid(3, "A") -> [ [' ', 'A', ' '], ['A', 'A', 'A'] ] make_pyramid(6, 'a') -> [ [' ', ' ', 'a', 'a', ' ',
    ' '], [' ', 'a', 'a', 'a', 'a', ' '], ['a', 'a', 'a', 'a', 'a', 'a'] ] :param base: int :param char: str :return:
    list
    """
    height = 0
    if base % 2 == 0:
        height = base // 2
    else:
        height = (base // 2) + 1
    pyramid = [
        [(char if j == 0 else ' ' if j > i < base - j else ' ' if i > base - 1 - j else char) for i in range(base)] for
        j in range(height)]
    pyramid.reverse()
    return pyramid
    pass


def join_pyramids(pyramid_a: list, pyramid_b: list) -> list:
    """
    Join together two pyramid lists.

    Get 2 pyramid lists as inputs. Join them together horizontally. If the the pyramid heights are not equal,
    add empty lines on the top until they are equal. join_pyramids(make_pyramid(3, "A"), make_pyramid(6, 'a')) -> [ [
    ' ', ' ', ' ', ' ', ' ', 'a', 'a', ' ', ' '], [' ', 'A', ' ', ' ', 'a', 'a', 'a', 'a', ' '], ['A', 'A', 'A', 'a',
    'a', 'a', 'a', 'a', 'a'] ]

    :param pyramid_a: list
    :param pyramid_b: list
    :return: list
    """
    height_a = len(pyramid_a)
    height_b = len(pyramid_b)
    if height_a < height_b:
        empty_lines = [[' ' for i in range(len(pyramid_a[0]))] for j in range(height_b - height_a)]
        pyramid_a = empty_lines + pyramid_a
    elif height_b < height_a:
        empty_lines = [[' ' for i in range(len(pyramid_b[0]))] for j in range(height_a - height_b)]
        pyramid_b = empty_lines + pyramid_b
    pyramid_joined = [pyramid_a[i] + pyramid_b[i] for i in range(len(pyramid_a))]
    return pyramid_joined

    pass


def to_string(pyramid: list) -> str:
    """
    Return pyramid list as a single string.

    Join pyramid list together into a string and return it.
    to_string(make_pyramid(3, 'A')) ->
    '''
     A
    AAA
    '''

    :param pyramid: list
    :return: str
    """
    pyramid = [[''.join(pyramid[i]) + '\n' if i < len(pyramid) - 1 else ''.join(pyramid[i])] for i in
               range(len(pyramid))]
    return ''.join([j for i in pyramid for j in i])

    pass

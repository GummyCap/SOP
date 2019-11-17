"""Primes identifier."""


def is_prime_number(number: int) -> bool:
    """
    Check if number (given in function parameter) is prime.

    If number is prime -> return True
    If number is not prime -> return False

    :param number: number for check.
    :return: boolean True if number is prime or False if number is not prime.
    """
    if number > 1:  # Is it larger than 1?
        for i in range(2, number):
            if (number % i) == 0:  # Does it divide cleanly with anything smaller than itself starting from 2
                return False
        else:
            return True
    else:
        return False


if __name__ == '__main__':
    print(is_prime_number(2))  # -> True
    print(is_prime_number(89))  # -> True
    print(is_prime_number(23))  # -> True
    print(is_prime_number(4))  # -> False
    print(is_prime_number(7))  # -> True
    print(is_prime_number(88))  # -> False

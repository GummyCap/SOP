# -*- coding: utf-8 -*-
"""Check if given ID code is valid."""


def get_gender(gender_number: int) -> str:
    """
    Find out if the gender number provided is a male or female return the correct gender.
    :param gender_number: int
    :return: str
    """

    if (gender_number % 2) == 0:
        return "female"
    else:
        return "male"


def is_leap_year(year: int) -> bool:
    """
    See if the year provided is a leap year, if it is return True.
    :param year: int
    :return: boolean
    """

    if (year % 400) == 0:
        return True
    elif (year % 100) == 0:
        return False
    elif (year % 4) == 0:
        return True
    else:
        return False


def is_valid_gender_number(number: int) -> bool:
    """
    Check if the gender number provided is an acceptable value for gender.
    :param number: int
    :return: boolean
    """

    if number < 1 or number > 6:
        return False
    else:
        return True


def is_valid_year_number(year_number: int) -> bool:
    """
    Check if given value is correct for year number in ID code.

    :param year_number: int
    :return: boolean
    """

    if year_number >= 0 and year_number < 100:
        return True
    else:
        return False
    pass


def is_valid_month_number(month_number: int) -> bool:
    """
    Check if given value is correct for month number in ID code.

    :param month_number: int
    :return: boolean
    """

    if month_number > 0 and month_number < 13:
        return True
    else:
        return False
    pass


def is_valid_day_number(gender_number: int, year_number: int, month_number: int, day_number: int) -> bool:
    """
    Check if given value is correct for day number in ID code.
    Also, consider leap year and which month has 30 or 31 days.

    :param gender_number: int
    :param year_number: int
    :param month_number: int
    :param day_number: int
    :return: boolean
    """

    days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    if month_number == 2 and is_leap_year(get_full_year(gender_number, year_number)):
        if day_number <= 29:
            return True
        else:
            return False
    else:
        if day_number <= days_in_month[month_number - 1]:
            return True
        else:
            return False


def is_valid_birth_number(birth_number: int):
    """
    Check if given value is correct for birth number in ID code.

    :param birth_number: int
    :return: boolean
    """

    if birth_number > 0 and birth_number < 1000:
        return True
    else:
        return False
    pass


def is_valid_control_number(id_code: str) -> bool:
    """
    Check if given value is correct for control number in ID code.
    Use algorithm made for creating this number.

    :param id_code: string
    :return: boolean
    """

    control_number = int(id_code[10])
    mod_1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 1]
    mod_2 = [3, 4, 5, 6, 7, 8, 9, 1, 2, 3]
    mod_control = 0
    for i in range(10):
        mod_control += (int(id_code[i]) * mod_1[i])
    check_number = mod_control % 11
    if (check_number is not 10) and check_number == control_number:
        return True
    elif (check_number is not 10) and check_number is not control_number:
        return False
    else:
        mod_control = 0
        for i in range(10):
            mod_control += (int(id_code[i]) * mod_2[i])
        check_number = mod_control % 11
        if control_number == check_number:
            return True
        else:
            return False


def get_full_year(gender_number: int, year_number: int) -> int:
    """
    Define the 4-digit year when given person was born.
    Person gender and year numbers from ID code must help.
    Given year has only two last digits.

    :param gender_number: int
    :param year_number: int
    :return: int
    """

    if gender_number == 1 or gender_number == 2:
        century = 1800
    elif gender_number == 3 or gender_number == 4:
        century = 1900
    else:
        century = 2000

    return century + year_number

    pass


def get_birth_place(birth_number: int) -> str:
    """
    Find the place where the person was born.

    Possible locations are following: Kuressaare, Tartu, Tallinn, Kohtla-Järve, Narva, Pärnu,
    Paide, Rakvere, Valga, Viljandi, Võru and undefined. Lastly if the number is incorrect the function must return
    the following 'Wrong input!'
    :param birth_number: int
    :return: str
    """

    if birth_number >= 1 and birth_number <= 10:
        return "Kuressaare"
    if (birth_number >= 11 and birth_number <= 20) or (birth_number >= 271 and birth_number <= 370):
        return "Tartu"
    if birth_number >= 21 and birth_number <= 220 or (birth_number >= 471 and birth_number <= 490):
        return "Tallinn"
    if birth_number >= 221 and birth_number <= 270:
        return "Kohtla-Järve"
    if birth_number >= 421 and birth_number <= 470:
        return "Pärnu"
    if birth_number >= 491 and birth_number <= 520:
        return "Paide"
    if birth_number >= 521 and birth_number <= 570:
        return "Rakvere"
    if birth_number >= 571 and birth_number <= 600:
        return "Valga"
    if birth_number >= 601 and birth_number <= 650:
        return "Viljandi"
    if birth_number >= 651 and birth_number <= 710:
        return "Võru"
    if birth_number >= 710 and birth_number <= 999:
        return "undefined"
    else:
        return "Wrong input!"
    pass


def get_data_from_id(id_code: str) -> str:
    """
    Get possible information about the person.

    Use given ID code and return a short message.
    Follow the template - This is a <gender> born on <DD.MM.YYYY> in <location>.
    :param id_code: str
    :return: str
    """

    if not is_id_valid(id_code):
        return "Given invalid ID code!"
    month_number = id_code[3] + id_code[4]  # Number of month
    day_number = id_code[5] + id_code[6]  # Day in Month
    birth_number = int(id_code[7] + id_code[8] + id_code[9])  # Birth  Number/ Location
    gender = get_gender(int(id_code[0]))  # Gender of Person
    year = str(get_full_year(int(id_code[0]), int(id_code[1] + id_code[2])))  # In what year they were born
    location = get_birth_place(birth_number)  # Where they were born
    return "This is a " + gender + " born on " + day_number + "." + month_number + "." + year + " in " + location
    pass


def is_id_valid(id_code: str) -> bool:
    """
    Check if given ID code is valid and return the result (True or False).

    Complete other functions before starting to code this one.
    You should use the functions you wrote before in this function.
    :param id_code: str
    :return: boolean
    """

    if len(id_code) is not 11:
        return False
    gender_number = int(id_code[0])
    year_number = int(id_code[1] + id_code[2])
    month_number = int(id_code[3] + id_code[4])
    day_number = int(id_code[5] + id_code[6])
    birth_number = int(id_code[7] + id_code[8] + id_code[9])

    if not is_valid_control_number(id_code):
        return False
    if not is_valid_gender_number(gender_number):
        return False
    if not is_valid_birth_number(birth_number):
        return False
    if not is_valid_year_number(year_number):
        return False
    if not is_valid_month_number(month_number):
        return False
    if not is_valid_day_number(gender_number, year_number, month_number, day_number):
        return False
    else:
        return True
    pass


if __name__ == '__main__':
    print("\nGender number:")
    for i in range(9):
        print(f"{i} {is_valid_gender_number(i)}")
        # 0 -> False
        # 1...6 -> True
        # 7...8 -> False
    print("\nYear number:")
    print(is_valid_year_number(100))  # -> False
    print(is_valid_year_number(50))  # -> true
    print("\nMonth number:")
    print(is_valid_month_number(2))  # -> True
    print(is_valid_month_number(15))  # -> False
    print("\nDay number:")
    print(is_valid_day_number(4, 5, 12, 25))  # -> True
    print(is_valid_day_number(3, 10, 8, 32))  # -> False
    print(is_leap_year(1804))  # -> True
    print(is_leap_year(1800))  # -> False
    print("\nFebruary check:")
    print(
        is_valid_day_number(4, 96, 2, 30))  # -> False (February cannot contain more than 29 days in any circumstances)
    print(is_valid_day_number(4, 99, 2, 29))  # -> False (February contains 29 days only during leap year)
    print(is_valid_day_number(4, 8, 2, 29))  # -> True
    print("\nMonth contains 30 or 31 days check:")
    print(is_valid_day_number(4, 22, 4, 31))  # -> False (April contains max 30 days)
    print(is_valid_day_number(4, 18, 10, 31))  # -> True
    print(is_valid_day_number(4, 15, 9, 31))  # -> False (September contains max 30 days)
    print("\nBorn order number:")
    print(is_valid_birth_number(0))  # -> False
    print(is_valid_birth_number(1))  # -> True
    print(is_valid_birth_number(850))  # -> True
    print("\nControl number:")
    print(is_valid_control_number("49808270244"))  # -> True
    print(is_valid_control_number("60109200187"))  # -> False, it must be 6

    print("\nFull message:")
    print(get_data_from_id("49808270244"))  # -> "This is a female born on 27.08.1998 in Tallinn."
    print(get_data_from_id("60109200187"))  # -> "Given invalid ID code!"
    print(get_full_year(1, 28))  # -> 1828
    print(get_full_year(4, 85))  # -> 1985
    print(get_full_year(5, 1))  # -> 2001
    print(get_gender(2))  # -> "female"
    print(get_gender(5))  # -> "male"

    # Comment these back in if you have completed other functions.
    print("\nChecking where the person was born")

    print(get_birth_place(0))  # -> "Wrong input!"
    print(get_birth_place(1))  # -> "Kuressaare"
    print(get_birth_place(273))  # -> "Tartu"
    print(get_birth_place(220))  # -> "Tallinn"

    print("\nOverall ID check::")
    print(is_id_valid("49808270244"))  # -> True
    print(is_id_valid("12345678901"))  # -> False
    print("\nTest now your own ID code:")
    personal_id = input()  # type your own id in command prompt
    print(is_id_valid(personal_id))  # -> True
    print(get_data_from_id(personal_id))

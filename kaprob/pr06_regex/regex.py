"""Text parser."""
import re


def read_file(path: str) -> list:
    """
    Read file and return list of lines read.

    :param path: str
    :return: list
    """
    path = open(path, 'r')
    output = path.readlines()
    path.close()
    for i in range(len(output)):
        output[i] = output[i].replace('\n', '')
    return output

    pass


def match_specific_string(input_data: list, keyword: str) -> int:
    """
    Check if given list of strings contains keyword.

    Return all keyword occurrences (case insensitive). If an element contains the keyword several times,
    count all the occurrences.

    ["Python", "python", "PYTHON", "java"], "python" -> 3

    :param input_data: list
    :param keyword: str
    :return: int
    """
    match_count = 0
    for line in input_data:
        words = re.findall(keyword, line, re.IGNORECASE)
        match_count += len(words)
    return match_count
    pass


def detect_email_addresses(input_data: list) -> list:
    """
    Check if given list of strings contains valid email addresses.

    Return all unique valid email addresses in alphabetical order presented in the list.
    ["Test", "Add me test@test.ee", "ago.luberg@taltech.ee", "What?", "aaaaaa@.com", ";_:Ö<//test@test.au??>>>;;d,"] ->
    ["ago.luberg@taltech.ee", "test@test.au", "test@test.ee"]

    :param input_data: list
    :return: list
    """
    address_list = []
    for line in input_data:
        address = re.findall(r'[a-zA-Z0-9+\-_.]+@(?:[a-zA-Z0-9-]+\.)+[a-zA-Z]{2,}', line)
        if len(address) > 0:
            for ele in address:
                address_list.append(ele)
    address_list = list(dict.fromkeys(address_list))
    address_list.sort()
    return address_list
    pass


if __name__ == '__main__':
    list_of_lines_emails = read_file("input_detect_email_addresses_example_2.txt")  # reading from file
    print(detect_email_addresses(
        list_of_lines_emails))  # ['allowed@example.com', 'firstname-lastname@example.com', 'right@example.com',
    # 'spoon@lol.co.jp', 'testtest@dome.museum', 'testtest@example.name']

    list_of_lines_keywords = read_file("input_match_specific_string_example_1.txt")

    print(match_specific_string(list_of_lines_keywords, "job"))  # 9

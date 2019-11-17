"""Filtering."""


def remove_vowels(string: str) -> str:
    """
    Remove vowels (a, e, i, o, u).

    :param string: Input string
    :return string without vowels.
    """
    for i in "aieouAIEOU":
        string = string.replace(i, "")
    return string

    pass


def longest_filtered_word(string_list: list) -> str:
    """
    Filter, find and return the longest string.

    Return None if list is empty.

    :param string_list: List of strings.
    :return: Longest string without vowels.
    """
    if len(string_list) == 0:
        return None
    longest_word = ""

    for i in range(len(string_list)):
        string_list[i] = remove_vowels(string_list[i])
        if len(string_list[i]) > len(longest_word):
            longest_word = string_list[i]
    return longest_word
    pass


def sort_list(string_list: list) -> list:
    """
    Filter vowels in strings and sort the list by the length.

    Longer strings come first.

    :param string_list: List of strings that need to be sorted.
    :return: Filtered list of strings sorted by the number of symbols in descending order.
    """
    for i in range(len(string_list)):
        string_list[i] = remove_vowels(string_list[i])
    string_list.sort(key=len)
    string_list.reverse()
    return string_list

    pass


if __name__ == '__main__':
    print(remove_vowels(""))  # => ""
    print(remove_vowels("hello"))  # => "hll"
    print(remove_vowels("Home"))  # => "Hm"
    print(longest_filtered_word(["Bunny", "Tiger", "Bear", "Snake"]))  # => "Bnny"
    print(sort_list(["Bunnysdadasdasda", "Tigersadas", "Byyyyyyear", "Snake"]))  # => ['Bnny', 'Tgr', 'Snk', 'Br']

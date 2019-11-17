"""Converter."""


def dec_to_binary(dec: int) -> str:
    """
    Convert decimal number into binary.

    :param dec: decimal number to convert
    :return: number in binary
    """
    output_list = []  # Initialize list for binary
    if dec == 0:
        return "0"
    while dec >= 1:  # Loop adds to binary
        output_list.append(dec % 2)
        dec = dec // 2
    output_list.reverse()  # List the number in correct order
    output_str = ""  # Init the final output
    for ele in output_list:  # Add elements to list
        output_str += str(ele)

    return output_str


def binary_to_dec(binary: str) -> int:
    """
    Convert binary number into decimal.

    :param binary: binary number to convert
    :return: number in decimal
    """
    lng = len(binary)  # Get number of chars
    pos = (lng - 1)  # initial position
    output = 0  # Output
    for i in range(0, lng):
        output += (int(binary[i]) * (2 ** pos))
        pos -= 1
    return output


if __name__ == "__main__":
    print(dec_to_binary(145))  # -> 10010001
    print(dec_to_binary(245))  # -> 11110101
    print(dec_to_binary(255))  # -> 11111111
    print(dec_to_binary(0))  # -> 1111111

    print(binary_to_dec("1111"))  # -> 15
    print(binary_to_dec("10101"))  # -> 21
    print(binary_to_dec("10010"))  # -> 18

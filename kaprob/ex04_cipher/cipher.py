"""Encode and decode text using Rail-fence Cipher."""


def create_table(rows: int, cols: int, zig: bool = False) -> []:
    """
    Create an empty table.

    Get number of rows and columns needed, optional zig-zag to table.

    :param rows: Number of rows.
    :param cols: Number of Columns.
    :param zig: Zig-Zag the table.
    :return: Created table.
    """
    table = [["" for i in range(cols)] for j in range(rows)]
    if zig:
        # Draw Zig-Zag in table
        row, col = 0, 0  # Position in table
        falling = None
        for i in range(cols):
            if row == 0:
                falling = True
            if row == rows - 1:
                falling = False
            table[row][col] = "*"
            col += 1
            if falling:
                row += 1
            else:
                row -= 1
    return table


def encode(message: str, key: int) -> str:
    """
    Encode text using Rail-fence Cipher.

    Replace all spaces with '_'.

    :param message: Text to be encoded.
    :param key: Encryption key.
    :return: Decoded string.
    """
    message = message.replace(" ", "_")
    if key == 1:
        return message
    rail = [""] * key  # Create str based on key number
    layer = 0  # Layer of rail
    falling = True
    for ele in message:
        rail[layer] += ele

        if layer == (key - 1):
            falling = False
            layer -= 1
        elif layer < key and falling:
            layer += 1
        elif not falling:
            layer -= 1

        if layer == 0:
            falling = True

    output = "".join(rail)
    return output

    pass


def decode(message: str, key: int) -> str:
    """
    Decode text knowing it was encoded using Rail-fence Cipher.

    '_' have to be replaced with spaces.

    :param message: Text to be decoded.
    :param key: Decryption key.
    :return: Decoded string.
    """
    message = message.replace("_", " ")
    if key == 1:
        return message
    table = create_table(key, len(message), True)

    # Transfer chars to the Zig-Zag
    pos = 0  # Position in message
    for i in range(key):
        for j in range(len(message)):
            if table[i][j] == "*" and pos < len(message):
                table[i][j] = message[pos]
                pos += 1

    # Merge lines together
    row, col = 0, 0  # Position in table
    for i in range(len(message)):
        if row == 0:
            falling = True
        if row == key - 1:
            falling = False
        table[0][col] = table[row][col]
        col += 1
        if falling:
            row += 1
        else:
            row -= 1
    return "".join(table[0])

    pass


if __name__ == '__main__':
    print(encode("Mind on vaja krüpteerida", 3))  # => M_v_prido_aaküteiannjred
    print(encode("Mind on", 3))  # => M_idonn
    print(encode("hello", 1))  # => hello
    print(encode("hello", 8))  # => hello
    print(encode("kaks pead", 1))  # => kaks_pead

    print(decode("kaks_pead", 1))  # => kaks pead
    print(decode("M_idonn", 3))  # => Mind on
    print(decode("M_v_prido_aaküteiannjred", 3))  # => Mind on vaja krüpteerida

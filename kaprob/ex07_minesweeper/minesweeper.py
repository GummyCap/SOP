"""Minesweeper has to swipe the mines."""
import copy


def create_minefield(height: int, width: int) -> list:
    """
    Create and return minefield.

    Minefield must be height high and width wide. Each position must contain single dot (`.`).
    :param height: int
    :param width: int
    :return: list
    """
    minefield = [['.' for i in range(width)] for j in range(height)]
    return minefield
    pass


def add_mines(minefield: list, mines: list) -> list:
    """
    Add mines to a minefield and return minefield.

    This function cannot modify the original minefield list.
    Minefield must be length long and width wide. Each non-mine position must contain single dot.
    If a position is empty ("."), then a small mine is added ("x").
    If a position contains small mine ("x"), a large mine is added ("X").
    Mines are in a list.
    Mine is a list. Each mine has 4 integer parameters in the format [N, S, E, W].
        - N is the distance between area of mines and top of the minefield.
        - S ... area of mines and bottom of the minefield.
        - E ... area of mines and right of the minefield.
        - W ... area of mines and left of the minefield.

    :param minefield: list
    :param mines: list
    :return: list
    """
    minefield_mines = copy.deepcopy(minefield)
    for mine in mines:
        minefield_mines = [['x' if (mine[3] <= w <= (len(minefield_mines[h]) - mine[2] - 1))
                            and (mine[0] <= h <= len(minefield_mines) - mine[1] - 1)
                            and minefield_mines[h][w] == '.'
                            else 'X' if (mine[3] <= w <= (len(minefield_mines[h]) - mine[2] - 1))
                            and (mine[0] <= h <= len(minefield_mines) - mine[1] - 1)
                            and minefield_mines[h][w] == 'x'
                            else minefield_mines[h][w] for w in range(len(minefield_mines[0]))]
                           for h in range(len(minefield_mines))]
    return minefield_mines
    pass


def get_minefield_string(minefield: list) -> str:
    """
    Return minefield's string representation.

    :param minefield: list
    :return: str
    """
    minefield = [[''.join(minefield[i]) + '\n' if i < len(minefield) else ''.join(minefield[i])]
                 for i in range(len(minefield))]
    return ''.join([j for i in minefield for j in i])
    pass


def calculate_mine_count(minefield: list) -> list:
    """
    For each cell in minefield, calculate how many mines are nearby.

    :param minefield: list
    :return: list
    """
    def border_mine(field: list, h: int, w: int) -> int:
        """
        Find out how many mines surround given position.

        :param w:
        :param h:
        :param field: list

        :return: int
        """
        total_mines = 0
        for height in range((h - 1), (h + 2)):
            for width in range((w - 1), (w + 2)):
                if 0 <= width < len(field[0]) and 0 <= height < len(field):
                    if field[height][width] == 'x' or field[height][width] == 'X':
                        total_mines += 1
        return total_mines

    mine_count = [[str(border_mine(minefield, h, w)) if minefield[h][w] == '.' else minefield[h][w] for w in
                   range(len(minefield[h]))] for h in
                  range(len(minefield))]
    return mine_count

    pass


def sweeper_finder(field: list) -> list:
    """
    Get position of sweeper and remove it from field.

    :param field: list
    :return: list
    """
    for line in range(len(field)):
        for column in range(len(field[line])):
            if field[line][column] == '#':
                field[line][column] = '.'
                return [line, column]
    pass


def walk(minefield: list, moves: str, lives: int) -> list:
    """
    Make moves on the minefield.

    This function cannot modify the original minefield list.
    Starting position is marked by #.
    There is always exactly one # on the field.
    The position you start is an empty cell (".").

    Moves is a list of move "orders":
    N - up,
    S - down,
    E - right,
    W - left.

    :param minefield:
    :param moves:
    :param lives:
    :return: list
    """
    minefield = copy.deepcopy(minefield)
    sweeper_pos = sweeper_finder(minefield)
    mine_map = calculate_mine_count(minefield)

    move_order = [char for char in moves]
    move_options = {'N': [-1, 0],
                    'S': [1, 0],
                    'W': [0, -1],
                    'E': [0, 1]}
    for move in move_order:
        new_pos = copy.deepcopy(sweeper_pos)
        new_pos[0] += move_options.get(move)[0]
        new_pos[1] += move_options.get(move)[1]
        if not (new_pos[0] < 0 or new_pos[0] > (len(minefield) - 1)
                or new_pos[1] < 0 or new_pos[1] > (len(minefield[0]) - 1)):
            if minefield[new_pos[0]][new_pos[1]] == 'x':
                if int(mine_map[sweeper_pos[0]][sweeper_pos[1]]) >= 5:
                    if lives == 0:
                        break
                    lives += -1
                minefield[new_pos[0]][new_pos[1]] = '.'
                mine_map = calculate_mine_count(minefield)
            elif minefield[new_pos[0]][new_pos[1]] == 'X':
                if lives == 0:
                    break
                else:
                    minefield[new_pos[0]][new_pos[1]] = '.'
                    mine_map = calculate_mine_count(minefield)
                    sweeper_pos = new_pos
                    lives += -1
            else:
                sweeper_pos = new_pos
    minefield[sweeper_pos[0]][sweeper_pos[1]] = '#'
    return minefield


if __name__ == '__main__':
    mf = create_minefield(3, 5)
    mf = add_mines(mf, [[0, 0, 1, 2]])
    mf = add_mines(mf, [[0, 1, 1, 1]])
    print(get_minefield_string(mf))
    mf[0][4] = "#"
    mf = walk(mf, "WSSWN", 2)
    print(get_minefield_string(mf))

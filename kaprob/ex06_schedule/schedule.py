"""Create schedule from the given file."""
import re


def create_schedule_file(input_filename: str, output_filename: str) -> None:
    """Create schedule file from the given input file."""
    file = open(input_filename, 'r')
    lines = file.readlines()
    file.close()
    string = ''.join(lines)
    schedule_string = create_schedule_string(string)
    output = open(output_filename, 'w+')
    output.write(schedule_string)
    output.close()

    pass


def create_schedule_string(input_string: str) -> str:
    """Create schedule string from the given input string.

    :param input_string: str
    :return: str
    """
    input_string = input_string.lower()
    time = re.findall(r'[\d{1,2}]+[^\d][\d]{1,2}[ ] *[a-z]+', input_string)
    task_list = []
    for ele in time:
        timestamp = re.findall(r'[\d{1,2}]+[^\d]\d{1,2}', ele)
        task = re.findall(r'[a-z]*(?=$)', ele)
        appendable = [timestamp[0], task[0]]
        task_list.append(appendable)

    for i in range(len(task_list)):
        task_list[i][0] = re.sub(r'[^\d]', ':', task_list[i][0])
    task_list = normalize(task_list)
    task_dict = {}
    for i in task_list:
        if i[0] not in task_dict:
            task_dict[i[0]] = [i[1]]
        else:
            task_dict.get(i[0]).append(i[1])
    for ele in task_dict:
        task_dict[ele] = list(dict.fromkeys(task_dict.get(ele)))

    new_dict = {}
    for key in task_dict:
        new_dict[key] = ', '.join(task_dict.get(key))

    return create_table(new_dict)

    pass


def create_table(task: dict) -> str:
    """Create table.

    :param task: dict
    :return: str
    """

    def sort_time(sortee: list) -> int:
        """Get total minutes.

        :param sortee:
        :return: int
        """
        splitter = sortee[0].find(':')
        hour = int((sortee[0])[:splitter])
        minute = int((sortee[0])[len(sortee[0]) - 2:])

        return (60 * hour) + minute

    if len(task) == 0:
        return "------------------\n|  time | items  |\n------------------\n| No items found |\n------------------"
    task_list = list(task.items())
    for i in range(len(task_list)):
        task_list[i] = list(task_list[i])

    task_list.sort(key=sort_time)
    task_list = get_formatted_time(task_list)
    if len(task_list) == 0:
        return "------------------\n|  time | items  |\n------------------\n| No items found |\n------------------"
    table_size = get_table_sizes(task_list)
    x = table_size[0]

    y = table_size[1]
    # Header start
    table_lines = [('-' * (x - 1 + y)) + '\n']
    line_1 = '|' + (' ' * (y + 4)) + 'time | items' + (' ' * (x - 19)) + '|\n'
    table_lines.append(line_1)
    table_lines.append(('-' * (x - 1 + y)) + '\n')
    # Header end
    for ele in task_list:
        if len(ele[0]) == 7:
            table_lines.append('| ' + (' ' * y) + ele[0] + ' | ' + ele[1] + (' ' * (x - 14 - len(ele[1]))) + '|\n')
        else:
            table_lines.append('| ' + ele[0] + ' | ' + ele[1] + (' ' * (x - 14 - len(ele[1]))) + '|\n')
    table_lines.append(('-' * (x - 1 + y)) + '\n')
    table = ''.join(table_lines)

    return table

    pass


def get_table_sizes(task_list: list) -> list:
    """Get the maximum sizes for table.

    :param task_list: list
    :return: int
    """
    x = 0
    time_slot = 0
    for ele in task_list:
        if len(ele[1]) > x:
            x = len(ele[1])
        if len(ele[0]) > time_slot:
            time_slot = len(ele[0])
    if x < 5:
        x = 5
    return [x + 15, time_slot - 7]


def normalize(time: list) -> list:
    """Add missing 0's to the minutes and remove extra 0's from hours.

    :param time: str
    :return: list
    """
    empty_list = [''] * len(time)
    for i in range(len(time)):
        empty_list[i] = list(time[i][0])
        if empty_list[i][0] == '0' and empty_list[i][2] == ':':
            empty_list[i].pop(0)
        if empty_list[i][len(empty_list[i]) - 3] != ':':
            empty_list[i].append('0')
        normal_time = ''
        for ele in empty_list[i]:
            normal_time += ele
        empty_list[i] = normal_time
        time[i][0] = empty_list[i]

    return time
    pass


def get_formatted_time(time: list) -> list:
    """Format 24 hour time to the 12 hour time.

    :param time: list
    :return: list
    """
    formatted_time = []
    for ele in time:
        splitter = ele[0].find(':')
        hour = int((ele[0])[:splitter])
        minute = int((ele[0])[len(ele[0]) - 2:])
        suffix = ''
        if hour < 24 and minute < 60:
            if hour >= 12:
                suffix = ' PM'
                if hour > 12:
                    hour -= 12
            else:
                suffix = ' AM'
                if hour == 0:
                    hour = 12
            if minute < 10:
                minute = '0' + str(minute)
            new_format = [str(hour) + ':' + str(minute) + suffix, ele[1]]
            formatted_time.append(new_format)

    return formatted_time
    pass


if __name__ == '__main__':
    print(create_schedule_string("26s11  aa"))
    create_schedule_file("schedule_input.txt", "schedule_output.txt")

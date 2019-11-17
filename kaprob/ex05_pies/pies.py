"""The Pies Eating Competition."""
import csv


def get_competitors_list(filename: str) -> list:
    """
    Get the names of all registered competitors.

    :param filename: is the path to the file with the names of competitors.
    :return: a list containing the names of competitors.
    """
    comp_text = open(filename, 'r')
    list_comp = comp_text.readlines()
    comp_text.close()
    for i in range(len(list_comp)):
        list_comp[i] = list_comp[i].replace('\n', '')
    return list_comp
    pass


def get_results_dict(filename: str) -> dict:
    """
    Get the results and store them in the dictionary.

    Results are following the format 'Firstname Lastname - result'.
    You have to return a dict, where the names of the competitors
    are keys and the results are values (as ints).

    :param filename: is the path to the file with the results.
    :return: a dict containing names as keys and results as values (as ints).
    """
    result_list = get_competitors_list(filename)
    results = {}
    for i in range(len(result_list)):
        name_end = result_list[i].index('-')
        name = result_list[i][:name_end - 1]
        score = int(result_list[i][name_end + 1:])
        results.update({name: score})
    return results
    pass


def filter_results(path_to_competitors: str, path_to_results: str) -> dict:
    """
    Filter out all illegal competitors.

    Illegal competitor is the one, whose name is not in the registered competitors list.
    You have to return a results dict, which doesn't contain the results of illegal competitors.
    Use methods defined above.

    :param path_to_competitors: is the path to the file with the names of competitors.
    :param path_to_results: is the path to the file with the results.
    :return: a dict with correct results.
    """
    comp_list = get_competitors_list(path_to_competitors)
    result_dict = get_results_dict(path_to_results)
    key_list = result_dict.keys()
    not_common = list(set(key_list).difference(comp_list))
    for name in not_common:
        result_dict.pop(name)
    return result_dict

    pass


def sort_results(path_to_competitors: str, path_to_results: str) -> list:
    """
    Sort the filtered results dictionary.

    In order to find the winner you have to sort the results.
    Results have to be sorted based on the cakes eaten by the competitors.
    The sorted results must be in a descending order.
    This means that the more cakes the competitor has eaten the better place they get.
    If there are multiple competitors with the same result the better place goes to the
    competitor, whose place in the registered competitors list is higher.

    For example, if Mati and Kati both have 5 pies eaten and Kati is on a higher place
    than Mati in the registered competitors list, then the better place must go to Kati
    (i.e. Kati gets 4th place and Mati gets 5th).

    It is recommended to use filter_results method here.

    The result has to be a list of tuples (name, result) where result is int (number of cakes eaten).

    :param path_to_competitors: is the path to the file with the names of competitors.
    :param path_to_results: is the path to the file with the results.
    :return: a sorted results list of tuples (name, number of cakes eaten).
    """
    registered_competitors = get_competitors_list(path_to_competitors)
    results = filter_results(path_to_competitors, path_to_results)
    same_score = get_same_score(results, registered_competitors)
    result_list = sorted(results.items(), key=lambda x: x[1], reverse=True)

    throwaway_list = []
    for ele in result_list:
        throwaway_list.append(list(ele))
    for shared in same_score:
        index = 0
        index_set = False
        num_names = len(shared[0])
        for i in range(len(throwaway_list)):
            if index_set:
                break
            if throwaway_list[i][1] == shared[1] and not index_set:
                index = i
                index_set = True
        for i in range(num_names):
            throwaway_list[index + i][0] = shared[0][i]
    new_list = []

    for ele in throwaway_list:
        new_list.append(tuple(ele))
    return new_list

    pass


def find_average_score(results: dict) -> int:
    """
    Find the average score.

    :param results: is a dictionary with the results.
    :return: average score rounded down.
    """
    total = 0
    for name in results:
        total += results[name]
    return total // len(results)
    pass


def write_results_csv(path_to_competitors: str, path_to_results: str, file_to_write: str) -> None:
    """
    Write the filtered and sorted results to csv file.

    The csv file must contain three columns:
    1. Place;
    2. Name;
    3. Result.

    :param path_to_competitors: is the path to the file with the names of competitors.
    :param path_to_results: is the path to the file with the results.
    :param file_to_write: is the name of the csv file.
    :return: None
    """
    result_list = sort_results(path_to_competitors, path_to_results)
    with open(file_to_write, 'w', newline='') as scoreboard:
        writer = csv.writer(scoreboard, delimiter=',')
        writer.writerow(("Place", "Name", "Result"))
        for num in range(len(result_list)):
            writer.writerow((num + 1, result_list[num][0], result_list[num][1]))
    return None


def get_same_score(score_dict: dict, comp_list: list) -> list:
    """
    Find competitors with the same score.

    :param comp_list: list of competitors.
    :param score_dict: competitors and their scores.
    :return: list of names with their scores.
    """
    def get_index(element: str):
        """
        Find index provided.

        :param element: element for index
        :return: index of element in list.
        """
        return comp_list.index(element)

    same_score = {}  # Reversed dict.
    filtered_same_score = []  # Reversed dict where people with the same score are presented together.
    for key, value in score_dict.items():
        same_score[value] = same_score.get(value, [])
        same_score[value].append(key)
    shared_score = same_score.copy()
    for key, value in shared_score.items():
        filtered_same_score.append(list((value, key)))
    for ele in filtered_same_score:
        if len(ele[0]) > 1:
            ele[0] = sorted(ele[0], key=get_index)

    return filtered_same_score


# Some examples based on the given files:
if __name__ == '__main__':
    competitors = get_competitors_list('competitors_list.txt')
    results_dict = get_results_dict('results.txt')
    filtered_results = filter_results('competitors_list.txt', 'results.txt')
    sorted_results = sort_results('competitors_list.txt', 'results.txt')

    print('Check the lengths:')
    print(len(competitors))  # -> 66
    print(len(results_dict))  # -> 93
    print(len(filtered_results))  # -> 66
    print(len(sorted_results))  # -> 66

    print('Check results for certain competitors:')
    print(results_dict['Marina Eley'])  # -> 35
    print(results_dict['Takako Vena'])  # -> 7
    print(results_dict['So Koziel'])  # -> 5
    print(results_dict['Macy Tenenbaum'] == 22)  # -> True
    print(results_dict['Edwina Alaniz'] == 48)  # -> False

    print('Check presence of the illegal competitors:')
    print('Tiffanie Mcdaniel' not in filtered_results)  # -> True
    print('Ela Gallow' not in filtered_results)  # -> True
    print('Sam Cheney' not in filtered_results)  # -> True
    print('Jayme Malachi' not in filtered_results)  # -> True
    print('Sabine Danos' not in filtered_results)  # -> True

    print('Check the order of the sorted results (must be descending):')
    values = [result[1] for result in sorted_results]
    print(all(values[i] >= values[i + 1] for i in range(65)))  # -> True

    print('Check places for certain competitors:')
    keys = [result[0] for result in sorted_results]
    print(keys.index('Ewa Grothe') + 1)  # -> 5
    print(keys.index('Cedrick Span') + 1)  # -> 20
    print(keys.index('Morris Ragusa') + 1)  # -> 37
    print(keys.index('Jaak Aaviksoo') + 1)  # -> 23
    print(keys.index('Ago Luberg') + 1)  # -> 66

    print('Check the average value:')
    print(find_average_score(results_dict))  # -> 19
    print(find_average_score(filtered_results))  # -> 19

    print('Write the results to CSV file:')
    write_results_csv('competitors_list.txt', 'results.txt', 'correct_results.csv')

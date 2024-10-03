# Selection Sort is more efficient than bogo sort algorithm.But it still works slow when data is to much.


unsorted_list = []

# Opening a text file contains numbers.
with open('unsorted_list.txt', 'r') as file:
    for line in file:
        '''
        We are appending numbers in txt file to empty list.
        '''
        unsorted_list.append(int(line.strip()))


def selection_sort(values):
    sorted_list = []
    for i in range(0, len(values)):
        index_to_move = index_of_min(values)
        sorted_list.append(values.pop(index_to_move))
    return sorted_list


def index_of_min(values):
    """
    Returns the index of the smallest value in unsorted list.
    """
    min_index = 0
    for i in range(1, len(values)):
        if values[i] < values[min_index]:
            min_index = i
    return min_index


print(selection_sort(unsorted_list))



# Merge Sort algorithm with recursive.It's faster than other merge sort algorithm which is written with while loops.

unsorted_list = []

# Opening a text file contains numbers.
with open('unsorted_list.txt', 'r') as file:
    for line in file:
        '''
        We are appending numbers in txt file to empty list.
        '''
        unsorted_list.append(int(line.strip()))


def merge_sort(values):
    if len(values) <= 1:
        return values
    # We split unsorted list two pieces.
    middle_index = len(values) // 2
    left_values = merge_sort(values[:middle_index])
    right_values = merge_sort(values[middle_index:])
    sorted_list = []
    left_index = 0
    right_index = 0
    # Comparing left values in the left sublist with right values in the right sublist.
    while left_index < len(left_values) and right_index < len(right_values):
        if left_values[left_index] < right_values[right_index]:
            sorted_list.append(left_values[left_index])
            left_index += 1
        else:
            sorted_list.append(right_values[right_index])
            right_index += 1
    # We add remaining values to sorted list after while loop ends.
    sorted_list += left_values[left_index:]
    sorted_list += right_values[right_index:]
    return sorted_list


print(merge_sort(unsorted_list))


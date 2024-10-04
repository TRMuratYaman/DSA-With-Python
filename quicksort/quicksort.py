# Quicksort algorithm is faster than selection sort algorithm bcs of we use recursive method.

unsorted_list = []

# Opening a text file contains numbers.
with open('unsorted_list.txt', 'r') as file:
    for line in file:
        '''
        We are appending numbers in txt file to empty list.
        '''
        unsorted_list.append(int(line.strip()))


def quicksort(values):
    # We divide the unsorted list to sublist until lists we have only one element.
    if len(values) <= 1:
        return values
    # We choose the pivot element as the first index value of unsorted list every time we call quicksort function.
    pivot = values[0]
    less_than_pivot = []
    greater_than_pivot = []
    for value in values[1:]:
        # we add the elements which values smaller than the pivot element.
        if value <= pivot:
            less_than_pivot.append(value)
            # we add the elements which values bigger than the pivot element.
        else:
            greater_than_pivot.append(value)
    return quicksort(less_than_pivot) + [pivot] + quicksort(greater_than_pivot)


print(quicksort(unsorted_list))

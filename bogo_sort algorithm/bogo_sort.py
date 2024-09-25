# This algorithm is an inefficient sorting algorithm used in computer science for educational purposes.

import random

numbers = []
# Opening a text file contains numbers.
with open('unsorted_numbers.txt', 'r') as file:
    for line in file:
        '''
        We are appending numbers in txt file to empty list.
        '''
        numbers.append(int(line.strip()))

# Checking numbers of the list is sorted or not.
def is_sorted(values):
    for index in range(len(values) - 1 ):
        if values[index] > values[index + 1]:
            return False
    return True

# This function shuffles values in the list until list get sorted.
def bogo_sort(values):
    count = 0
    while not is_sorted(values):
        print(count)
        random.shuffle(values)
        count += 1
    return values


print(bogo_sort(numbers))
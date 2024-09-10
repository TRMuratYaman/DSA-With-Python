
def merge_sort(array):
    """
    This function sorts an array in ascending order.Returns a sorted array.
    Time Complexity = O(n log n)
    """
    if len(array) <= 1:
        return array
    left_half, right_half = split(array)
    left = merge_sort(left_half)
    right = merge_sort(right_half)

    return merge(left, right)

def split(array):
    """
    This function divides an unsorted array into subarrays.Returns two subarrays called left and right.
    Time Complexity = O(log n)
    """

    midpoint = len(array) // 2
    left = array[:midpoint]
    right = array[midpoint:]

    return left, right
def merge(left, right):
    """
    This function merges two subarrays and returns one sorted array.
    Time Complexity = O(n)
    """

    sorted_array = []
    i = 0
    j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            sorted_array.append(left[i])
            i += 1
        else:
            sorted_array.append(right[j])
            j += 1

    while j < len(right):
        sorted_array.append(right[j])
        j += 1

    while i < len(left):
        sorted_array.append(left[i])
        i += 1

    return sorted_array


def is_sorted(array):
    """
    This function checks an array is sorted or not recursively.Returns True or False.
    """
    if len(array) == 0 or len(array) == 1:
        return True
    return array[0] <= array[1] and is_sorted(array[1:])

arr1 = [20 ,20 ,20 ,10 ,35 ,70 ,65 ,1000 ,2041 ,5 ,1 ,0 ,2 ,3 ,4 ,48 ,56 ,65 ,80 ,90 ,85]
print(is_sorted(arr1))
arr2 = merge_sort(arr1)
print(arr2)
print(is_sorted(arr2))

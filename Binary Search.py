

def binary_search(arr, target):
    """
    This function returns the index of the element in arr that has the target value,else returns None.
    Note : The input array is assumed to be sorted.
    Time Complexity of this function : O(log(n))
    """
    first = 0
    last = len(arr) - 1
    while first <= last:
        middle = (first + last) // 2
        if arr[middle] == target:
            return middle
        elif arr[middle] < target:
            first = middle + 1
        else:
            last = middle - 1
    return None


def verify(index):
    if index is not None:
        print("Target found at index :", index)
    else:
        print("Target not found in array.")


result = binary_search([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 20, 25, 30, 35, 40],40)
verify(result)

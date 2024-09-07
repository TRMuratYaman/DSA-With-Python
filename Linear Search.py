

def linear_search(arr, target):
    """
    This function returns the index of the element in arr that has the target value,else returns None.
    Time Complexity of this function : O(n)
    """
    for i in range(0, len(arr)):
        if arr[i] == target:
            return i
    return None


def verify(index):
    if index is not None:
        print("Target found at index :", index)
    else:
        print("Target not found in array.")


result = linear_search([10, 25, 30, 45, 5, 100, 33, 65, 78, 97, 24], 97)
verify(result)

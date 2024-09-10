

def binary_search_recursive(arr, target):
    """ This function's time complexity is the same as iterative binary search.But this one uses memory stack.That means more memory usage."""

    if len(arr) == 0:
        return False
    else:
        middle = (len(arr))//2
        if arr[middle] == target:
            return True
        else:
            if arr[middle] < target:
                return binary_search_recursive(arr[middle + 1:], target) # inclusive
            else:
                return binary_search_recursive[arr[:middle], target] # exclusive



def verify(result):
    print("Target in the array : ", result)


result = binary_search_recursive([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 85, 95, 100, 150, 200], 35)
verify(result)

result = binary_search_recursive([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 85, 95, 100, 150, 200], 250)
verify(result)

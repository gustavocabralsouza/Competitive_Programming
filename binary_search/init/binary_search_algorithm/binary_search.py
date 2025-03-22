def binary_search_recursive(array, item, begin=0, end=None):
    if end is None:
        end = len(array) - 1
    if begin <= end:
        middle = (end + begin) // 2
        if array[middle] == item:
            return middle
        if item < array[middle]:
            return binary_search_recursive(array, item, begin, middle - 1)
        else: 
            return binary_search_recursive(array, item, middle + 1, end)
    return None 


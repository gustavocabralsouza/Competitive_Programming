
def binary_search_recursive(array, item, begin=0, end=None):
    if end is None:
        end = len(array) - 1
    if begin <= end:
        middle = (end + begin) // 2
        if array[middle] == item:
            return middle
        if item < array[middle]: #present in the left array
            return binary_search_recursive(array, item, begin, middle - 1)
        else: #present in the right array
            return binary_search_recursive(array, item, middle + 1, end)
    return None # item element is not present in the array

if __name__== '__main__':
    lista = [1, 2, 3, 4, 5, 6]
    index = binary_search_recursive(lista, 4)
    print(index)

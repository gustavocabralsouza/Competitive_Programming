import random
from binary_search import binary_search_recursive

empty = []
single = [7]
pair = [3, 7]
odd = [1, 2, 3, 5, 7, 8, 9, 13, 27, 31, 43]
even = [1, 2, 3, 5, 7, 8, 9, 13, 27, 31, 43, 70]
repeated = [1, 2, 2, 5, 5, 5, 9, 13, 21, 21, 21, 21]

def test_empty():
    return binary_search_recursive(empty, random.randint(0, 1000)) is None

def test_single():
    if binary_search_recursive(single, 7) is None:
        return False
    if binary_search_recursive(single, 10) is not None:
        return False
    return True

if __name__ == "__main__":
    print("*******************************")
    print("PASSED EMPTY" if test_empty() else "FAILED EMPTY")
    print("PASSED SINGLE" if test_single() else "FAILED SINGLE")

    test_cases = { 
        'Pair': pair, 
        'Odd': odd,
        'Even': even,
        'Repeated': repeated
    }

    again = 'y'
    while again == 'y':
        for name, array in test_cases.items():
            print("\nTest case: {}\n{}".format(name, array))
            e = int(input("Element to find: "))
            i = binary_search_recursive(array, e)
            print("\n  Found Index:", i)
        again = input("Repeat? (Y/N): ").strip().lower()
    print("*******************************")

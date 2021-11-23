# write a program to find the position of a given number
# in a list of numbers arranged in decreasing order. We
# also need to minimise the number of time we access elements
# from the list.

# INPUT
# cards: a list of sorted numbers
# query: a number, who position in the array is to be determined

# OUTPUT
from jovian.pythondsa import evaluate_test_case

# position: the position of the var query in the list cards
test = {
    'input': {
        'cards': [13, 11, 10, 7, 4, 3, 1, 0],
        'query': 7
    },
    'output': 7
}

def locate_card(cards, query):
    position = 0

    print('cards:', cards)
    print('query:', query)

    while position < len(cards):
        print('position:', position)
        if cards[position] == query:
            return position
        position += 1
    return -1

result = locate_card(test['input']['cards'], test['input']['query'])
print(result)
evaluate_test_case(locate_card,test)



# x is the array position
def recursive_binary_search(arr, low, high, x):
    if high >= low:
        mid = (high + low) // 2
        # if element is found at the middle
        if arr[mid] == x:
            return mid

        # if element is less than mid, it must be in left
        # sub-array
        elif arr[mid] > x:
            return recursive_binary_search(arr, mid - 1, high, x)

        else:
            return recursive_binary_search(arr, mid + 1, high, x)
    else:
        # if not found in the array
        return -1

arr = [i for i in range(15000)]
# print(arr)
x = 14
# Function call
# result = recursive_binary_search(arr, 0, len(arr) - 1, x)
#
# if result != -1:
#     print("Element is present at index", str(result))
# else:
#     print("Element is not present in array")

def iterative_binary_search(arr, x):
    low = 0
    high = len(arr)-1
    mid = 0

    while low <= high:
        mid = (high + low) // 2

        if arr[mid] < x:
            low = mid + 1

        elif arr[mid] > x:
            high = mid - 1

        else:
            return mid
    return -1


result = iterative_binary_search(arr, x)

if result != -1:
    print("Element is present at index", str(result))
else:
    print("Element is not present in array")

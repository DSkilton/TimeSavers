# write a program to find the position of a given number
# in a list of numbers arranged in decreasing order. We #
# also need to minimise the number of time we access elements
# from the list.

# INPUT
# cards: a list of sorted numbers
# query: a number, who position in the array is to be determined

#OUTPUT
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

    while True:
        print('position:', position)
        if cards[position] == query:
            return position

        position += 1

        if position ==len(cards):
            return -1

result = locate_card(test['input']['cards'], test['input']['query'])
print(result)
evaluate_test_case(locate_card,test)
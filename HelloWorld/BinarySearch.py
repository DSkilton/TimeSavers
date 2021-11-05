# write a program to find the position of a given number
# in a list of numbers arranged in decreasing order. We #
# also need to minimise the number of time we access elements
# from the list.

# INPUT
# cards: a list of sorted numbers
# query: a number, who position in the array is to be determined

#OUTPUT
# position: the position of the var query in the list cards

cards = [13, 11, 10, 7, 4, 3, 1, 0]
query = 7
# TEST CASE
output = 3

def locate_card(cards, query):
    #print(cards, query)
    pass

result = locate_card(cards, query)
print(result)

print(result == output)
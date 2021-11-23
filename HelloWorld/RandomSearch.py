import random

fruits = ['orange', 'plum', 'banana', 'apple']


def find(elements, value):
    while True:
        random_element = random.randint(0, len(fruits) - 1)
        if elements[random_element] == value:
            return random_element
        elif value not in elements:
            return False


print(find(fruits, "plum"))

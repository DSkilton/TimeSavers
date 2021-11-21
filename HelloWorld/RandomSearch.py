import random
fruits = ['orange', 'plum', 'banana', 'apple']


def find(elements, value):
    while True:
        random_element = random.choice(elements)
        if random_element == value:
            return random_element


find(fruits, "plum")

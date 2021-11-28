import random
import string


def tuple_dict():
    tuple_example = ("a", 2, "password", "Password")

    for mutable in enumerate(tuple_example):
        hash_example = hash(mutable)
        print(hash_example)

def random_string(length):
    result = ''.join((random.choice(string.ascii_lowercase) for x in range(length)))
    return result


def generate_dict():
    for i in range(100000):
        print("'" + random_string(random.randint(1, 10)) + "'"
              + ", " + "'" + random_string(random.randint(1, 10)) + "'")

generate_dict()
import time


def sum_of_n_2(n):
    start = time.time()
    the_sum = 0
    for i in range(1, n + 1):
        the_sum = the_sum + i
        end = time.time()

    return the_sum, end - start


def sum_of_n(n):
    start = time.time()
    the_sum = (n * (n + 1) / 2)
    print(the_sum)
    end = time.time()

    return the_sum, end - start


# print("the sum is %d and the time is %10.8f" % sum_of_n(10))

list_ints = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31,
 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61,
 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91,
 92, 93, 94, 95, 96, 97, 98, 99, 100]


def generate_list():
    for number in range(100):
        list_ints.append(str(number) + ", ")


# print(list)

def linear_search(query_number):
    position = 0
    # low = 0
    # high = len(list_ints - 1)

    while True:
        if list_ints[position] == query_number:
            return "Found at position ", position

        position += 1

        if position == len(list_ints):
            return "Not found"


print(linear_search(12))

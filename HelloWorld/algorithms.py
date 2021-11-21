# Import the timeit module
# Import the Timer class defined in the module
import timeit
from timeit import Timer
import numpy as np
import matplotlib.pyplot as plt

def plot_big_o():

    # Stylesheets defined in Matplotlib
    plt.style.use('bmh')

    # Set up runtime comparisons
    n = np.linspace(1, 50, 1000)
    labels = ['Constant', 'Logarithmic', 'Linear']
    big_o = [np.ones(n.shape), np.log(n), n]

    # Plot setup
    plt.figure(figsize=(12, 10))
    plt.ylim(0, 50)

    for i in range(len(big_o)):
        plt.plot(n, big_o[i], label=labels[i])

    plt.legend(loc=0)
    plt.ylabel('Relative Runtime')
    plt.xlabel('Input Size')
    plt.savefig('big-o-notation.png')


plot_big_o()


def test1():
    list = []
    for i in range (1000):
        list = list + [i]

def test2():
    list = []
    for i in range (1000):
        list.append(i)

def test3():
    list = [i for i in range (1000)]

def test4():
    list1 = list(range(1000))


t1 = Timer("test1()", "from __main__ import test1")
print("concat ",t1.timeit(number=1000), "milliseconds")
t2 = Timer("test2()", "from __main__ import test2")
print("append ",t2.timeit(number=1000), "milliseconds")
t3 = Timer("test3()", "from __main__ import test3")
print("comprehension ",t3.timeit(number=1000), "milliseconds")
t4 = Timer("test4()", "from __main__ import test4")
print("list range ",t4.timeit(number=1000), "milliseconds")

def algorithm1():
    a = 5
    b = 6
    c = 10
    n = 10

    range(n)

    for i in range(n):
        for j in range(n):
            x = i * i
            y = j * j
            z = i * j
            print(x)
            print(y)
            print(z)

    for k in range(n):
        w = a * k + 45
        v = b * b
        print(w)
        print(v)
    d = 33


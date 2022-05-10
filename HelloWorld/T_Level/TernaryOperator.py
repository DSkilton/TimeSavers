x = 79

def if_to_ternary():
    if(x % 2 == 0):
        print('even')
    else:
        print('false')

    #Ternary operator
    even = 'even' if x % 2 == 0 else 'false'
    print(even)


def if_to_ternary():
    grade = ('A' if (x >= 90) else ('B' if (x >= 80) else 'C'))
    print('Grade is ' + str(grade))


print(if_to_ternary())

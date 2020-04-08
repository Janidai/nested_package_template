# Title     : TODO
# Objective : TODO
# Created by: noonwave
# Created on: 4/6/20

from example_pkg import fun_2
from example_pkg import sub_pkg_2

print(sub_pkg_2.message)

fun_2("hello")


def is_prime(number):
    """Retrun True if *number* is prime."""
    for element in range(2, number):
        if number % element == 0:
            return False
    return True

def print_next_prime(number):
    """Print the closet prime number larger than *number*."""
    index = number
    while True:
        index +=1
        if is_prime(index):
            print(index)

def main():
    people = [Person('Janid')]
    print(people)
    for i in range(6):
        print(i)





if __name__ == '__main__':
    main()

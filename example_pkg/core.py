# Title     : TODO
# Objective : TODO
# Created by: noonwave
# Created on: 4/6/20

from example_pkg import message, sub_pkg_2


"""
Method 1: import package and use modules as methods
Step 1: in /sub_pkg_1/__init__.py add
"""
# from example_pkg.sub_pkg_1 import mod_one
# from example_pkg.sub_pkg_1 import mod_two
"""
in example_pkg/code.py
You can import
"""
# from example_pkg import sub_pkg_1 as pkg_1
# name = "janid"
# pkg_1.mod_one.stringToUpper(name)
#


"""
Method 2: import package and use modules as methods
Step 1: in /sub_pkg_1/__init__.py add
"""
# from example_pkg.sub_pkg_1.mod_two import stringToLower
# from example_pkg.sub_pkg_1.mod_one import stringToUpper
"""
in example_pkg/code.py
You can import
"""
# from example_pkg import sub_pkg_1
# name = "janid"
# pkg_1.stringToLower(name)
# pkg_1.mod_one

from example_pkg import sub_pkg_1

sub_pkg_1.nested_pkg_1.nested_function()


sub_pkg_1.stringToUpper("janid")

sub_pkg_1.nest.nested_function()


#1) from example_pkg import fun_2 -> works




sub_pkg_1.stringToLower()

name = "janid"

stringToLower(name)

stringToUpper(name)


# from .supporters import fun_2 -> Error




print(sub_pkg_2.message)
print(message)

fun_2("hello")

print("janid")
print("janid_s")
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

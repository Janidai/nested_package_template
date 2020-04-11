# Title     : TODO
# Objective : TODO
# Created by: noonwave
# Created on: 4/6/20

from example_pkg import Person, sub_pkg_1
from example_pkg.sub_pkg_1 import nested_pkg_1

print(nested_pkg_1.nested_function())

sub_pkg_1.hello("janid")


def main():
    people = []
    for i in range(1, 3):
        people.append(Person('name_' + str(i)))
    for person in people:
        print(person.name)


if __name__ == '__main__':
    main()

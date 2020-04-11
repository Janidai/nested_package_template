# Title     : TODO
# Objective : TODO
# Created by: noonwave
# Created on: 4/6/20

from example_pkg import Person
from example_pkg.sub_pkg_1 import nested_pkg_1

print(nested_pkg_1.nested_function())

sub_pkg_1.string_to_upper("janid")



def main():
    people = []
    people.append(Person('Janid'))
    for person in people:
        print(person.name)


if __name__ == '__main__':
    main()

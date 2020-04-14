# Title     : TODO
# Objective : TODO
# Created by: noonwave
# Created on: 4/6/20

from example_pkg import sub_pkg_1
from example_pkg import sub_pkg_2
from example_pkg.sub_pkg_1 import nested_pkg_1
from example_pkg import greetings




def main(person):
    str_1 = sub_pkg_1.hello()
    str_2 = sub_pkg_1.world()
    str_3 = sub_pkg_2.to()
    person = sub_pkg_2.Person(person)
    str_4 = nested_pkg_1.nested_function()
    greetings(str_1, str_2, str_3, person.name, str_4)



if __name__ == '__main__':
    import sys
    name = sys.argv[1]
    #name = input()
    main(name)

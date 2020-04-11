# Title     : TODO
# Objective : TODO
# Created by: noonwave
# Created on: 4/11/20

from example_pkg import sub_pkg_1
from example_pkg import sub_pkg_2
from example_pkg.sub_pkg_1 import nested_pkg_1
from example_pkg.helpers import greetings

def test_greetings(capsys):

    str_1 = sub_pkg_1.hello()
    str_2 = sub_pkg_1.world()
    str_3 = sub_pkg_2.to()
    person = sub_pkg_2.Person("janid")
    str_4 = nested_pkg_1.nested_function()

    greetings(str_1, str_2, str_3, person.name, str_4)
    captured = capsys.readouterr()
    assert captured.out == "Hello World to janid !!!\n"

    person = sub_pkg_2.Person("")
    greetings(str_1, str_2, str_3, person.name, str_4)
    captured = capsys.readouterr()
    assert captured.out == "Hello World to nobuddy !!!\n"


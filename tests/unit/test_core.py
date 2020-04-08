# Title     : TODO
# Objective : TODO
# Created by: noonwave
# Created on: 4/8/20
import pytest
from example_pkg import is_prime

# Shortcut to run the test_ ctrl+shif+F10
x = 8
class Testis_prime:
    def test_is_prime(self):
        assert is_prime(5)

    @pytest.mark.skipif(x>4, reason="Too big")
    def test_is_not_prime(self):
        assert is_prime(6) == False

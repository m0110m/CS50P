import pytest
from jar import Jar


def test_init():
    jar = Jar(10)
    assert jar.capacity == 10

def test_str():
    jar = Jar()
    assert str(jar) == ""
    jar.deposit(1)
    assert str(jar) == "🍪"
    jar.deposit(11)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"


def test_deposit():
    jar = Jar()
    jar.deposit(10)
    assert jar.size == 10
    with pytest.raises(ValueError):
        jar.deposit(9)


def test_withdraw():
    jar = Jar()
    jar.deposit(8)
    jar.withdraw(4)
    assert jar.size == 4
    with pytest.raises(ValueError):
        jar.withdraw(14)

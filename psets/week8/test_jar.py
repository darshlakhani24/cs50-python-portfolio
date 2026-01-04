from jar import Jar
import pytest

def test_init_default():
    jar = Jar()
    assert jar.capacity == 12
    assert jar.size == 0

def test_init_custom_capacity():
    jar = Jar(5)
    assert jar.capacity == 5

def test_invalid_capacity():
    with pytest.raises(ValueError):
        Jar(-1)
    with pytest.raises(ValueError):
        Jar("big")

def test_str():
    jar = Jar()
    jar.deposit(3)
    assert str(jar) == "🍪🍪🍪"

def test_deposit():
    jar = Jar(5)
    jar.deposit(2)
    assert jar.size == 2
    with pytest.raises(ValueError):
        jar.deposit(4) 

def test_withdraw():
    jar = Jar(5)
    jar.deposit(3)
    jar.withdraw(2)
    assert jar.size == 1
    with pytest.raises(ValueError):
        jar.withdraw(5)

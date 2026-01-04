from fuel import convert, gauge
import pytest
def test_convert_valid():
    assert convert("1/2") == 50
    assert convert("3/4") == 75
    assert convert("0/4") == 0
    assert convert("1/1") == 100

def test_convert_zero_division():
    with pytest.raises(ZeroDivisionError):
        convert("1/0")

def test_convert_invalid_value():
    with pytest.raises(ValueError):
        convert("5/4")
    with pytest.raises(ValueError):
        convert("cat/dog")

def test_gauge_e():
    assert gauge(0) == "E"
    assert gauge(1) == "E"

def test_gauge_f():
    assert gauge(99) == "F"
    assert gauge(100) == "F"

def test_gauge_percentage():
    assert gauge(50) == "50%"
    assert gauge(25) == "25%"

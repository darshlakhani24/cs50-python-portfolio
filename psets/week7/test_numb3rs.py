from numb3rs import validate

def test_valid_addresses():
    assert validate("192.168.0.1") == True
    assert validate("0.0.0.0") == True
    assert validate("255.255.255.255") == True

def test_invalid_format():
    assert validate("192.168.1") == False
    assert validate("192.168.1.1.1") == False
    assert validate("192.168..1") == False
    assert validate("192.168.01.1") == True  # leading zero allowed in this implementation

def test_out_of_range():
    assert validate("256.100.100.100") == False
    assert validate("100.256.100.100") == False
    assert validate("100.100.300.100") == False
    assert validate("100.100.100.999") == False

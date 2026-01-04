from plates import is_valid

def test_length():
    assert is_valid("AB") == True
    assert is_valid("ABCDEF") == True
    assert is_valid("A") == False
    assert is_valid("ABCDEFG") == False

def test_start_letters():
    assert is_valid("AB123") == True
    assert is_valid("A1234") == False
    assert is_valid("1ABC") == False

def test_numbers_at_end():
    assert is_valid("AB123") == True
    assert is_valid("AB12C3") == False
    assert is_valid("AB123C") == False

def test_no_leading_zero():
    assert is_valid("AB012") == False
    assert is_valid("AB102") == True

def test_only_alphanumeric():
    assert is_valid("AB.CD") == False
    assert is_valid("AB CD") == False
    assert is_valid("AB@12") == False
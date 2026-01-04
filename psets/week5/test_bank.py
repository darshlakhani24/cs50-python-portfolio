from bank import value

def test_hello():
    assert value("hello") == 0
    assert value("Hello there") == 0
    assert value("HELLO!") == 0

def test_h_only():
    assert value("hi") == 20
    assert value("Hey") == 20
    assert value("Hmmm") == 20

def test_other():
    assert value("What's up?") == 100
    assert value("Good morning") == 100
    assert value("yo") == 100
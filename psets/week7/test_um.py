from um import count

def test_single_um():
    assert count("um") == 1
    assert count("Um") == 1
    assert count("hello, um, world") == 1

def test_multiple_um():
    assert count("um um um") == 3
    assert count("Um? Um. UM!") == 3

def test_not_substring():
    assert count("yummy") == 0
    assert count("album") == 0
    assert count("documentum") == 0

def test_mixed_cases_and_punctuation():
    assert count("Um, I think, um... UM!") == 3
    assert count("Umm, I said um.") == 1

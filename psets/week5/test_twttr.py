from twttr import shorten

def test_shorten_lowercase():
    assert shorten("twitter") == "twttr"

def test_shorten_uppercase():
    assert shorten("TWITTER") == "TWTTR"

def test_shorten_mixed_case():
    assert shorten("TwItTeR") == "TwtTR"

def test_shorten_with_numbers():
    assert shorten("h3ll0") == "h3ll0"

def test_shorten_with_punctuation():
    assert shorten("hello!") == "hll!"

def test_shorten_all_vowels():
    assert shorten("aeiouAEIOU") == ""

def test_shorten_empty_string():
    assert shorten("") == ""

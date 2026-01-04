from project import split_equal, tip, generate_summary

# Tests split_equal function
def test_split_equal():
    people = ["Darsh", "Aditya", "Neil]
    total = 90
    expected = {"Darsh": 30.0, "Aditya": 30.0, "Neil": 30.0}
    assert split_equal(total, people) == expected

# Tests tip function
def test_tip():
    total = 100
    tip_percent = 15
    expected = 115.0
    assert tip(total, tip_percent) == expected

# Tests generate_summary function
def test_generate_summary():
    split = {"Darsh": 20.0, "Neil": 30.0}
    total = 50
    summary = generate_summary(split, total)

    assert "Darsh owes ₹20.0" in summary
    assert "Neil owes ₹30.0" in summary
    assert "Total Bill: ₹50" in summary

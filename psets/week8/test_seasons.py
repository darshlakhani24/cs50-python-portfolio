from seasons import get_minutes_since_birth
from datetime import date

def test_minutes_today():
    today = date.today().isoformat()
    assert get_minutes_since_birth(today) == 0

def test_minutes_yesterday():
    today = date.today()
    yesterday = today.replace(day=today.day - 1)
    assert get_minutes_since_birth(yesterday.isoformat()) == 1440

def test_minutes_known_date():
    assert get_minutes_since_birth("2000-01-01") > 10**6

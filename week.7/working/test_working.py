from working import convert
import pytest

def test_one():
    assert convert("2 AM to 4 PM") == "02:00 to 16:00"
    assert convert("12:45 AM to 5:54 PM") == "00:45 to 17:54"


def tes_two():
    assert convert("9:12 PM to 1 PM") == "21:12 to 13:00"
    assert convert("8 AM to 4:19 PM") == "08:00 to 16:19"

def test_three():
    with pytest.raises(ValueError):
        convert("4 PM to 4:60")

def test_four():
    with pytest.raises(ValueError):
        convert("09:00 AM to 17:00 PM")

def test_five():
    with pytest.raises(ValueError):
        convert("9 AM - 5 PM")
def test_six():
    with pytest.raises(ValueError):
        convert("9:60 AM to 5:60 PM")


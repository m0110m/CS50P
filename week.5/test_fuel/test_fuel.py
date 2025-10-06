from fuel import convert, gauge
import pytest

def test_convert():
    with pytest.raises(ZeroDivisionError):
        convert("0/0")
    with pytest.raises(ValueError):
        convert("7/4")
    with pytest.raises(ValueError):
        convert("-1/2")
    assert convert("2/4") == 50


def test_gauge():
    assert gauge(1) == "E"
    assert gauge(75) == "75%"
    assert gauge(99) == "F"

from seasons import return_date
from datetime import date

def test_return_date():
    assert return_date("1999-10-05") == date(1999,10,5)

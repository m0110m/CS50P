from plates import is_valid

def test_one():
    assert is_valid("CS.50") == False
    assert is_valid("CS50") == True

def test_two():
    assert is_valid("H") == False
    assert is_valid("GOODBYE") == False

def test_three():
    assert is_valid("88") == False
    assert is_valid("7TT") == False

def test_four():
    assert is_valid("AA02") == False
    assert is_valid("CS50P") == False
    assert is_valid("AA11") == True

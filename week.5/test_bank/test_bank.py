from bank import value

def test_one():
    assert value("Hello") == 0
    assert value("HELLOO") == 0
    assert value("hello there") == 0

def test_two():
    assert value("Hey!") == 20
    assert value("How are you?") == 20

def test_three():
    assert value("What's up") == 100
    assert value("THIS IS CS50") == 100

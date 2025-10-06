from numb3rs import validate

def test_one():
    assert validate("1.2.3.4") == True
    assert validate("255.255.0.255") == True

def test_two():
    assert validate("256.0.1.23") == False
    assert validate("1.2.2.3.5") == False
    assert validate("5555") == False
    assert validate("0.0.0.259") == False


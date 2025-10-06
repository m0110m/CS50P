from um import count

def test_one():
    assert count("UM") == 1
    assert count("Um") == 1
    assert count("um") == 1


def test_two():
    assert count("thank you, um, for the album") == 1
    assert count("This is umy, um..") == 1

def test_three():
    assert count("um, hello, um, world") == 2
    assert count("yum") == 0

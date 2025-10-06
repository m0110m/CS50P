from twttr import shorten

def test_shorten():
    assert shorten("CS50") == "CS50"
    assert shorten("HeLLO") == "HLL"
    assert shorten("PI = 3.14") == "P = 3.14"
    assert shorten("HELLO FRIEND") == "HLL FRND"
    assert shorten("this is cs50, python") == "ths s cs50, pythn"

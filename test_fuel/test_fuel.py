from fuel import gauge
from fuel import convert


def testcase():
    assert convert("5/10") == "50%"
    assert convert("99/100") == "F"
    assert convert("1/100") == "E"

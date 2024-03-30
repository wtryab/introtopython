from bank import value

def test_case1():
    assert value("Hello")=="$0"

def test_case2():
    assert value("")=="$100"

def test_case3():
    assert value("HEY")=="$20"
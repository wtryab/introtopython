from plates import is_valid

def test1():
    assert is_valid("ABCDDE")==True

def test2():
    assert is_valid("ABC239")==True

def test3():
    assert is_valid("PD2DJS")==False

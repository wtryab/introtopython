from test_twttr.twttr2 import shorten
def test_shorten():
    assert shorten("hello")=="hll"
    assert shorten("PEOP")=="PP"
    assert shorten("")==""

test_shorten()
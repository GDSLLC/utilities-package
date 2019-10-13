import re

from utilitiespackage.python_utils.converters import to_int

def test_to_int():
    assert to_int('abc') == 0
    assert to_int('1') == 1
    assert to_int('abc123abc', regexp='(\d+)') == 123
    assert to_int('abc123abc456', regexp=True) == 123
    assert to_int('123abc', regexp=re.compile('(\d+)')) == 123

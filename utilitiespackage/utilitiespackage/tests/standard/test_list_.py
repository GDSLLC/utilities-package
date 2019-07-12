from utilitiespackage.standard.list_ import groupby_count, is_iterable, iterate


def test_standard_list_groupby_count():
    assert list(groupby_count([1, 1, 1, 2, 3])) == [(1, 3), (2, 1), (3, 1)]


def test_standard_list_is_iterable():
    assert is_iterable("foo") == False
    assert is_iterable(["foo"]) == True
    assert is_iterable(["foo"], unless=list) == False
    assert is_iterable(range(5)) == True


def test_standard_list_iterate():
    assert iterate("foo") == ["foo"]
    assert iterate(["foo"]) == ["foo"]
    assert iterate(["foo"], unless=list) == [["foo"]]
    assert list(iterate(range(5))) == [0, 1, 2, 3, 4]

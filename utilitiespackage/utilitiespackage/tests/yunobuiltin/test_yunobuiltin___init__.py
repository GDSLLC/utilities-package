from utilitiespackage.yunobuiltin import gensym, isa, interleave, is_even, is_iterable, new_list, new_iter, new_tuple, juxt, flatten, is_str_or_bytes, identity, is_map, is_seq, append, prepend

def test_gensym():
    identifier = gensym()
    assert isinstance(identifier, str)

def test_isa():
    assert isa(1,1)
    class NewStyleClass(object):
        pass
    nsc = NewStyleClass()
    assert isa(nsc, object)

def test_is_even():
    assert is_even(2)

def test_is_iterable():
    assert is_iterable([])

def test_new_list():
    assert new_list(1,2,3) == [1,2,3]

def test_new_iter():
    assert list(new_iter(1,2,3)) == [1,2,3]

def test_new_tuple():
    assert new_tuple(1,2,3) == (1,2,3)

def test_flatten():
    assert list(flatten([[[1,2,3]]])) == [1,2,3]

def test_is_str_or_bytes():
    assert is_str_or_bytes("test")
    assert is_str_or_bytes(123) == False

def test_identity():
    assert identity(1) == 1

def test_is_map():
    assert is_map({"abc": 123})

def test_is_seq():
    assert is_seq([1,2,3])

def test_append():
    assert append([], 1, 2, 3) == [1,2,3]
    assert list(append([0], 1, 2, 3)) == [0,1,2,3]
    assert append([], 1, 2, 3) == [1,2,3]
    assert list(append([0], 1, 2, 3)) == [0,1,2,3]

def test_prepend():
    assert list(prepend(1, [1,2,3])) == [1,1,2,3]

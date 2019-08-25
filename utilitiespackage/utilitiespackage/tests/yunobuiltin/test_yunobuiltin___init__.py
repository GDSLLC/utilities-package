import operator
from functools import partial

from utilitiespackage.yunobuiltin import (
    get,
    gensym,
    isa,
    interleave,
    is_even,
    is_iterable,
    new_list,
    new_iter,
    new_tuple,
    juxt,
    flatten,
    is_str_or_bytes,
    identity,
    is_map,
    is_seq,
    append,
    prepend,
    MultiFn,
    pipeline,
    rpartial,
    juxt,
    thread,
)


def test_gensym():
    identifier = gensym()
    assert isinstance(identifier, str)


def test_isa():
    assert isa(1, 1)

    class NewStyleClass(object):
        pass

    nsc = NewStyleClass()
    assert isa(nsc, object)


def test_is_even():
    assert is_even(2)


def test_is_iterable():
    assert is_iterable([])


def test_new_list():
    assert new_list(1, 2, 3) == [1, 2, 3]


def test_new_iter():
    assert list(new_iter(1, 2, 3)) == [1, 2, 3]


def test_new_tuple():
    assert new_tuple(1, 2, 3) == (1, 2, 3)


def test_flatten():
    assert list(flatten([[[1, 2, 3]]])) == [1, 2, 3]


def test_is_str_or_bytes():
    assert is_str_or_bytes("test")
    assert is_str_or_bytes(123) == False


def test_identity():
    assert identity(1) == 1


def test_is_map():
    assert is_map({"abc": 123})


def test_is_seq():
    assert is_seq([1, 2, 3])


def test_append():
    assert append([], 1, 2, 3) == [1, 2, 3]
    assert list(append([0], 1, 2, 3)) == [0, 1, 2, 3]
    assert append([], 1, 2, 3) == [1, 2, 3]
    assert list(append([0], 1, 2, 3)) == [0, 1, 2, 3]


def test_prepend():
    assert list(prepend(1, [1, 2, 3])) == [1, 1, 2, 3]


def test_MultiFn():
    def test_func1():
        pass

    def test_func2(*args, **kwargs):
        pass

    mfunc = MultiFn(test_func1)
    mfunc.default_func = test_func2
    mfunc.invoke("mfunc", {"test": "abc"}, {"test": "abc"})
    mfunc.register_default(test_func2)
    mfunc.unregister_default()
    mfunc.__call__()


def test_pipeline():
    five = partial(operator.add, 5)
    ten = partial(operator.add, 10)
    one = partial(operator.add, 1)

    assert pipeline(five, ten, one)(0) == 16


def test_rpartial():
    func = rpartial(get, 0)
    assert func([0]) == 0


def test_juxt():
    def test_func1(a, b, c):
        return "data 1"

    def test_func2(a, b, c):
        return "data 2"

    func = juxt(test_func1, test_func2)
    assert list(func(1, 2, 3)) == ["data 1", "data 2"]


def test_thread():
    assert thread(10, lambda x: x + 1, lambda x: x * 2) == 22

import string

from utilitiespackage.standard.string_ import (
    r,
    random_string,
    number_to_string,
    bytes_to_number,
    number_to_bytes,
    to_int,
    to_float,
    dollars_to_cents,
    slugify,
)


def test_random_string():
    assert len(random_string()) == 6
    assert len(random_string(length=10)) == 10


def test_number_to_string():
    assert number_to_string(12345678, "01") == "101111000110000101001110"
    assert number_to_string(12345678, "ab") == "babbbbaaabbaaaababaabbba"
    assert number_to_string(12345678, string.ascii_letters + string.digits) == "ZXP0"
    assert (
        number_to_string(12345, ["zero ", "one ", "two ", "three ", "four ", "five ", "six ", "seven ", "eight ", "nine "])
        == "one two three four five "
    )


def test_bytes_to_number():
    assert bytes_to_number(b"*") == 42
    assert bytes_to_number(b"\xff") == 255


def test_number_to_bytes():
    assert number_to_bytes(42) == b"*"
    assert number_to_bytes(255) == b"\xff"


def test_to_int():
    assert to_int("1") == 1
    assert to_int(1) == 1
    assert to_int("") == 0
    assert to_int(None) == 0
    assert to_int(0, default="Empty") == 0
    assert to_int(None, default="Empty") == "Empty"


def test_to_float():
    assert to_float("1.5") == 1.5
    assert to_float(1) == 1.0
    assert to_float("") == 0.0
    assert to_float("nan") == 0.0
    assert to_float("inf") == 0.0
    assert to_float("-inf", allow_nan=True) == float("-inf")
    assert to_float(None) == 0.0
    assert to_float(0, default="Empty") == 0.0
    assert to_float(None, default="Empty") == "Empty"


def test_dollars_to_cents():
    assert dollars_to_cents("$1") == 100
    assert dollars_to_cents("1") == 100
    assert dollars_to_cents(1) == 100
    assert dollars_to_cents("1e2") == 10000
    assert dollars_to_cents("-1$", allow_negative=True) == -100
    assert dollars_to_cents("1 dollar") == 100


def test_slugify():
    assert slugify("test") == "test"
    assert slugify("next test") == "next-test"
    assert slugify("more numbers 123456789") == "more-numbers-123456789"

import sys

del sys.modules["utilitiespackage.derived_settings"]
from utilitiespackage.derived_settings import set_vars


def test_set_vars():
    vars = set_vars()
    assert isinstance(vars, dict)
    assert len(vars.keys()) == 4
    for k, v in vars.items():
        assert isinstance(k, str)
        assert isinstance(v, str)

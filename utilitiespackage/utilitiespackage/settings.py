from utilitiespackage.derived_settings import APPDIR, SETUPFILEDIR, TESTDIR, MEMTEMPDIR


def set_vars():
    VERSION = "0.0.8"
    PRINT_VERBOSITY = "high"
    EXCLUDED_DIRS = [".DS_Store"]
    PROJECT_NAME = "utilitiespackage"
    TEMPDIR = "/tmp"
    TEXTTABLE_STYLE = ["-", "|", "+", "-"]
    DIRS = [f"{TEMPDIR}/utilitiesworkingdirs"]
    MINIMUM_PYTHON_VERSION = (3, 6, 0)
    COVERAGERC_PATH = f"{APPDIR}/.coveragerc"

    globals()["VERSION"] = VERSION
    globals()["PRINT_VERBOSITY"] = PRINT_VERBOSITY
    globals()["EXCLUDED_DIRS"] = EXCLUDED_DIRS
    globals()["PROJECT_NAME"] = PROJECT_NAME
    globals()["TEMPDIR"] = TEMPDIR
    globals()["TEXTTABLE_STYLE"] = TEXTTABLE_STYLE
    globals()["DIRS"] = DIRS
    globals()["MINIMUM_PYTHON_VERSION"] = MINIMUM_PYTHON_VERSION
    globals()["COVERAGERC_PATH"] = COVERAGERC_PATH

    return {
        "VERSION": VERSION,
        "PRINT_VERBOSITY": PRINT_VERBOSITY,
        "EXCLUDED_DIRS": EXCLUDED_DIRS,
        "PROJECT_NAME": PROJECT_NAME,
        "TEMPDIR": TEMPDIR,
        "TEXTTABLE_STYLE": TEXTTABLE_STYLE,
        "DIRS": DIRS,
        "MINIMUM_PYTHON_VERSION": MINIMUM_PYTHON_VERSION,
        "COVERAGERC_PATH": COVERAGERC_PATH,
    }


set_vars()

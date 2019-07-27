import os

from utilitiespackage.standard.os_ import chdir

def test_chdir():
    old_cwd = os.getcwd()
    with chdir("/"):
        print("current dir: {0}".format(os.getcwd()))
        print(chdir("/usr/"))

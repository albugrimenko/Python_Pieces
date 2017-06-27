"""
    Basic check for all required libraries.
    NOTE: must be modified for the needs of each specific project.

    Scikit-learn requires:
        - Python (>= 2.6 or >= 3.3)
        - NumPy (>= 1.6.1)
        - SciPy (>= 0.9)
    Sources:
        http://scikit-learn.org/stable/developers/advanced_installation.html
        http://www.lfd.upython ci.edu/~gohlke/pythonlibs/
        http://conda.pydata.org/miniconda.html
        http://winpython.github.io/ - Windows installation.

    @author: Alex Bugrimenko
"""

import sys
import importlib


def check_lib(lib_name):
    """ Checks if a specified library is installed. """
    res = False
    print("... checking for {0} ...".format(lib_name))
    try:
        # import lib_name
        importlib.import_module(lib_name)
        print("+++ {0} ... OK".format(lib_name))
        res = True
    except ImportError:
        print("--! ERROR: {0} is MISSING:\n--! {1}".format(lib_name, sys.exc_info()[1]))
    except:
        print("--! ERROR:", sys.exc_info())
    return res


def check_required_libs():
    """ Checks all required libraries """
    check_lib("json")   # used in config_json
    check_lib("time")
    check_lib("datetime")
    check_lib("dateutil")

    check_lib("unittest")

    # ML libs
    # check_lib("pickle")
    # check_lib("numpy")
    # check_lib("scipy")
    # check_lib("sklearn")
    # check_lib("pandas")


if __name__ == "__main__":
    check_required_libs()

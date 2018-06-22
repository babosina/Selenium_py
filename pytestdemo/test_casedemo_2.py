"""
file name should start with test
test method name should start with test

py.test test_mod.py  # run tests in module
py.test somepath  # run all tests below somepath
py.test test_module.py::test_method  # only run test_method in test_module

-s to print statements
-v verbose
"""


import pytest


@pytest.fixture()
def set_up():
    print("Running test_casedemo2 setup")
    yield
    print("Running test_casedemo2 teardown")


def test_method_a(set_up):
    print("Method A")


def test_method_b(set_up):
    print("Method B")

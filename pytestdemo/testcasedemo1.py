import pytest


@pytest.fixture()
def set_up():
    print("Set up before every method")


def test_method_a():
    print("Running test method A")


def test_method_b(set_up):
    print("Running test method B")

import pytest


# @pytest.yield_fixture() - old syntax to use yield
@pytest.fixture()
def set_up():
    print("Set up before every method")
    yield
    print("Teardown after every method")


def test_method_a(set_up):
    print("Running test method A")


def test_method_b(set_up):
    print("Running test method B")

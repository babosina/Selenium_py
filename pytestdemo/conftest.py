import pytest


@pytest.fixture()
def set_up():
    print("Running conftest setup")
    yield
    print("Running conftest teardown")


@pytest.fixture(scope='module')  # run ONCE at the start of the module tests
def set_up_once():
    print("Running conftest setup ONCE")
    yield
    print("Running conftest teardown ONCE")

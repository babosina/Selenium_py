import pytest


# @pytest.fixture(scope='module') # run ONCE at the start of the module tests
@pytest.fixture(scope='class')  # comment it to run module tests
def set_up_once(request ,browser, ostype):
    print("Running conftest setup ONCE")
    if browser == "firefox":
        value = 10
        print("Running tests on FF")
    else:
        value = 20
        print("Running tests on Chrome")

    if request.cls is not None:
        request.cls.value = value
    yield value
    print("Running conftest teardown ONCE")


@pytest.fixture()
def set_up():
    print("Running conftest setup")
    yield
    print("Running conftest teardown")


def pytest_addoption(parser):
    parser.addoption("--browser")
    parser.addoption("--ostype", help='Type of operating system')


@pytest.fixture(scope="session")
def browser(request):
    return request.config.getoption("--browser")


@pytest.fixture(scope="session")
def ostype(request):
    return request.config.getoption("--ostype")

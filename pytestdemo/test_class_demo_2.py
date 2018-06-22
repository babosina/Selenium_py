import pytest
from pytestdemo.class_to_test import ClassToTest


@pytest.mark.usefixtures("set_up_once", "set_up")
class TestClassDemo:

    @pytest.fixture(autouse=True)
    def class_setup(self, set_up_once):
        self.abc = ClassToTest(self.value)

    def test_method_a(self):
        result = self.abc.sum(2, 5)
        assert result == 12
        print("Method A")

    def test_method_b(self):
        print("Method B")

import pytest
from pytestdemo.class_to_test import ClassToTest


@pytest.mark.usefixtires("set_up_once", "set_up")
class TestReporting:

    @pytest.fixture(autouse=True)
    def class_setup(self):
        self.abc = ClassToTest(10)

    def test_method_a(self):
        result = self.abc.sum(2, 8)
        assert result == 20
        print("Running method A")

    def test_method_b(self):
        result = self.abc.sum(2, 8)
        assert result > 20
        print("Running method B")

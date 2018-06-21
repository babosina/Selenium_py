import pytest


@pytest.mark.run(order=2)
def test_method_a(set_up_once, set_up):
    print("Method A")


@pytest.mark.run(order=1)
def test_method_b(set_up_once, set_up):
    print("Method B")


@pytest.mark.run(order=3)
def test_method_c(set_up_once, set_up):
    print("Method C")


@pytest.mark.run(order=5)
def test_method_d(set_up_once, set_up):
    print("Method D")


@pytest.mark.run(order=4)
def test_method_e(set_up_once, set_up):
    print("Method E")


@pytest.mark.run(order=6)
def test_method_f(set_up_once, set_up):
    print("Method F")

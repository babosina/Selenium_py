import pytest


def test_method_a(set_up_once, set_up):
    print("Conftest 1: Method A")


def test_method_b(set_up_once, set_up):
    print("Conftest 1: Method B")

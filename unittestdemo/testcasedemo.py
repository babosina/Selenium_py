import unittest


class UnitTestDemo(unittest.TestCase):

    def setUp(self):
        print("This is a SetUp method to run before every test")

    def test_method_1(self):
        print("Running test method 1")

    def test_method_2(self):
        print("Running test method 2")

    def tearDown(self):
        print("Cleaning the test environment")


if __name__ == "__main__":
    unittest.main(verbosity=2)

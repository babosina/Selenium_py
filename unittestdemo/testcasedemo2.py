import unittest


class UnitTestDemo(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print("*" * 25)
        print("Run SetUp only once")
        print("*" * 25, "\n")

    def setUp(self):
        print("This is a SetUp method to run before every test")

    def test_method_1(self):
        print("Running test method 1")

    def test_method_2(self):
        print("Running test method 2")

    @classmethod
    def tearDownClass(cls):
        print("*" * 25)
        print("Run TearDown only once")
        print("*" * 25, "\n")

    def tearDown(self):
        print("Cleaning the test environment")


if __name__ == "__main__":
    unittest.main(verbosity=2)

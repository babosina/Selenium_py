import unittest
from unittestdemo.testclass1 import TestClass1
from unittestdemo.testclass2 import TestClass2

# get all tests from TestClass1 and TestClass2
tc1 = unittest.TestLoader().loadTestsFromTestCase(TestClass1)
tc2 = unittest.TestLoader().loadTestsFromTestCase(TestClass2)

# create a test suite combining TestClass1 and TEstClass2
smoke_test = unittest.TestSuite([tc1, tc2])

unittest.TextTestRunner(verbosity=1).run(smoke_test)

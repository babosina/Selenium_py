"""
How to use test class to wrap methods under one class
Learn about autouse keywords in fixtures
Assert the result to create a real test scenario
"""


class ClassToTest:

    def __init__(self, value):
        self.value = value

    def sum(self, a, b):
        return a + b + self.value

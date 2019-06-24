"""test functions for app class
usage: python -m unittest -v tests/app_test.py
"""
import unittest

from app import App

class TestAppClass(unittest.TestCase):
    """tests for app
    Arguments:
        unittest {unit test} -- class
    """
    def __init__(self, methodName):
        self.app = App()
        self.msg = "unit testing"
        super().__init__(methodName)

    def test_set_up(self):
        """test app init
        """
        self.assertEqual(self.app.get_message(), "initialized")

    def test_set_message(self):
        """testing set method
        """
        self.app.set_message(self.msg)
        self.assertEqual(self.app.get_message(), self.msg)

    def test_get_message(self):
        """test get method
        """
        self.assertIsNotNone(self.app.get_message())

if __name__ == '__main__':
    unittest.main()

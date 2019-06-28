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
        super().__init__(methodName)

    # def test_db_conn(self):
    #     """test db connection
    #     """
    #     self.assertIsNotNone(self.app._db.conn)

    # def test_update_db(self):
    #     """testing set method
    #     """
    #     self.assertIsNone(self.app.set_row('test', 'testid'))

    def test_get_message(self):
        """test get method
        """
        self.app.set_row('test', 'testid')
        ret = self.app.get_row()
        self.assertIn('test', ret)
        self.app.close()

if __name__ == '__main__':
    unittest.main()

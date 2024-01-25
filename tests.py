import unittest
from password import test_valid_password

class TestPasswordMethods(unittest.TestCase):

    def test_password(self):
        pwd = 'asweY76*#'
        valid = test_valid_password(pwd)
        self.assertTrue(valid)

if __name__ == '__main__':
    unittest.main()
    
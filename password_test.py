import unittest
from password import User

class TestUser(unittest.TestCase):
    '''
    Test class that defines test cases for the user class behaviours.

    Args:
        unittest.TestCase: TestCase class that helps in creating test cases
    '''
def setUp(self):
    self.new_user=User("Betty","12056")
    
def test_init(self):
    self.assertEqual(self.new_user.user_name, "Betty")
    self.assertEqual(self.new_user.user_password, "12056")
    
if __name__ == '__main__':
    unittest.main()
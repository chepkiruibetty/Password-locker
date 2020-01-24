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
    
def test_save_user(self):
    '''
    test_save_user test case to test if the user object is saved into
    the user list
    add 
    '''
    self.new_user.save_user() # saving the new users
    self.assertEqual(len(User.user_list), 1)
    
def test_save_multiple_users(self):
    self.new_user.save_user()
    test_user = User("Gakii", "12345")
    test_user.save_user()
    self.assertEqual(len(User.user_list), 2)

    
if __name__ == '__main__':
    unittest.main()
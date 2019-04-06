import unittest
from login import Login

class TestLogin(unittest.TestCase):
    '''
    Test class that defines test cases for the login class behaviour.
    Args:
    unittest.TestCase: TestCase class that helps in creating test cases
    '''

     def setUp(self):
            '''
        Set up method to run before each test cases.
        '''
        self.new_login = Login("lilomuso","lilo89","lilo89","lilo89") # create login object
    def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''

        self.assertEqual(self.new_login.username,"lilomuso")
        self.assertEqual(self.new_login.password,"lilo89")
        self.assertEqual(self.new_login.new_password,"lilo89")
        self.assertEqual(self.new_login.confirm_password,"lilo89")

    def test_save_login(self):
        '''
        test_save_login test case to test is the login object is saved into the login
        '''
        self.new_login.save_login()#saving the new user
        self.assertEqual(len(Login.login),1)

    def test_save_multiple_login(self):
        '''
        test_save_multiple_login to check if we can save multiple login object to our user
        '''
        self.new_login.save_login()
        test_login = Login("Test","login","lilo89","lilo89")#new login
        test_login.save_login()
        self.assertEqual(len(Login.login),2)   

    def test_login_exists(self):
            '''
        test to check if we can return a Boolean if we cannot find the login.
        '''
        self.new_login.save_login()
        test_login = Login("Test","login","lilo89","lilo89")#new user
        test_login.save_login()
        login_exists = Login.login_exist("0701234567")
        self.assertTrue(login_exists)



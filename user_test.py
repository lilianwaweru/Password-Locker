import unittest
from user import User

class TestUser(unittest.TestCase):
    '''
    Test class that defines test cases for the user class behaviour.
    Args:
    unittest.TestCase: TestCase class that helps in creating test cases
    '''
    def setUp(self):
        '''
        Set up method to run before each test cases.
        '''
        self.new_user = User("James","Muriuki","0712345678","james@ms.com") # create user object


    def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''

        self.assertEqual(self.new_user.first_name,"James")
        self.assertEqual(self.new_user.last_name,"Muriuki")
        self.assertEqual(self.new_user.phone_number,"0712345678")
        self.assertEqual(self.new_user.email,"james@ms.com")


    def test_save_user(self):
        '''
        test_save_user test case to test is the user object is saved into the user
        '''
        self.new_user.save_user()#saving the new user
        self.assertEqual(len(User.user),1)

    def test_save_multiple_user(self):
        '''
        test_save_multiple_user to check if we can save multiple user object to our user
        '''
        self.new_user.save_user()
        test_user = User("Test","user","0701234567","test@user.com")#new user
        test_user.save_user()
        self.assertEqual(len(User.user),2)   

    def tearDown(self):
        '''
        tearDown method that does clean up after each test case has run.
        '''
        User.user=[]
    def test_save_multiple_user(self):
        '''
        test_save_multiple_user to check if we can save multiple user object to our user
        '''
        self.new_user.save_user()
        test_user = User("Test","user","0701234567","test@user.com")
        test_user.save_user()
        self.assertEqual(len(User.user),2)

#more test above
    def test_delete_user(self):
        '''
        test_delete_user to test if we can remove a user from our user
        '''
        self.new_user.save_user()
        test_user = User("Test","user","0701234567","test@user.com")
        test_user.save_user()
        self.new_user.delete_user()#deleting a user object
        self.assertEqual(len(User.user), 1)
        
    def test_find_user_by_number(self):
        '''
        test to check if we can find a user by phone number and display information
        '''
        self.new_user.save_user()
        test_user = User("Test", "user", "0701234567", "test@user.com")
        test_user.save_user()

        found_user = User.find_by_number("0701234567")
        self.assertEqual(found_user.email, test_user.email)
    def test_user_exists(self):
        '''
        test to check if we can return a Boolean if we cannot find the contact.
        '''
        self.new_user.save_user()
        test_user = User("Test","user","0701234567","test@user.com")#new user
        test_user.save_user()
        user_exists = User.user_exist("0701234567")
        self.assertTrue(user_exists)


if __name__ == '__main__':
        unittest.main()



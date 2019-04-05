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
        set up method to run before each test cases.
        '''
        self.new_user = User("lilo","muso","0712345678","lilo@lw.com","lilomuso","lilo1234")

    def test_init(self):
        '''
        test_init test case to test if the object is intitialized properly
        '''
        self.asssertEqual(self.new_user.first_name,"lilo")
        self.asssertEqual(self.new_user.last_name,"muso")
        self.asssertEqual(self.new_user.phone_number,"071234568")
        self.asssertEqual(self.new_user.email,"lilo@lw.com")
        self.asssertEqual(self.new_user.username,"lilomuso")
        self.asssertEqual(self.new_user.password,"lilo1234")


    def test_save_user(self):
        '''
        test_save_user test case to test is the user object is saved into the user
        '''
        self.new_user.save_user()#saving the new user
        self.asssertEqual(len(User.user),1)



if __name__ == '__main__':
        unittest.main()



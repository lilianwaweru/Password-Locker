import run_unittest
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
        

class Login:
    """
    Class that generates new instances of login
    """

    login = []

    def __init__(self,username,password,new_password,confirm_password):
        self.username = username
        self.password = password
        self.new_password = new_password
        self.confirm_password = confirm_password

     def save_login(self):
            '''
        save_login method saves contact objects into login
        '''
        Login.login.append(self)

      @classmethod
    def login_exist(cls,number):
        '''
        Method that checks if a user exists from the login.
        Args:
            password:password to search if it exists
        Returns:
            Boolean:True or false depending if the user exists
        '''
        for login in cls.login:
            if login.password == password:
                return True
        return False  
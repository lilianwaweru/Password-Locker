class Login:
    """
    Class that generates new instances of login
    """

    login = []

    def __init__(self, social, firstname, lastname, username,password):
        self.social = social
        self.firstname = firstname
        self.lastname = lastname
        self.username = username
        self.password = password

    def save_login(self):
        '''
        save_login method saves contact objects into login
        '''
        Login.login.append(self)

    @classmethod
    def login_exist(cls,password):
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

    @classmethod
    def display_login(cls):
        '''
        method that returns the login list
        '''
        return cls.login
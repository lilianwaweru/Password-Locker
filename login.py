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
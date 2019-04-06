class User:
    """
    Class that generates new instances of user
    """
    

    user = []

    def __init__(self,first_name,last_name,phone_number,email):
        self.first_name = first_name
        self.last_name = last_name
        self.phone_number = phone_number
        self.email = email
        # self.username = username
        # self.password = password

    def save_user(self):
        '''
        save_user method saves contact objects into user
        '''
        User.user.append(self)

    def delete_user(self):
        '''
        delete_user method deletes a saved user from the user
        '''
        User.user.remove(self)
        
    @classmethod
    def find_by_number(cls,number):
        '''
        method that takes in a number and returns a user that matches that number
        Args:
            number:phone number to search
        Returns:
            User of that matches te number.
        '''
        for user in cls.user:
            if user.phone_number == number:
                return user

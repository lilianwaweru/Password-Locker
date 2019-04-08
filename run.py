#!/usr/bin/env python3.6
from user import User
from login import Login

def create_user(fname,lname,phone,email):
    '''
    function to create new user
    '''
    new_user = User(fname,lname,phone,email)
    return new_user

def create_login(username,password,npassword,cpassword):
    '''
    function to create new login
    '''
    new_login = Login(username,password,npassword,cpassword)
    return new_login

def save_user(user):
    '''
    functon to save user
    '''
    user.save_user()

def save_login(login):
        '''
    functon to save login
    '''
        login.save_login()

def del_user(user):
    '''
    function to delete a user
    '''
    user.delete_user()

def find_user(number):
    '''
    function that finds a user by number and returns the user
    '''
    return User.find_by_number(number)

def check_existing_user(number):
    '''
    function that checks if a user exists with that number and return a boolean
    '''
    return User.user_exist(number)

def display_user():
    '''
    Function that returns all the saved users
    '''
    return User.display_user()

def main():
    print("Hello,welcome to password locker.what is your name?")
            user_name = input()
            print(f"Hello{user_name}.what would you like to do?")
            print('\n')
            while True:
                    print("use these short codes : cc - create a new user, dc - display user, fc - find a user, ex - exit the user")
                    short_code = input().lower()
                    if short_code == 'cc':
                            print("New User")
                            print("-"*10)

                            print("first name....")
                            f_name = input()

                            print("Last name....")
                            l_name = input()

                            print("phone number....")
                            p_number = input()

                            print("email address....")
                            e_address = input()

                            save_user(create_user(f_name,l_name,p_number,e_address))#create and save new user
                            print ('\n')
                            print(f"New User {f_name} {l_name} created")
                            print ('\n')
                    elif short_code == 'dc':
                            if display_user():
                                    print("Here is a list of all your user")
                                    print('\n')
                                    for user in display_user()
                                         print(f"{user.first_name} {user.last_name}.....{user.phone_number}")
                                    print('\n')
                            else:
                                    print('\n')
                                    print("You don't seem to have any user saved yet")
                                    print('\n')

                    elif short_code == 'fc':
                            print("Enter the number you want to search for")
                            search_number = input()
                            if check_existing_user(search_number):
                                search_user = find_user(search_number)
                                print(f"{search_user.first_name} {search_user.last_name}")
                                print('-'*20)

                                print(f"phone number.......{search_user.phone_number}")
                                print(f"Email address.......{search_user.email}")
                            
                            else:
                                print("That user does not exist")
                    elif short_code == "ex":
                        print("Bye......")
                        break
                    else:
                         print("I really didn't get that.please use the short codes")


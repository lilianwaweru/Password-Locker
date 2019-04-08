#!/usr/bin/env python3.6
from user import User
from login import Login
import random

def create_user(fname,lname,phone,email,username,password):
    '''
    function to create new user
    '''
    new_user = User(fname,lname,phone,email,username,password)
    return new_user

def create_login(social, firstname, lastname, username,password):
    '''
    function to create new login
    '''
    new_login = Login(social, firstname, lastname, username,password)
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

def check_existing_user(username):
    '''
    function that checks if a user exists with that number and return a boolean
    '''
    return User.user_exist(username)

def check_existing_login(password):
    '''
    function that checks if a user exists with that number and return a boolean
    '''
    return Login.login_exist(password)


def display_login():
    '''
    Function that returns all the saved users
    '''
    return Login.display_login()

def main():
    print("Hello,welcome to password locker.what is your name?")
    user_name = input()
    print(f"Hello{user_name}.what would you like to do?")
    print('\n')
    while True:
        print("use these short codes : ca - create a new account,cc - create credentials li - login, dc - display user, fc - find a user, ex - exit the user")
        short_code = input().lower()
        if short_code == 'ca':
            # print("New User")
            # print("-"*10)
            while True:
                print("first name....")
                f_name = input()
                print("Last name....")
                l_name = input()
                print("phone number....")
                p_number = input()
                print("email address....")
                e_address = input()
                print("username....")
                username = input()
                print("password....")
                password = input()

                if f_name == "" or l_name == "" or p_number == "" or e_address == "" or username == "" or password == "":
                    print('Failed. One input field was blank')

                else:
                    save_user(create_user(f_name,l_name,p_number,e_address,username,password))#create and save new user
                    print ('\n')
                    print(f"New User {f_name} {l_name} created successfully")
                    print ('\n')
                    print("Please Login to create credentials")
                break

        elif short_code == 'cc':
            # print("New Login")
            print("-"*10)
            print("Enter username....")
            username = input()
            print("Enter password")
            password = input()
            if check_existing_user(username):
                print("Welcome Back")
                print(f"New Login {username} {password} login successful")
                print("Enter social media you want to create")
                social = input()
                print("Enter your firstname")
                firstname = input()
                print("Enter your lastname")
                lastname = input()
                print("Enter your username")
                username = input()
                print("You can press gp - to generate a password or cp - to create your own password")
                print ('\n')
                password_choice = input()
                if password_choice == 'gp':
                    symbols = "abcdefghijklmonpqrstuvwxyz0123456789"
                    password = "".join(random.choice(symbols) for _ in range(9))
                    print(f"Here is your password  {password}")
                    print('\n')
                elif password_choice == 'cp':
                    print("Enter Password")
                    password = input()

                    save_login(create_login(social, firstname, lastname, username,password))   
                    print('\n')       
                    print(f" {social} account has been created successfully")
            else:
                    print("You entered wrong account details")
                    print('\n')
                    print("-"*10)
                    username = input()
                    print("Re-enter username")
                    print('\n')
                    print("-"*10)
                    password = input()
                    print("Re-enter password")
                    print('\n')
                    print("-"*10)
                    if check_existing_login(password):
                        print(f"Login successfully for{username}")
                    else:
                        print(f"you dont have an account")

        elif short_code == 'dc':
            if display_login():
                print("Your Current user accounts are:")
                print("*"*10)
                for info in display_login():
                    print(f" Social Media {info.social} \n First Name: {info.firstname} \n Second Name: {info.lastname} \n Username: {info.username} \nPassword {info.password}")

            else:
                print('\n')
                print("You dont have any credentials")
        elif short_code == "ex":
                    print("Bye .......")
                    break
        else:
            print("I really didn't get that. Please use the short codes")

            
if __name__ == '__main__':
    main()

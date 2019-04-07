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

  

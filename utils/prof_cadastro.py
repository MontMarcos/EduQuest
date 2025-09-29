#!/usr/bin/env python
# -*- coding: utf-8 -*-

from os.path import dirname, realpath, join
from controls.json_maneger import JsonManager
from getpass import getpass
from passlib.hash import bcrypt

class JLogin(JsonManager):

    def __init__(self):
        self.__root = dirname(realpath(__file__))  
        self.__path_data = join(self.__root, '../data/data.json')  
        self.__logged_in_user = None

    def sign_in(self):
        print('### Sign In ###')

        users = self.read_json(self.__path_data)

        while True:
            username = input('Enter your username (max 20 chars): ').strip()
            if not username:
                print("Username cannot be empty.")
            elif len(username) > 20:
                print("Username must be at most 20 characters.")
            elif any(user['username'] == username for user in users):
                print("Username already exists. Choose another one.")
            else:
                break

        while True:
            password = getpass('Enter your password (max 8 chars): ').strip()
            if not password:
                print("Password cannot be empty.")
                continue
            if len(password) > 8:
                print("Password must be at most 8 characters.")
                continue
            password_verify = getpass('Repeat your password: ').strip()
            if password != password_verify:
                print('Passwords do not match!')
                continue
            break

        hash_password = bcrypt.hash(password)
        self.create_json(self.__path_data, username, hash_password)
        print('Registration done!')

    def login(self):
        print('### Login ###')

        users = self.read_json(self.__path_data)
        if not users:
            print("No user registered. Please sign in first.")
            return False

        username = input('Enter your username: ').strip()
        password = getpass('Enter your password: ').strip()

        for user in users:
            if user['username'] == username:
                if bcrypt.verify(password, user['password']):
                    print(f"Login successful! Welcome {username}")
                    self.__logged_in_user = username
                    return True
                else:
                    print("Incorrect password!")
                    return False

        print("Username does not exist!")
        return False

    def logout(self):
        if self.__logged_in_user:
            print(f"{self.__logged_in_user} has been logged out.")
            self.__logged_in_user = None
        else:
            print("No user is logged in.")

    def get_logged_in_user(self):
        return self.__logged_in_user


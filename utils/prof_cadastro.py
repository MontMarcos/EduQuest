#!/usr/bin/env python
# -*- coding: utf-8 -*-

from os.path import dirname, realpath, join, isfile
from controls.json_maneger import JsonManager
from getpass import getpass
from passlib.hash import bcrypt
import json


class JLogin(JsonManager):

    def __init__(self):
        self.root = dirname(realpath(__file__))
        self.path_data = join(self.root, '../data/data.json')

    def sign_in(self):
        print('### Sign In ###')

        while True:
            username = input('Enter your username (max 20 chars): ').strip()
            if not username:
                print("Username cannot be empty.")
            elif len(username) > 20:
                print("Username must be at most 20 characters.")
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

        self.create_json(self.path_data, username, hash_password)
        print('Registration done!')

    def login(self):
        print('### Login ###')

        users = self.read_json(self.path_data)
        if not users:
            print("No user registered. Please sign in first.")
            return False

        username = input('Enter your username: ').strip()
        password = getpass('Enter your password: ').strip()

        # procura o usuário na lista
        for user in users:
            if user['username'] == username and bcrypt.verify(password, user['password']):
                print(f"Login successful! Welcome {username}")
                return True

        print("Username or password incorrect!")
        return False
